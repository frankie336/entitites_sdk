from types import SimpleNamespace

import projectdavid.clients.registry_client as registry_module
from projectdavid.clients.registry_client import RegistryClient


class FakeResponse:
    def raise_for_status(self):
        return None

    def json(self):
        return {
            "id": "bm_local",
            "endpoint": (
                "/opt/projectdavid/model-hub/models/" "model-a/variant-a/revision-a"
            ),
        }


class FakeHttpClient:
    def __init__(self):
        self.calls = []

    def post(self, url, *, json):
        self.calls.append(
            {
                "url": url,
                "json": json,
            }
        )

        return FakeResponse()


class FakeBaseModelRead:
    @classmethod
    def model_validate(cls, value):
        return value


def test_register_local_uses_dedicated_local_registry_route():
    client = RegistryClient.__new__(RegistryClient)

    client.training_url = "http://project-david"

    client.client = FakeHttpClient()

    original_validator = registry_module.validator

    registry_module.validator = SimpleNamespace(
        BaseModelRead=FakeBaseModelRead,
    )

    try:
        result = client.register_local(
            model_endpoint=(
                "/opt/projectdavid/model-hub/models/" "model-a/variant-a/revision-a"
            ),
            name="Model A",
            family="test",
        )
    finally:
        registry_module.validator = original_validator

    assert result["id"] == "bm_local"

    assert client.client.calls == [
        {
            "url": ("http://project-david" "/v1/registry/base-models/local"),
            "json": {
                "model_endpoint": (
                    "/opt/projectdavid/model-hub/models/" "model-a/variant-a/revision-a"
                ),
                "name": "Model A",
                "family": "test",
                "is_multimodal": False,
            },
        }
    ]
