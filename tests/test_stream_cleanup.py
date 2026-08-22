import asyncio
from dataclasses import dataclass, field
from typing import Any, List, Optional

import httpx
import pytest

from projectdavid.clients import inference_client as inference_module
from projectdavid.clients.inference_client import InferenceClient
from projectdavid.clients.synchronous_inference_wrapper import (
    SynchronousInferenceStream,
)

VALID_STREAM_REQUEST = {
    "model": "vllm/Qwen/Qwen2.5-3B-Instruct",
    "thread_id": "thread_test",
    "message_id": "message_test",
    "run_id": "run_test",
    "assistant_id": "asst_test",
}


class TrackingLineIterator:
    def __init__(self, lines: List[str]) -> None:
        self._lines = iter(lines)
        self.closed = False

    def __aiter__(self) -> "TrackingLineIterator":
        return self

    async def __anext__(self) -> str:
        try:
            return next(self._lines)
        except StopIteration as exc:
            raise StopAsyncIteration from exc

    async def aclose(self) -> None:
        self.closed = True


@dataclass
class StreamState:
    lines: List[str] = field(default_factory=list)
    status_code: int = 200
    line_iterator: Optional[TrackingLineIterator] = None
    response_entered: bool = False
    response_exited: bool = False
    client_entered: bool = False
    client_exited: bool = False


class FakeResponse:
    def __init__(self, state: StreamState) -> None:
        self._state = state
        self.status_code = state.status_code
        self.request = httpx.Request("POST", "http://test/v1/completions")

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            response = httpx.Response(self.status_code, request=self.request)
            raise httpx.HTTPStatusError(
                "stream request failed",
                request=self.request,
                response=response,
            )

    def aiter_lines(self) -> TrackingLineIterator:
        iterator = TrackingLineIterator(self._state.lines)
        self._state.line_iterator = iterator
        return iterator


class FakeResponseContext:
    def __init__(self, state: StreamState) -> None:
        self._state = state
        self._response = FakeResponse(state)

    async def __aenter__(self) -> FakeResponse:
        self._state.response_entered = True
        return self._response

    async def __aexit__(self, *_exc: Any) -> None:
        self._state.response_exited = True


class FakeAsyncClient:
    def __init__(self, state: StreamState, *_args: Any, **_kwargs: Any) -> None:
        self._state = state

    async def __aenter__(self) -> "FakeAsyncClient":
        self._state.client_entered = True
        return self

    async def __aexit__(self, *_exc: Any) -> None:
        self._state.client_exited = True

    def stream(self, *_args: Any, **_kwargs: Any) -> FakeResponseContext:
        return FakeResponseContext(self._state)


def install_fake_async_client(
    monkeypatch: pytest.MonkeyPatch, state: StreamState
) -> None:
    monkeypatch.setattr(
        inference_module.httpx,
        "AsyncClient",
        lambda *args, **kwargs: FakeAsyncClient(state, *args, **kwargs),
    )


def make_inference_client() -> InferenceClient:
    return InferenceClient(base_url="http://test", api_key="test-api-key")


def consume_stream(client: InferenceClient) -> List[dict]:
    async def consume() -> List[dict]:
        return [
            chunk
            async for chunk in client.stream_inference_response(**VALID_STREAM_REQUEST)
        ]

    return asyncio.run(consume())


def test_full_stream_closes_line_response_and_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = StreamState(
        lines=[
            'data: {"type":"content","content":"hello"}',
            "data: [DONE]",
        ]
    )
    client = make_inference_client()
    install_fake_async_client(monkeypatch, state)

    try:
        chunks = consume_stream(client)
    finally:
        client.close()

    assert chunks == [{"type": "content", "content": "hello"}]
    assert state.line_iterator is not None and state.line_iterator.closed
    assert state.response_entered and state.response_exited
    assert state.client_entered and state.client_exited


def test_early_consumer_exit_closes_line_response_and_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = StreamState(
        lines=[
            'data: {"type":"content","content":"first"}',
            'data: {"type":"content","content":"second"}',
            "data: [DONE]",
        ]
    )
    client = make_inference_client()
    install_fake_async_client(monkeypatch, state)

    async def consume_one() -> dict:
        stream = client.stream_inference_response(**VALID_STREAM_REQUEST)
        try:
            return await anext(stream)
        finally:
            await stream.aclose()

    try:
        first = asyncio.run(consume_one())
    finally:
        client.close()

    assert first == {"type": "content", "content": "first"}
    assert state.line_iterator is not None and state.line_iterator.closed
    assert state.response_exited and state.client_exited


def test_http_error_propagates_after_resources_close(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = StreamState(status_code=503)
    client = make_inference_client()
    install_fake_async_client(monkeypatch, state)

    try:
        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            consume_stream(client)
    finally:
        client.close()

    assert exc_info.value.response.status_code == 503
    assert state.line_iterator is None
    assert state.response_exited and state.client_exited


def test_stream_with_no_content_still_closes_resources(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = StreamState(
        lines=[
            'data: {"type":"status","status":"complete"}',
            "data: [DONE]",
        ]
    )
    client = make_inference_client()
    install_fake_async_client(monkeypatch, state)

    try:
        chunks = consume_stream(client)
    finally:
        client.close()

    assert chunks == [{"type": "status", "status": "complete"}]
    assert state.line_iterator is not None and state.line_iterator.closed
    assert state.response_exited and state.client_exited


class TrackingInferenceClient:
    def __init__(self, *, error: Optional[Exception] = None) -> None:
        self.error = error
        self.closed = False

    async def stream_inference_response(self, **_kwargs: Any):
        try:
            yield {"type": "content", "content": "first"}
            if self.error:
                raise self.error
            yield {"type": "content", "content": "second"}
        finally:
            self.closed = True


def make_sync_stream(inference: TrackingInferenceClient) -> SynchronousInferenceStream:
    stream = SynchronousInferenceStream(inference)
    stream.setup(
        thread_id="thread_test",
        assistant_id="asst_test",
        message_id="message_test",
        run_id="run_test",
    )
    return stream


def test_sync_wrapper_closes_async_stream_on_early_exit() -> None:
    inference = TrackingInferenceClient()
    chunks = make_sync_stream(inference).stream_chunks(
        model=VALID_STREAM_REQUEST["model"]
    )

    assert next(chunks)["content"] == "first"
    chunks.close()

    assert inference.closed


def test_sync_wrapper_propagates_stream_error_after_cleanup() -> None:
    failure = httpx.ReadError("stream disconnected")
    inference = TrackingInferenceClient(error=failure)
    chunks = make_sync_stream(inference).stream_chunks(
        model=VALID_STREAM_REQUEST["model"]
    )

    assert next(chunks)["content"] == "first"
    with pytest.raises(httpx.ReadError, match="stream disconnected"):
        next(chunks)

    assert inference.closed
