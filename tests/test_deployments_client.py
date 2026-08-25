from unittest.mock import MagicMock

from projectdavid_common.schemas.deployment_schemas import (
    DeactivateAllResponse,
    DeploymentDeactivationResponse,
)

from projectdavid.clients.deployments_client import DeploymentsClient


def _make_client():
    client = DeploymentsClient.__new__(DeploymentsClient)
    client.training_url = "http://project-david.test"
    client.client = MagicMock()
    return client


def _mock_response(client, payload):
    response = MagicMock()
    response.json.return_value = payload
    response.raise_for_status.return_value = None
    client.client.delete.return_value = response
    return response


def test_deactivate_base_preserves_cancelling_status():
    client = _make_client()

    _mock_response(
        client,
        {
            "status": "cancelling",
            "base_model_id": "bm_test",
        },
    )

    result = client.deactivate_base("Qwen/Test-Model")

    assert isinstance(result, DeploymentDeactivationResponse)
    assert result.status == "cancelling"
    assert result.base_model_id == "bm_test"

    client.client.delete.assert_called_once_with(
        "http://project-david.test/v1/deployments/base/Qwen/Test-Model"
    )


def test_deactivate_base_preserves_cancelled_status():
    client = _make_client()

    _mock_response(
        client,
        {
            "status": "cancelled",
            "base_model_id": "bm_test",
        },
    )

    result = client.deactivate_base("bm_test")

    assert isinstance(result, DeploymentDeactivationResponse)
    assert result.status == "cancelled"
    assert result.base_model_id == "bm_test"


def test_deactivate_fine_tuned_preserves_cancelling_status():
    client = _make_client()

    _mock_response(
        client,
        {
            "status": "cancelling",
            "model_id": "ftm_test",
        },
    )

    result = client.deactivate_fine_tuned("ftm_test")

    assert isinstance(result, DeploymentDeactivationResponse)
    assert result.status == "cancelling"
    assert result.model_id == "ftm_test"

    client.client.delete.assert_called_once_with(
        "http://project-david.test/v1/deployments/fine-tuned/ftm_test"
    )


def test_deactivate_all_preserves_stateful_lifecycle_status():
    client = _make_client()

    _mock_response(
        client,
        {
            "status": "cancelling",
            "message": "All local deployments are being removed from Ray Serve.",
        },
    )

    result = client.deactivate_all()

    assert isinstance(result, DeactivateAllResponse)
    assert result.status == "cancelling"
    assert result.message == ("All local deployments are being removed from Ray Serve.")

    client.client.delete.assert_called_once_with(
        "http://project-david.test/v1/deployments/"
    )
