import asyncio
import json
import re
from contextlib import suppress
from typing import Any, Dict, Generator, Optional, Union

import nest_asyncio
from projectdavid_common import ToolValidator, UtilsInterface

from projectdavid.events import (
    CodeExecutionGeneratedFileEvent,
    CodeExecutionOutputEvent,
    CodeStatusEvent,
    ComputerExecutionOutputEvent,
    ComputerGeneratedFileEvent,
    ContentEvent,
    DecisionEvent,
    EngineerStatusEvent,
    HotCodeEvent,
    PlanEvent,
    ReasoningEvent,
    ResearchStatusEvent,
    ScratchpadEvent,
    ShellStatusEvent,
    StreamEvent,
    ToolCallRequestEvent,
    ToolInterceptEvent,
    WebStatusEvent,
)

LOG = UtilsInterface.LoggingUtility()


class SynchronousInferenceStream:
    """
    A per-request inference stream.

    IMPORTANT — Thread Safety:
    --------------------------
    This class must be instantiated fresh for every request. It must NOT be
    stored as a shared singleton on the client (e.g. as a cached property).
    Sharing an instance across concurrent requests causes .setup() to race-
    overwrite thread_id, run_id, and other fields mid-stream.

    Correct usage in Flask route:
        sync_stream = SynchronousInferenceStream.for_request(
            inference=client.inference,
            runs_client=client.runs,
            actions_client=client.actions,
            messages_client=client.messages,
            assistants_client=client.assistants,
        )
        sync_stream.setup(thread_id=..., assistant_id=..., message_id=...,
                          run_id=..., api_key=..., meta_data=...)
        for event in sync_stream.stream_events(model=...):
            ...
    """

    def __init__(self, inference) -> None:
        self.inference_client = inference
        self.user_id: Optional[str] = None
        self.thread_id: Optional[str] = None
        self.assistant_id: Optional[str] = None
        self.message_id: Optional[str] = None
        self.run_id: Optional[str] = None
        self.api_key: Optional[str] = None
        self.meta_data: Optional[Dict[str, Any]] = None

        self.runs_client: Any | None = None
        self.actions_client: Any | None = None
        self.messages_client: Any | None = None
        self.assistants_client: Any | None = None

        self.validator = ToolValidator()

    # ── Factory ────────────────────────────────────────────────────────────────

    @classmethod
    def for_request(
        cls,
        inference: Any,
        runs_client: Any,
        actions_client: Any,
        messages_client: Any,
        assistants_client: Any,
    ) -> "SynchronousInferenceStream":
        instance = cls(inference)
        instance.bind_clients(
            runs_client=runs_client,
            actions_client=actions_client,
            messages_client=messages_client,
            assistants_client=assistants_client,
        )
        return instance

    def setup(
        self,
        thread_id: str,
        assistant_id: str,
        message_id: str,
        run_id: str,
        api_key: Optional[str] = None,
        meta_data: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.thread_id = thread_id
        self.assistant_id = assistant_id
        self.message_id = message_id
        self.run_id = run_id
        self.api_key = api_key
        self.meta_data = meta_data

    def bind_clients(
        self,
        runs_client: Any,
        actions_client: Any,
        messages_client: Any,
        assistants_client: Any,
    ) -> None:
        self.runs_client = runs_client
        self.actions_client = actions_client
        self.messages_client = messages_client
        self.assistants_client = assistants_client

    # ── Raw chunk streaming ────────────────────────────────────────────────────

    def stream_chunks(
        self,
        model: str,
        *,
        api_key: Optional[str] = None,
        meta_data: Optional[Dict[str, Any]] = None,
        timeout_per_chunk: float = 600.0,
        suppress_fc: bool = True,
    ) -> Generator[dict, None, None]:
        resolved_api_key = api_key or self.api_key
        resolved_meta_data = meta_data or self.meta_data

        thread_id = self.thread_id
        message_id = self.message_id
        run_id = self.run_id
        assistant_id = self.assistant_id

        agen = self.inference_client.stream_inference_response(
            model=model,
            api_key=resolved_api_key,
            thread_id=thread_id,
            message_id=message_id,
            run_id=run_id,
            assistant_id=assistant_id,
            meta_data=resolved_meta_data,
            timeout=timeout_per_chunk,
        ).__aiter__()

        active_loop = None
        is_new_loop = False

        try:
            active_loop = asyncio.get_running_loop()
            nest_asyncio.apply(active_loop)
        except RuntimeError:
            active_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(active_loop)
            is_new_loop = True

        try:
            while True:
                try:
                    chunk = active_loop.run_until_complete(
                        asyncio.wait_for(agen.__anext__(), timeout=timeout_per_chunk)
                    )
                    chunk["run_id"] = run_id
                    if suppress_fc and chunk.get("type") == "call_arguments":
                        continue
                    yield chunk

                except StopAsyncIteration:
                    break
                except Exception as exc:
                    LOG.error(f"[SyncStream] Streaming error: {exc}", exc_info=True)
                    raise
        finally:
            try:
                if active_loop and not active_loop.is_closed():
                    active_loop.run_until_complete(agen.aclose())
            finally:
                if is_new_loop and active_loop and not active_loop.is_closed():
                    pending = asyncio.all_tasks(active_loop)
                    for task in pending:
                        task.cancel()
                    if pending:
                        active_loop.run_until_complete(
                            asyncio.gather(*pending, return_exceptions=True)
                        )
                    active_loop.run_until_complete(active_loop.shutdown_asyncgens())
                    active_loop.close()
                    asyncio.set_event_loop(None)

    # ── Event streaming ────────────────────────────────────────────────────────

    def stream_events(
        self,
        model: str,
        *,
        meta_data: Optional[Dict[str, Any]] = None,
        timeout_per_chunk: float = 280.0,
        max_turns: int = 10,
    ) -> Generator[Union[StreamEvent, Any], None, None]:

        if self.assistant_id and self.assistants_client:
            try:
                ast = self.assistants_client.retrieve_assistant(self.assistant_id)
                tools = (
                    getattr(ast, "tools", [])
                    if not isinstance(ast, dict)
                    else ast.get("tools", [])
                )
                self.validator.build_registry_from_assistant(tools)
            except Exception as e:
                LOG.warning(
                    f"[SyncStream] Failed to retrieve Assistant tool schemas: {e}"
                )

        turn_count = 0
        while turn_count < max_turns:
            turn_count += 1
            last_tool_call: Optional[ToolCallRequestEvent] = None
            validation_failed_this_turn = False

            for chunk in self.stream_chunks(
                model=model,
                meta_data=meta_data or self.meta_data,
                timeout_per_chunk=timeout_per_chunk,
                suppress_fc=True,
            ):
                event = self._map_chunk_to_event(chunk)
                if not event:
                    continue

                if isinstance(event, ToolCallRequestEvent):
                    error_msg = self.validator.validate_args(
                        event.tool_name, event.args
                    )
                    if error_msg:
                        LOG.warning(f"[SDK] Intercepted invalid tool call: {error_msg}")
                        self.messages_client.submit_tool_output(
                            thread_id=self.thread_id,
                            content=error_msg,
                            role="tool",
                            assistant_id=self.assistant_id,
                            tool_id=event.action_id,
                        )
                        event.executed = True
                        last_tool_call = event
                        validation_failed_this_turn = True
                        break

                yield event
                if isinstance(event, ToolCallRequestEvent):
                    last_tool_call = event

            if validation_failed_this_turn or (
                last_tool_call and last_tool_call.executed
            ):
                LOG.info(
                    f"[SyncStream] Self-Correction triggered. Turn {turn_count + 1}"
                )
                continue

            break

    # ── Chunk → Event mapping ──────────────────────────────────────────────────

    def _map_chunk_to_event(self, chunk: dict) -> Optional[StreamEvent]:
        """
        Maps raw API chunks to typed Event instances.

        Unwrap order
        ────────────
        1. Unwrap mixin JSON encoded inside a content chunk (legacy path).
           Shell mixin yields JSON strings; the inference transport wraps them
           in {"type":"content","content":"<json>"}.  Step 1 unwraps them when
           the embedded JSON contains "stream_type" or a recognised type key.

        2. Unwrap stream_type envelopes.
           Sets _from_shell_envelope=True when stream_type=="shell" so step 3
           can suppress PTY-text inner types that must NOT reach the SSE stream.

        3. Dispatch on c_type → typed Event | None.

        Shell envelope suppression
        ──────────────────────────
        The shell mixin wraps all PTY output as:
            {"stream_type": "shell", "chunk": {"type": "shell_output", ...}}
        and its final aggregated summary as:
            {"stream_type": "shell", "chunk": {"type": "content", ...}}

        After step 1+2 unwrap, these arrive with generic type names that
        collide with top-level event types:

            shell_output  → ComputerExecutionOutputEvent → Flask "computer_output"
                          → useChat codeOutput.output → code-interpreter panel  ❌
            content       → ContentEvent → Flask "content"
                          → useChat updateBot(text) → "pwd" in main chat        ❌

        xterm reads all PTY text directly from the sandbox WebSocket
        (CollapsibleXtermTerminal) so suppressing these from SSE is both
        correct and complete.  The only shell inner types that must survive are:
            computer_file  — file download attachments for the UI
            shell_status   — arrives bare (no envelope), routes normally
        """

        # ── 1. Unwrap mixin JSON embedded in a content chunk ──────────────────
        if chunk.get("type") == "content" and isinstance(chunk.get("content"), str):
            text = chunk["content"].strip()
            if text.startswith("{") and text.endswith("}"):
                with suppress(Exception):
                    parsed = json.loads(text)
                    if isinstance(parsed, dict):
                        if (
                            parsed.get("type")
                            in {
                                "web_status",
                                "research_status",
                                "scratchpad_status",
                                "code_status",
                                "shell_status",
                                "engineer_status",
                                "tool_intercept",
                                "status",
                                "error",
                            }
                            or "stream_type" in parsed
                        ):
                            chunk = parsed

        # ── 2. Unwrap stream_type envelopes ───────────────────────────────────
        _from_shell_envelope = False

        stream_type = chunk.get("type", chunk.get("stream_type"))
        if stream_type in {
            "code_execution",
            "computer_execution",
            "delegation",
            "shell",
        }:
            if stream_type == "shell":
                _from_shell_envelope = True
            payload = chunk.get("chunk", {})
            if isinstance(payload, dict):
                payload.setdefault("run_id", chunk.get("run_id"))
                chunk = payload

        c_type = chunk.get("type")
        run_id = chunk.get("run_id")

        # ── 3. Type dispatch ──────────────────────────────────────────────────

        if c_type == "tool_call_manifest":
            raw_args = chunk.get("args", {})
            if isinstance(raw_args, str):
                try:
                    match = re.search(r"(\{.*\}|\[.*\])", raw_args, re.DOTALL)
                    if match:
                        raw_args = json.loads(match.group(1))
                except Exception:
                    LOG.warning(f"[SDK] Stage 1 Healing failed for args: {raw_args}")

            return ToolCallRequestEvent(
                run_id=str(self.run_id or ""),
                tool_name=chunk.get("tool", "unknown_tool"),
                args=raw_args,
                action_id=chunk.get("action_id"),
                tool_call_id=chunk.get("tool_call_id"),
                thread_id=str(self.thread_id or ""),
                assistant_id=str(self.assistant_id or ""),
                _runs_client=self.runs_client,
                _actions_client=self.actions_client,
                _messages_client=self.messages_client,
            )

        elif c_type == "content":
            if _from_shell_envelope:
                # Shell mixin's final PTY summary. Suppressed — the LLM receives
                # this via submit_tool_output; xterm has it via WebSocket.
                LOG.debug("[SyncStream] Suppressing shell envelope 'content' chunk.")
                return None
            return ContentEvent(
                run_id=str(self.run_id or ""), content=chunk.get("content", "")
            )

        elif c_type == "reasoning":
            return ReasoningEvent(
                run_id=str(self.run_id or ""), content=chunk.get("content", "")
            )

        elif c_type == "decision":
            return DecisionEvent(
                run_id=str(self.run_id or ""), content=chunk.get("content", "")
            )

        elif c_type == "plan":
            return PlanEvent(
                run_id=str(self.run_id or ""), content=chunk.get("content", "")
            )

        elif c_type == "hot_code":
            return HotCodeEvent(
                run_id=str(self.run_id or ""), content=chunk.get("content", "")
            )

        elif c_type == "hot_code_output":
            return CodeExecutionOutputEvent(
                run_id=str(self.run_id or ""), content=chunk.get("content", "")
            )

        elif c_type == "scratchpad_status":
            return ScratchpadEvent(
                run_id=str(self.run_id or ""),
                operation=chunk.get("operation", "unknown"),
                state=chunk.get("state", "in_progress"),
                activity=chunk.get("activity"),
                tool=chunk.get("tool"),
                entry=chunk.get("entry"),
                content=chunk.get("content"),
                assistant_id=chunk.get("assistant_id"),
            )

        elif c_type in ("computer_output", "shell_output", "shell_error"):
            if _from_shell_envelope:
                # PTY text from the shell session, arriving via stream_type="shell"
                # envelope.  Suppressed — xterm receives these via WebSocket and
                # does not need a second copy via SSE.  Forwarding causes output
                # to appear in the code-interpreter execution panel.
                LOG.debug("[SyncStream] Suppressing shell envelope '%s' chunk.", c_type)
                return None
            # Bare computer_output (non-shell path) still routes normally.
            return ComputerExecutionOutputEvent(
                run_id=str(self.run_id or ""), content=chunk.get("content", "")
            )

        elif c_type == "code_status":
            return CodeStatusEvent(
                run_id=str(self.run_id or ""),
                activity=chunk.get("activity", ""),
                state=chunk.get("state", "in_progress"),
                tool=chunk.get("tool"),
            )

        elif c_type == "shell_status":
            # Always arrives bare (no stream_type wrapper) so
            # _from_shell_envelope is always False here — routes normally.
            return ShellStatusEvent(
                run_id=str(self.run_id or ""),
                activity=chunk.get("activity", ""),
                state=chunk.get("state", "in_progress"),
                tool=chunk.get("tool"),
            )

        elif c_type == "code_interpreter_file":
            return CodeExecutionGeneratedFileEvent(
                run_id=str(self.run_id or ""),
                filename=chunk.get("filename", "unknown"),
                file_id=str(chunk.get("file_id") or ""),
                base64_data=str(chunk.get("base64") or ""),
                mime_type=str(chunk.get("mime_type", "application/octet-stream")),
                url=str(chunk.get("url") or ""),
            )

        elif c_type == "computer_file":
            # The only shell inner type that MUST survive the envelope —
            # provides file download links rendered in the frontend.
            return ComputerGeneratedFileEvent(
                run_id=str(self.run_id or ""),
                filename=str(chunk.get("filename", "unknown")),
                file_id=str(chunk.get("file_id") or ""),
                mime_type=str(chunk.get("mime_type", "application/octet-stream")),
                url=str(chunk.get("url") or ""),
                base64_data=str(chunk.get("base64") or ""),
                context=str(chunk.get("context") or ""),
            )

        elif c_type == "research_status":
            return ResearchStatusEvent(
                run_id=str(self.run_id or ""),
                activity=str(chunk.get("activity", "")),
                state=str(chunk.get("state", "in_progress")),
                tool=str(chunk.get("tool") or ""),
            )

        elif c_type == "web_status":
            return WebStatusEvent(
                run_id=str(self.run_id or ""),
                status=str(chunk.get("status", "running")),
                tool=str(chunk.get("tool") or ""),
                message=str(chunk.get("message") or ""),
            )

        elif c_type == "engineer_status":
            return EngineerStatusEvent(
                run_id=str(self.run_id or ""),
                activity=str(chunk.get("activity") or chunk.get("message", "")),
                state=str(chunk.get("state") or chunk.get("status", "in_progress")),
                tool=str(chunk.get("tool") or ""),
            )

        elif c_type == "tool_intercept":
            return ToolInterceptEvent(
                run_id=str(self.run_id or ""),
                tool_name=str(chunk.get("tool_name", "")),
                args=dict(chunk.get("args", {})),
                action_id=str(chunk.get("action_id") or ""),
                origin=str(chunk.get("origin") or ""),
                thread_id=str(chunk.get("thread_id") or ""),
                tool_call_id=str(chunk.get("tool_call_id") or ""),
                origin_run_id=str(chunk.get("origin_run_id") or ""),
                origin_assistant_id=str(chunk.get("origin_assistant_id") or ""),
            )

        elif c_type == "error":
            return WebStatusEvent(
                run_id=str(self.run_id or ""),
                status="failed",
                tool=str(chunk.get("tool")),
                message=str(chunk.get("error") or chunk.get("message")),
            )

        return None
