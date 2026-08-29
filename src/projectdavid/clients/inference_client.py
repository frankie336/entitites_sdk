import asyncio
import json
import time
from typing import Any, AsyncGenerator, Dict, List, Optional

import httpx
from dotenv import load_dotenv
from projectdavid_common import UtilsInterface, ValidationInterface
from projectdavid_common.validation import StreamRequest
from pydantic import ValidationError

from projectdavid.clients.base_client import BaseAPIClient

load_dotenv()
logging_utility = UtilsInterface.LoggingUtility()


class InferenceClient(BaseAPIClient):
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        super().__init__(
            base_url=base_url,
            api_key=api_key,
            timeout=280.0,
            connect_timeout=10.0,
            read_timeout=280.0,
            write_timeout=30.0,
        )
        self._async_client: Optional[httpx.AsyncClient] = None
        logging_utility.info("InferenceClient initialized using BaseAPIClient.")

    @property
    def async_client(self) -> httpx.AsyncClient:
        if self._async_client is None or self._async_client.is_closed:
            self._async_client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=httpx.Timeout(280.0, connect=10.0),
                headers=({"X-API-Key": self.api_key} if self.api_key else {}),
            )
        return self._async_client

    async def aclose(self):
        if self._async_client:
            await self._async_client.aclose()

    async def create_completion(self, **kwargs) -> Dict[str, Any]:
        """
        Returns a single assembled completion dict.

        Uses stream=False to let the server buffer and assemble the response —
        more efficient than streaming and reassembling client-side.
        Falls back to client-side assembly if the server returns SSE chunks.
        """
        run_id = kwargs.get("run_id", "unknown")
        final_text = ""

        # Ask the server to buffer — single JSON response, no SSE parsing overhead.
        # stream_inference_response handles the non-streaming path transparently:
        # it yields the assembled content as a single chunk so this loop still works.
        async for chunk in self.stream_inference_response(**kwargs, stream=False):
            final_text += chunk.get("content", "")

        return {
            "id": f"chatcmpl-{run_id}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": kwargs.get("model"),
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": final_text},
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
        }

    def create_completion_sync(self, **kwargs) -> Dict[str, Any]:
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        if loop.is_running():
            from concurrent.futures import ThreadPoolExecutor

            with ThreadPoolExecutor() as executor:
                future = executor.submit(
                    lambda: asyncio.run(self.create_completion(**kwargs))
                )
                return future.result()
        else:
            return loop.run_until_complete(self.create_completion(**kwargs))

    def create_stateless_completion(
        self,
        *,
        model: str,
        prompt: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        provider_api_key: Optional[str] = None,
        max_tokens: int = 256,
        temperature: float = 0.2,
        top_p: float = 1.0,
    ) -> Dict[str, Any]:
        """Run one bounded completion without conversation entity identifiers."""
        if (prompt is None) == (messages is None):
            raise ValueError("Provide exactly one of prompt or messages")

        payload: Dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "stream": False,
            "stateless": True,
        }
        if prompt is not None:
            payload["prompt"] = prompt
        if messages is not None:
            payload["messages"] = messages
        if provider_api_key is not None:
            payload["api_key"] = provider_api_key

        response = self.client.post("/v1/completions", json=payload)
        response.raise_for_status()
        completion = response.json()

        choices = completion.get("choices")
        if not isinstance(choices, list) or not choices:
            raise ValueError("Stateless completion response has no choices")
        if not isinstance(choices[0], dict) or not isinstance(
            choices[0].get("text"), str
        ):
            raise ValueError("Stateless completion response has no text")

        return completion

    async def stream_inference_response(
        self,
        model: str,
        thread_id: str,
        message_id: str,
        run_id: str,
        assistant_id: str,
        user_content: Optional[str] = None,
        api_key: Optional[str] = None,
        meta_data: Optional[Dict[str, Any]] = None,
        timeout: float = 600.0,
        stream: bool = True,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Streams or buffers inference depending on the `stream` flag.

        stream=True  (default):
            Opens an SSE connection to /v1/completions and yields each chunk
            as it arrives. Used by SynchronousInferenceStream and any caller
            that needs live token-by-token delivery.

        stream=False:
            Sends a regular POST to /v1/completions with stream=False in the
            payload. The server runs the full generator, assembles the content,
            and returns a single JSON object. This method yields that object as
            one chunk so all callers (including create_completion) stay unchanged.
            All server-side side effects (tool calls, file generation, status
            events) still execute — only the delivery mechanism differs.

        NOTE on api_key vs self.api_key:
        - self.api_key  → platform API key; sent as X-API-Key header
                          so the server can authenticate the caller.
        - api_key param → LLM provider key (Together, OpenAI, Hyperbolic etc.);
                          sent only in the JSON body payload, never in headers.
        """
        payload: Dict[str, Any] = {
            "model": model,
            "api_key": api_key,
            "thread_id": thread_id,
            "message_id": message_id,
            "run_id": run_id,
            "assistant_id": assistant_id,
            "stream": stream,
        }

        if user_content:
            payload["content"] = user_content

        if meta_data:
            payload["meta_data"] = meta_data

        try:
            StreamRequest(**payload)
        except ValidationError as e:
            logging_utility.error("Payload validation error: %s", e.json())
            raise

        headers = {"X-API-Key": self.api_key} if self.api_key else {}

        # ── PATH A: BUFFERED ──────────────────────────────────────────────────
        # Regular POST — server returns a single JSON object.
        # Yield as one chunk so callers are transparent to the mode.
        if not stream:
            async with httpx.AsyncClient(
                base_url=self.base_url,
                timeout=httpx.Timeout(timeout, connect=10.0),
                headers=headers,
            ) as client:
                try:
                    response = await client.post("/v1/completions", json=payload)
                    response.raise_for_status()
                    data = response.json()
                    # Server returns {run_id, content, type, model, elapsed_s}
                    # Normalise to the same shape as a content chunk so
                    # callers don't need to branch.
                    yield {
                        "type": "content",
                        "content": data.get("content", ""),
                        "run_id": data.get("run_id", run_id),
                        "model": data.get("model", model),
                        "elapsed_s": data.get("elapsed_s"),
                    }
                except httpx.HTTPStatusError as e:
                    logging_utility.error(
                        f"Buffered inference HTTP error: "
                        f"{e.response.status_code} {e.request.url}"
                    )
                    raise
                except Exception as e:
                    logging_utility.error(f"Buffered inference error: {e}")
                    raise
            return

        # ── PATH B: STREAMING ─────────────────────────────────────────────────
        # SSE connection — yield each chunk as it arrives.
        async with httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(timeout, connect=10.0),
            headers=headers,
        ) as client:
            try:
                async with client.stream(
                    "POST", "/v1/completions", json=payload
                ) as response:
                    response.raise_for_status()
                    lines = response.aiter_lines()
                    try:
                        async for line in lines:
                            line = line.strip()
                            if not line or not line.startswith("data:"):
                                continue

                            data_str = line[len("data:") :].strip()
                            if data_str == "[DONE]":
                                break

                            try:
                                yield json.loads(data_str)
                            except json.JSONDecodeError:
                                continue
                    finally:
                        await lines.aclose()

            except httpx.HTTPStatusError as e:
                logging_utility.error(
                    f"Inference Stream HTTP Error: "
                    f"{e.response.status_code} {e.request.url}"
                )
                raise
            except Exception as e:
                logging_utility.error(f"Inference Stream Unexpected Error: {e}")
                raise

    def close(self):
        if hasattr(self, "client") and self.client:
            self.client.close()
