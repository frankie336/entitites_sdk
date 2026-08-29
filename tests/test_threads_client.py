import json

import httpx
from projectdavid_common import ValidationInterface

from projectdavid.clients.threads_client import ThreadsClient

validator = ValidationInterface()


def _thread_payload(thread_id: str, *, title: str | None = None):
    q_metadata = {"title": title} if title else {}
    return {
        "id": thread_id,
        "created_at": 123,
        "meta_data": {"q": q_metadata},
        "object": "thread",
        "tool_resources": {},
        "owner_id": "user_1",
    }


def _client(handler):
    client = ThreadsClient(base_url="https://project-david.test", api_key="pd-key")
    client.client.close()
    client.client = httpx.Client(
        base_url=client.base_url,
        headers={"X-API-Key": client.api_key},
        transport=httpx.MockTransport(handler),
    )
    return client


def test_list_threads_keeps_id_only_contract():
    def handler(request):
        assert request.url.path == "/v1/threads/user/user_1"
        return httpx.Response(200, json=["thread_1", "thread_2"])

    with _client(handler) as client:
        result = client.list_threads("user_1")

    assert result == ["thread_1", "thread_2"]
    assert all(isinstance(thread_id, str) for thread_id in result)


def test_list_thread_records_uses_records_endpoint():
    def handler(request):
        assert request.url.path == "/v1/threads/user/user_1/records"
        return httpx.Response(200, json=[_thread_payload("thread_1")])

    with _client(handler) as client:
        result = client.list_thread_records("user_1")

    assert [record.id for record in result] == ["thread_1"]


def test_list_thread_records_validates_thread_read_models():
    def handler(request):
        return httpx.Response(
            200,
            json=[_thread_payload("thread_1", title="Project David Lifecycle")],
        )

    with _client(handler) as client:
        result = client.list_thread_records("user_1")

    assert type(result[0]) is validator.ThreadRead
    assert result[0].meta_data["q"]["title"] == "Project David Lifecycle"


def test_update_thread_metadata_uses_dedicated_metadata_route():
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(
            200,
            json=_thread_payload("thread_1", title="Durable title"),
        )

    with _client(handler) as client:
        client.update_thread_metadata(
            "thread_1",
            {"q": {"title": "Durable title"}},
        )

    assert len(requests) == 1
    assert requests[0].method == "PUT"
    assert requests[0].url.path == "/v1/threads/thread_1/metadata"
    assert json.loads(requests[0].content) == {"q": {"title": "Durable title"}}


def test_update_thread_metadata_preserves_thread_read_return_model():
    def handler(request):
        return httpx.Response(
            200,
            json=_thread_payload("thread_1", title="Durable title"),
        )

    with _client(handler) as client:
        result = client.update_thread_metadata(
            "thread_1",
            {"q": {"title": "Durable title"}},
        )

    assert type(result) is validator.ThreadRead
    assert result.id == "thread_1"
    assert result.meta_data["q"]["title"] == "Durable title"
