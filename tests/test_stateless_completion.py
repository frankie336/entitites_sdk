import inspect
import json

import httpx

from projectdavid.clients.inference_client import InferenceClient


def _client(handler):
    client = InferenceClient(
        base_url="https://project-david.test",
        api_key="pd-key",
    )
    client.client.close()
    client.client = httpx.Client(
        base_url=client.base_url,
        headers={"X-API-Key": client.api_key},
        transport=httpx.MockTransport(handler),
    )
    return client


def test_stateless_helper_uses_existing_completion_endpoint_and_flag():
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "object": "text_completion",
                "model": "vllm/bm_example",
                "choices": [{"index": 0, "text": "BGP Route Reflectors"}],
            },
        )

    with _client(handler) as client:
        client.create_stateless_completion(
            model="vllm/bm_example",
            prompt="Name this conversation",
            max_tokens=24,
            temperature=0.2,
        )

    assert len(requests) == 1
    assert requests[0].method == "POST"
    assert requests[0].url.path == "/v1/completions"
    payload = json.loads(requests[0].content)
    assert payload["stateless"] is True
    assert payload["stream"] is False


def test_stateless_helper_sends_no_conversation_identifiers():
    captured = {}

    def handler(request):
        captured.update(json.loads(request.content))
        return httpx.Response(
            200,
            json={"choices": [{"text": "Durable Conversation Titles"}]},
        )

    with _client(handler) as client:
        client.create_stateless_completion(
            model="together-ai/example/model",
            messages=[{"role": "user", "content": "Name this"}],
            provider_api_key="provider-key",
        )

    assert not {
        "thread_id",
        "message_id",
        "run_id",
        "assistant_id",
    }.intersection(captured)
    assert captured["messages"] == [{"role": "user", "content": "Name this"}]
    assert captured["api_key"] == "provider-key"


def test_stateless_helper_returns_normal_completion_response():
    response_payload = {
        "object": "text_completion",
        "model": "vllm/bm_example",
        "choices": [
            {"index": 0, "text": "Project David Lifecycle", "finish_reason": "stop"}
        ],
    }

    def handler(request):
        return httpx.Response(200, json=response_payload)

    with _client(handler) as client:
        result = client.create_stateless_completion(
            model="vllm/bm_example",
            prompt="Name this conversation",
        )

    assert result == response_payload
    assert result["choices"][0]["text"] == "Project David Lifecycle"


def test_stateless_helper_requires_prompt_or_messages_but_not_both():
    client = InferenceClient(base_url="https://project-david.test", api_key="pd-key")
    try:
        for kwargs in ({}, {"prompt": "one", "messages": []}):
            try:
                client.create_stateless_completion(
                    model="vllm/bm_example",
                    **kwargs,
                )
            except ValueError as exc:
                assert "exactly one" in str(exc)
            else:
                raise AssertionError("invalid input shape was accepted")
    finally:
        client.close()


def test_existing_inference_method_signatures_remain_available():
    assert "kwargs" in inspect.signature(InferenceClient.create_completion).parameters
    assert (
        "kwargs" in inspect.signature(InferenceClient.create_completion_sync).parameters
    )
    assert hasattr(InferenceClient, "stream_inference_response")
