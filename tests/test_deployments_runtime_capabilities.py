from __future__ import annotations

from unittest.mock import Mock, patch

import pytest

from projectdavid.clients.deployments_client import DeploymentsClient


def _client() -> DeploymentsClient:
    return DeploymentsClient(
        base_url="https://example.test",
        api_key="test-key",
    )


def test_runtime_capabilities_uses_canonical_route():
    sdk = _client()

    payload = {
        "schema_version": 1,
        "project_david_version": "1.47.1",
        "backend": {
            "id": "vllm",
            "version": "0.10.1",
        },
        "runtime": {
            "accelerator_api": "cuda",
            "cuda_runtime_version": None,
            "rocm_runtime_version": None,
        },
        "frameworks": {
            "torch": {
                "version": "2.7.1+cu128",
                "cuda_version": "12.8",
                "cudnn_version": "91002",
            }
        },
        "visible_accelerators": [],
    }

    response = Mock()
    response.json.return_value = payload

    with patch.object(
        sdk.client,
        "get",
        return_value=response,
    ) as request:
        result = sdk.runtime_capabilities()

    assert result == payload

    request.assert_called_once_with(
        "https://example.test/v1/deployments/runtime-capabilities"
    )
    response.raise_for_status.assert_called_once_with()


def test_runtime_capabilities_propagates_http_failure():
    sdk = _client()

    response = Mock()
    response.raise_for_status.side_effect = RuntimeError("runtime unavailable")

    with patch.object(
        sdk.client,
        "get",
        return_value=response,
    ):
        with pytest.raises(
            RuntimeError,
            match="runtime unavailable",
        ):
            sdk.runtime_capabilities()


def test_runtime_capabilities_rejects_non_object_payload():
    sdk = _client()

    response = Mock()
    response.json.return_value = [
        "invalid",
        "payload",
    ]

    with patch.object(
        sdk.client,
        "get",
        return_value=response,
    ):
        with pytest.raises(
            ValueError,
            match="must be an object",
        ):
            sdk.runtime_capabilities()
