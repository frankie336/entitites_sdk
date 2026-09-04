import os
from typing import Any, Dict, Optional

import httpx
from projectdavid_common import UtilsInterface
from projectdavid_common.schemas.deployment_schemas import (
    ActivateBaseModelRequest,
    ActivateFineTunedModelRequest,
    DeactivateAllResponse,
    DeploymentActivationResponse,
    DeploymentDeactivationResponse,
    DeploymentListResponse,
)

from projectdavid.clients.base_client import BaseAPIClient

logging_utility = UtilsInterface.LoggingUtility()


class DeploymentsClient(BaseAPIClient):
    """
    Client for inference deployment lifecycle management.

    Handles activation, updating, listing, and stateful deactivation of base
    models and fine-tuned models on the Project David sovereign AI cluster.

    Activation is asynchronous. The server creates a pending
    InferenceDeployment record and returns immediately. The
    InferenceReconciler submits the corresponding Ray Serve application and
    promotes the deployment to active only after Ray reports the application
    RUNNING.

    Deactivation is also asynchronous. A running or pending deployment first
    transitions to cancelling. The InferenceReconciler removes the Ray Serve
    application, confirms runtime teardown and GPU release, and only then marks
    the deployment cancelled.

    All operations require admin privileges.

    Usage::

        client = Entity(api_key="...")

        # Activate a base model with custom hyperparams
        result = client.deployments.activate_base(
            base_model_id="OpenGVLab/InternVL2-4B",
            gpu_memory_utilization=0.95,
            max_model_len=8192,
            limit_mm_per_prompt={"image": 2},
            mm_processor_kwargs={"min_pixels": 784, "max_pixels": 50176},
        )

        # Activate a fine-tuned model
        result = client.deployments.activate_fine_tuned(
            model_id="ftm_G05BERHAEvSRr2KTyUqWIJ",
            gpu_memory_utilization=0.90,
        )

        # Patch a tracked deployment without reactivating it
        client.deployments.update(
            deployment_id="dep_abc123",
            max_model_len=4096,
            enforce_eager=True,
            mm_processor_kwargs={"min_pixels": 784, "max_pixels": 200704},
        )

        # List tracked deployments and inspect lifecycle status
        deployments = client.deployments.list()

        # Request stateful deactivation of a base model
        result = client.deployments.deactivate_base(
            "OpenGVLab/InternVL2-4B"
        )

        # Request stateful teardown of all local deployments
        result = client.deployments.deactivate_all()
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        training_url: Optional[str] = None,
    ):
        super().__init__(base_url=base_url, api_key=api_key)

        resolved_url = (
            training_url
            or os.getenv("TRAINING_BASE_URL")
            or base_url
            or "http://localhost:80"
        )
        self.training_url = resolved_url.rstrip("/")

    # -------------------------------------------------------------------------
    # Runtime capabilities
    # -------------------------------------------------------------------------

    def runtime_capabilities(self) -> Dict[str, Any]:
        """
        Return the authoritative inference-runtime capability snapshot.

        The server captures this information inside the Project David
        inference-worker environment used by Ray Serve/vLLM. It therefore
        describes the inference runtime rather than the SDK or API process.

        Returns:
            Raw runtime capability payload reported by Project David Core.

        Raises:
            httpx.HTTPStatusError:
                If the Core endpoint rejects the request or is unavailable.
            ValueError:
                If Core returns a non-object JSON payload.
        """
        logging_utility.debug(
            "DeploymentsClient: requesting inference runtime capabilities"
        )

        response = self.client.get(
            f"{self.training_url}/v1/deployments/runtime-capabilities"
        )
        response.raise_for_status()

        payload = response.json()

        if not isinstance(payload, dict):
            raise ValueError(
                "Project David runtime capability response must be an object."
            )

        return payload

    # -------------------------------------------------------------------------
    # Activation
    # -------------------------------------------------------------------------

    def activate_base(
        self,
        base_model_id: str,
        target_node_id: Optional[str] = None,
        tensor_parallel_size: int = 1,
        # --- vLLM engine hyperparam overrides ---
        # All optional. None = server falls back to VLLM_DEFAULT_* env vars
        # or built-in safe defaults in inference_worker.py.
        gpu_memory_utilization: Optional[float] = None,
        max_model_len: Optional[int] = None,
        max_num_seqs: Optional[int] = None,
        quantization: Optional[str] = None,
        dtype: Optional[str] = None,
        enforce_eager: Optional[bool] = None,
        limit_mm_per_prompt: Optional[Dict[str, int]] = None,
        mm_processor_kwargs: Optional[Dict[str, Any]] = None,
    ) -> DeploymentActivationResponse:
        """
        Schedule a base model (no LoRA adapter) for inference deployment.

        Accepts either a ``bm_...`` prefixed catalog ID or a raw HuggingFace
        model path. The server resolves HF paths to catalog IDs automatically.

        Activation is asynchronous. A successful response means the deployment
        has been accepted into the lifecycle, normally with status ``pending``.
        The deployment becomes ``active`` only after Project David confirms the
        Ray Serve application is RUNNING.

        Activation may be rejected while another local deployment is pending,
        active, or cancelling.

        All vLLM hyperparam args are optional. Omit them to use the node-level
        env var defaults. Set them to tune this specific deployment without
        touching compose files or rebuilding images.

        Args:
            base_model_id:           ``bm_...`` ID or HF path.
            target_node_id:          Optional. Pin to a specific Ray node ID.
            tensor_parallel_size:    Number of GPUs to shard across. Default 1.
            gpu_memory_utilization:  VRAM fraction [0.10-0.95]. None = env default.
            max_model_len:           Max sequence length in tokens. None = env default.
            max_num_seqs:            Max concurrent sequences. None = vLLM default.
            quantization:            e.g. 'awq_marlin', 'gptq'. None = full precision.
            dtype:                   e.g. 'float16', 'bfloat16'. None = float16.
            enforce_eager:           Disable CUDA graphs. None = False.
            limit_mm_per_prompt:     e.g. {'image': 2}. None = family registry default.
            mm_processor_kwargs:     Processor-level resolution caps.
                                     None = family registry default.
                                     Qwen2.5-VL:
                                     {'min_pixels': 784, 'max_pixels': 50176}
                                     Phi-3.5-Vision:
                                     {'num_crops': 4}

        Returns:
            DeploymentActivationResponse containing the accepted deployment
            lifecycle status and deployment metadata.
        """
        logging_utility.info(
            "DeploymentsClient: activating base model: %s", base_model_id
        )
        payload = ActivateBaseModelRequest(
            base_model_id=base_model_id,
            target_node_id=target_node_id,
            tensor_parallel_size=tensor_parallel_size,
            gpu_memory_utilization=gpu_memory_utilization,
            max_model_len=max_model_len,
            max_num_seqs=max_num_seqs,
            quantization=quantization,
            dtype=dtype,
            enforce_eager=enforce_eager,
            limit_mm_per_prompt=limit_mm_per_prompt,
            mm_processor_kwargs=mm_processor_kwargs,
        ).model_dump(exclude_none=True)

        try:
            response = self.client.post(
                f"{self.training_url}/v1/deployments/base",
                json=payload,
            )
            response.raise_for_status()
            return DeploymentActivationResponse.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP %d activating base model %s: %s",
                e.response.status_code,
                base_model_id,
                e.response.text,
            )
            raise

    def activate_fine_tuned(
        self,
        model_id: str,
        target_node_id: Optional[str] = None,
        tensor_parallel_size: int = 1,
        # --- vLLM engine hyperparam overrides ---
        gpu_memory_utilization: Optional[float] = None,
        max_model_len: Optional[int] = None,
        max_num_seqs: Optional[int] = None,
        quantization: Optional[str] = None,
        dtype: Optional[str] = None,
        enforce_eager: Optional[bool] = None,
        limit_mm_per_prompt: Optional[Dict[str, int]] = None,
        mm_processor_kwargs: Optional[Dict[str, Any]] = None,
    ) -> DeploymentActivationResponse:
        """
        Schedule a fine-tuned model (base + LoRA adapter) for deployment.

        Activation is asynchronous. A successful response means the deployment
        has entered the lifecycle, normally as ``pending``. It becomes
        ``active`` only after the reconciler confirms Ray Serve is RUNNING.

        Activation may be rejected while another local deployment is pending,
        active, or cancelling.

        All vLLM hyperparam args are optional. Omit them to use the node-level
        env var defaults.

        Args:
            model_id:                ``ftm_...`` prefixed ID.
            target_node_id:          Optional. Pin to a specific Ray node ID.
            tensor_parallel_size:    Number of GPUs to shard across. Default 1.
            gpu_memory_utilization:  VRAM fraction [0.10-0.95]. None = env default.
            max_model_len:           Max sequence length in tokens. None = env default.
            max_num_seqs:            Max concurrent sequences. None = vLLM default.
            quantization:            e.g. 'awq_marlin', 'gptq'. None = full precision.
            dtype:                   e.g. 'float16', 'bfloat16'. None = float16.
            enforce_eager:           Disable CUDA graphs. None = False.
            limit_mm_per_prompt:     e.g. {'image': 2}. None = family registry default.
            mm_processor_kwargs:     Processor-level resolution caps.
                                     None = family registry default.

        Returns:
            DeploymentActivationResponse containing the accepted deployment
            lifecycle status and deployment metadata.
        """
        logging_utility.info(
            "DeploymentsClient: activating fine-tuned model: %s", model_id
        )
        payload = ActivateFineTunedModelRequest(
            model_id=model_id,
            target_node_id=target_node_id,
            tensor_parallel_size=tensor_parallel_size,
            gpu_memory_utilization=gpu_memory_utilization,
            max_model_len=max_model_len,
            max_num_seqs=max_num_seqs,
            quantization=quantization,
            dtype=dtype,
            enforce_eager=enforce_eager,
            limit_mm_per_prompt=limit_mm_per_prompt,
            mm_processor_kwargs=mm_processor_kwargs,
        ).model_dump(exclude_none=True)

        try:
            response = self.client.post(
                f"{self.training_url}/v1/deployments/fine-tuned",
                json=payload,
            )
            response.raise_for_status()
            return DeploymentActivationResponse.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP %d activating fine-tuned model %s: %s",
                e.response.status_code,
                model_id,
                e.response.text,
            )
            raise

    # -------------------------------------------------------------------------
    # Update (partial patch)
    # -------------------------------------------------------------------------

    def update(
        self,
        deployment_id: str,
        gpu_memory_utilization: Optional[float] = None,
        max_model_len: Optional[int] = None,
        max_num_seqs: Optional[int] = None,
        quantization: Optional[str] = None,
        dtype: Optional[str] = None,
        enforce_eager: Optional[bool] = None,
        limit_mm_per_prompt: Optional[Dict[str, int]] = None,
        mm_processor_kwargs: Optional[Dict[str, Any]] = None,
        tensor_parallel_size: Optional[int] = None,
    ) -> dict:
        """
        Partially update vLLM engine hyperparams for a tracked deployment.

        Only fields explicitly provided are sent to the server. Omitted fields
        retain their current DB values. Changes are picked up by the
        InferenceReconciler on its next poll cycle.

        Use this to tune a tracked deployment without reactivating it::

            client.deployments.update(
                deployment_id="dep_abc123",
                max_model_len=8192,
                gpu_memory_utilization=0.95,
                mm_processor_kwargs={
                    "min_pixels": 784,
                    "max_pixels": 200704,
                },
            )

        Args:
            deployment_id:           ``dep_...`` ID of the deployment to patch.
            gpu_memory_utilization:  New VRAM fraction [0.10-0.95].
            max_model_len:           New max sequence length in tokens.
            max_num_seqs:            New max concurrent sequences.
            quantization:            New quantization scheme.
            dtype:                   New compute dtype.
            enforce_eager:           Enable/disable CUDA graphs.
            limit_mm_per_prompt:     New per-modality token cap.
            mm_processor_kwargs:     New processor-level resolution caps.
            tensor_parallel_size:    New GPU shard count.

        Returns:
            dict with status, deployment_id, and updated_fields.
        """
        logging_utility.info(
            "DeploymentsClient: patching deployment: %s", deployment_id
        )

        payload = {
            k: v
            for k, v in {
                "gpu_memory_utilization": gpu_memory_utilization,
                "max_model_len": max_model_len,
                "max_num_seqs": max_num_seqs,
                "quantization": quantization,
                "dtype": dtype,
                "enforce_eager": enforce_eager,
                "limit_mm_per_prompt": limit_mm_per_prompt,
                "mm_processor_kwargs": mm_processor_kwargs,
                "tensor_parallel_size": tensor_parallel_size,
            }.items()
            if v is not None
        }

        try:
            response = self.client.patch(
                f"{self.training_url}/v1/deployments/{deployment_id}",
                json=payload,
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP %d patching deployment %s: %s",
                e.response.status_code,
                deployment_id,
                e.response.text,
            )
            raise

    # -------------------------------------------------------------------------
    # Listing
    # -------------------------------------------------------------------------

    def list(self) -> DeploymentListResponse:
        """
        Return all InferenceDeployment records tracked by Project David.

        Results may include lifecycle states such as ``pending``, ``active``,
        ``cancelling``, ``cancelled``, and ``failed``.

        Returns:
            DeploymentListResponse containing items and total count.
        """
        logging_utility.info("DeploymentsClient: listing tracked deployments")
        try:
            response = self.client.get(
                f"{self.training_url}/v1/deployments/",
            )
            response.raise_for_status()
            return DeploymentListResponse.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP %d listing deployments: %s",
                e.response.status_code,
                e.response.text,
            )
            raise

    # -------------------------------------------------------------------------
    # Deactivation
    # -------------------------------------------------------------------------

    def deactivate_base(
        self,
        base_model_id: str,
    ) -> DeploymentDeactivationResponse:
        """
        Request stateful deactivation of a base-model deployment.

        Accepts either a ``bm_...`` prefixed catalog ID or a raw HuggingFace
        model path.

        Matching pending or active deployments transition to ``cancelling``.
        Project David removes the corresponding Ray Serve application and marks
        the deployment ``cancelled`` only after runtime teardown and GPU release
        are confirmed.

        If no matching runtime requires teardown, the server may return
        ``cancelled`` immediately.

        Args:
            base_model_id: ``bm_...`` ID or HF path of the base model.

        Returns:
            DeploymentDeactivationResponse containing the current lifecycle
            status, typically ``cancelling`` or ``cancelled``.
        """
        logging_utility.info(
            "DeploymentsClient: requesting base model deactivation: %s",
            base_model_id,
        )
        try:
            response = self.client.delete(
                f"{self.training_url}/v1/deployments/base/{base_model_id}",
            )
            response.raise_for_status()
            return DeploymentDeactivationResponse.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP %d deactivating base model %s: %s",
                e.response.status_code,
                base_model_id,
                e.response.text,
            )
            raise

    def deactivate_fine_tuned(
        self,
        model_id: str,
    ) -> DeploymentDeactivationResponse:
        """
        Request stateful deactivation of a fine-tuned deployment.

        Matching pending or active deployments transition to ``cancelling``.
        Project David removes the corresponding Ray Serve application and marks
        the deployment ``cancelled`` only after runtime teardown and GPU release
        are confirmed.

        If no matching runtime requires teardown, the server may return
        ``cancelled`` immediately.

        Args:
            model_id: ``ftm_...`` prefixed fine-tuned model ID.

        Returns:
            DeploymentDeactivationResponse containing the current lifecycle
            status, typically ``cancelling`` or ``cancelled``.
        """
        logging_utility.info(
            "DeploymentsClient: requesting fine-tuned model deactivation: %s",
            model_id,
        )
        try:
            response = self.client.delete(
                f"{self.training_url}/v1/deployments/fine-tuned/{model_id}",
            )
            response.raise_for_status()
            return DeploymentDeactivationResponse.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP %d deactivating fine-tuned model %s: %s",
                e.response.status_code,
                model_id,
                e.response.text,
            )
            raise

    def deactivate_all(self) -> DeactivateAllResponse:
        """
        Request stateful teardown of all local inference deployments.

        Project David preserves deployment records while matching pending or
        active deployments transition to ``cancelling``. The
        InferenceReconciler removes their Ray Serve applications, confirms
        runtime teardown and GPU release, and only then settles each deployment
        as ``cancelled``.

        If no deployment currently requires teardown, the server may return
        ``cancelled`` immediately.

        Returns:
            DeactivateAllResponse containing the current lifecycle status and
            server message.
        """
        logging_utility.warning(
            "DeploymentsClient: requesting deactivation of all deployments"
        )
        try:
            response = self.client.delete(
                f"{self.training_url}/v1/deployments/",
            )
            response.raise_for_status()
            return DeactivateAllResponse.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            logging_utility.error(
                "HTTP %d on deactivate-all: %s",
                e.response.status_code,
                e.response.text,
            )
            raise
