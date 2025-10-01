import logging

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Union

__version__ = "0.1.22"

from .client import AsyncModelRedClient, ModelRedClient
from .config import DEFAULT_BASE_URL, load_settings
from .exceptions import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    ModelRedError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
    SubscriptionLimitError,
    ValidationError,
)
from .resources.assessments import (
    Assessment as _ResourceAssessment,
    AssessmentPriority as _ResourcePriority,
    AssessmentStatus as _ResourceStatus,
)
from .resources.models import Model as _ResourceModel
from .resources.probes import Probe as Probe, ProbeIndex as ProbesIndex

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
logger = logging.getLogger("modelred")
if not logger.handlers:
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(h)
logger.setLevel(logging.INFO)

# -----------------------------------------------------------------------------
# Constants / Enums
# -----------------------------------------------------------------------------
BASE_URL = DEFAULT_BASE_URL


class ModelProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    AZURE = "azure"
    HUGGINGFACE = "huggingface"
    REST = "rest"
    BEDROCK = "bedrock"
    SAGEMAKER = "sagemaker"
    GOOGLE = "google"


AssessmentStatus = _ResourceStatus
Priority = _ResourcePriority


# -----------------------------------------------------------------------------
# Data classes
# -----------------------------------------------------------------------------
@dataclass
class Model:
    id: str
    modelId: str
    provider: str
    modelName: Optional[str]
    displayName: str
    description: Optional[str]
    isActive: bool
    lastTested: Optional[datetime]
    testCount: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    createdByUser: Optional[Dict[str, Any]] = None


@dataclass
class Assessment:
    id: str
    modelId: str
    status: AssessmentStatus
    testTypes: List[str]
    priority: Priority
    progress: int = 0
    results: Optional[Dict[str, Any]] = None
    errorMessage: Optional[str] = None
    createdAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    estimatedDuration: Optional[int] = None
    detailedReport: Optional[Dict[str, Any]] = None


# -----------------------------------------------------------------------------
# Provider config helpers
# -----------------------------------------------------------------------------
class ProviderConfig:
    @staticmethod
    def openai(
        api_key: str,
        model_name: str = "gpt-3.5-turbo",
        organization: Optional[str] = None,
    ) -> Dict[str, Any]:
        cfg = {"api_key": api_key, "model_name": model_name}
        if organization:
            cfg["organization"] = organization
        return cfg

    @staticmethod
    def anthropic(
        api_key: str, model_name: str = "claude-3-sonnet-20240229"
    ) -> Dict[str, Any]:
        return {"api_key": api_key, "model_name": model_name}

    @staticmethod
    def azure(
        api_key: str,
        endpoint: str,
        deployment_name: str,
        api_version: str = "2024-06-01",
    ) -> Dict[str, Any]:
        return {
            "api_key": api_key,
            "endpoint": endpoint,
            "deployment_name": deployment_name,
            "api_version": api_version,
        }

    @staticmethod
    def huggingface(
        model_name: str,
        api_key: Optional[str] = None,
        use_inference_api: bool = True,
        endpoint_url: Optional[str] = None,
        task: str = "text-generation",
    ) -> Dict[str, Any]:
        cfg = {
            "model_name": model_name,
            "use_inference_api": use_inference_api,
            "task": task,
        }
        if api_key:
            cfg["api_key"] = api_key
        if endpoint_url:
            cfg["endpoint_url"] = endpoint_url
        return cfg

    @staticmethod
    def rest(
        uri: str,
        name: Optional[str] = None,
        key_env_var: str = "REST_API_KEY",
        api_key: Optional[str] = None,
        method: str = "POST",
        headers: Optional[Dict[str, str]] = None,
        req_template: str = "$INPUT",
        req_template_json_object: Optional[Dict[str, Any]] = None,
        response_json: bool = True,
        response_json_field: str = "text",
        request_timeout: int = 20,
        ratelimit_codes: Optional[List[int]] = None,
        skip_codes: Optional[List[int]] = None,
        verify_ssl: Union[bool, str] = True,
        proxies: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        cfg = {
            "uri": uri,
            "method": method,
            "headers": headers or {},
            "req_template": req_template,
            "response_json": response_json,
            "response_json_field": response_json_field,
            "request_timeout": request_timeout,
            "ratelimit_codes": ratelimit_codes or [429],
            "skip_codes": skip_codes or [],
            "verify_ssl": verify_ssl,
        }
        if name is not None:
            cfg["name"] = name
        if key_env_var != "REST_API_KEY":
            cfg["key_env_var"] = key_env_var
        if api_key is not None:
            cfg["api_key"] = api_key
        if req_template_json_object is not None:
            cfg["req_template_json_object"] = req_template_json_object
        if proxies is not None:
            cfg["proxies"] = proxies
        return cfg

    @staticmethod
    def bedrock(
        region: str,
        model_id: str,
        access_key_id: str,
        secret_access_key: str,
        session_token: Optional[str] = None,
        temperature: float = 0.0,
        max_tokens: int = 1024,
    ) -> Dict[str, Any]:
        cfg = {
            "region": region,
            "model_id": model_id,
            "access_key_id": access_key_id,
            "secret_access_key": secret_access_key,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if session_token:
            cfg["session_token"] = session_token
        return cfg

    @staticmethod
    def sagemaker(
        region: str,
        endpoint_name: str,
        access_key_id: str,
        secret_access_key: str,
        session_token: Optional[str] = None,
        content_type: str = "application/json",
        accept: str = "application/json",
        request_json_template: Optional[Dict[str, Any]] = None,
        request_text_template: Optional[str] = None,
        response_json_field: str = "generated_text",
        timeout_ms: int = 20000,
    ) -> Dict[str, Any]:
        cfg = {
            "region": region,
            "endpoint_name": endpoint_name,
            "access_key_id": access_key_id,
            "secret_access_key": secret_access_key,
            "content_type": content_type,
            "accept": accept,
            "response_json_field": response_json_field,
            "timeout_ms": timeout_ms,
        }
        if session_token:
            cfg["session_token"] = session_token
        if request_json_template is not None:
            cfg["request_json_template"] = request_json_template
        if request_text_template is not None:
            cfg["request_text_template"] = request_text_template
        return cfg

    @staticmethod
    def google(
        model_name: str,
        api_key: str,
        *,
        generation_config: Optional[Dict[str, Any]] = None,
        safety_settings: Optional[List[Dict[str, Any]]] = None,
        # legacy args kept for compatibility but ignored:
        project_id: Optional[str] = None,
        location: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Google Gemini (Developer API only).

        Required:
          - model_name (e.g., "gemini-2.5-flash")
          - api_key   (Google AI Studio / Developer API key)

        Optional:
          - generation_config: dict
          - safety_settings:  list[dict]

        Notes:
          - Vertex/ADC params (project_id, location) are ignored.
        """
        if not api_key:
            raise ValidationError("Google (Developer API) requires api_key")

        # Gentle warning if legacy Vertex hints are supplied
        if project_id or location:
            logger.warning(
                "ProviderConfig.google: ignoring Vertex params (project_id/location) "
                "because SDK is in Developer API mode."
            )

        cfg: Dict[str, Any] = {
            "model_name": model_name,
            "api_key": api_key,
        }
        if generation_config is not None:
            cfg["generation_config"] = generation_config
        if safety_settings is not None:
            cfg["safety_settings"] = safety_settings
        return cfg


# -----------------------------------------------------------------------------
# Base client
# -----------------------------------------------------------------------------
class ModelRed:
    def __init__(
        self,
        api_key: Optional[str] = None,
        timeout: int = 30,
        *,
        _client: Optional[ModelRedClient] = None,
    ) -> None:
        settings = load_settings(timeout=timeout)
        self._client = _client or ModelRedClient(api_key=api_key, settings=settings)
        self.timeout = timeout
        self.logger = logger
        self.api_key = self._client.api_key

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": f"ModelRed-PythonSDK/{__version__}",
        }

    # Models
    def create_model(
        self,
        *,
        modelId: str,
        provider: Union[str, ModelProvider],
        displayName: str,
        providerConfig: Dict[str, Any],
        description: Optional[str] = None,
    ) -> Model:
        provider_value = (
            provider.value if isinstance(provider, ModelProvider) else str(provider)
        )
        resource = self._client.models.create(
            model_id=modelId,
            provider=provider_value,
            display_name=displayName,
            provider_config=providerConfig,
            description=description,
        )
        return _to_legacy_model(resource)

    def list_models(self) -> List[Model]:
        return [_to_legacy_model(m) for m in self._client.models.list()]

    def get_model(self, model_identifier: str) -> Model:
        resource = self._client.models.retrieve(model_identifier)
        return _to_legacy_model(resource)

    def delete_model(self, model_identifier: str) -> bool:
        return self._client.models.delete(model_identifier)

    # Assessments
    def create_assessment(
        self,
        *,
        model: str,
        test_types: List[str],
        priority: Union[str, Priority] = Priority.NORMAL,
    ) -> Assessment:
        priority_value = _normalise_priority(priority)
        resource = self._client.assessments.create(
            model=model,
            test_types=test_types,
            priority=priority_value,
        )
        return _to_legacy_assessment(resource)

    def get_assessment(self, assessment_id: str) -> Assessment:
        resource = self._client.assessments.retrieve(assessment_id)
        return _to_legacy_assessment(resource)

    def list_assessments(self, limit: Optional[int] = None) -> List[Assessment]:
        resources = self._client.assessments.list(limit=limit)
        return [_to_legacy_assessment(a) for a in resources]

    def wait_for_completion(
        self,
        assessment_id: str,
        *,
        timeout_minutes: int = 60,
        poll_interval: int = 10,
        progress_callback: Optional[Callable[[Assessment], None]] = None,
    ) -> Assessment:
        wrapped = _wrap_sync_callback(progress_callback)
        resource = self._client.assessments.wait_for_completion(
            assessment_id,
            timeout_seconds=timeout_minutes * 60,
            poll_interval=poll_interval,
            progress_callback=wrapped,
        )
        return _to_legacy_assessment(resource)

    # Probes
    def get_probes(
        self,
        *,
        category: Optional[str] = None,
        tier: Optional[str] = None,
        severity: Optional[str] = None,
    ) -> ProbesIndex:
        return self._client.probes.list(
            category=category,
            tier=tier,
            severity=severity,
        )

    def redacted_api_key(self) -> str:
        return self._client.redacted_api_key()

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ModelRed":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


class AsyncModelRed:
    def __init__(
        self,
        api_key: Optional[str] = None,
        timeout: int = 30,
        *,
        _client: Optional[AsyncModelRedClient] = None,
    ) -> None:
        settings = load_settings(timeout=timeout)
        self._client = _client or AsyncModelRedClient(
            api_key=api_key, settings=settings
        )
        self.timeout = timeout
        self.logger = logger
        self.api_key = self._client.api_key

    # Models
    async def create_model(
        self,
        *,
        modelId: str,
        provider: Union[str, ModelProvider],
        displayName: str,
        providerConfig: Dict[str, Any],
        description: Optional[str] = None,
    ) -> Model:
        provider_value = (
            provider.value if isinstance(provider, ModelProvider) else str(provider)
        )
        resource = await self._client.models.create(
            model_id=modelId,
            provider=provider_value,
            display_name=displayName,
            provider_config=providerConfig,
            description=description,
        )
        return _to_legacy_model(resource)

    async def list_models(self) -> List[Model]:
        resources = await self._client.models.list()
        return [_to_legacy_model(m) for m in resources]

    async def get_model(self, model_identifier: str) -> Model:
        resource = await self._client.models.retrieve(model_identifier)
        return _to_legacy_model(resource)

    async def delete_model(self, model_identifier: str) -> bool:
        return await self._client.models.delete(model_identifier)

    # Assessments
    async def create_assessment(
        self,
        *,
        model: str,
        test_types: List[str],
        priority: Union[str, Priority] = Priority.NORMAL,
    ) -> Assessment:
        priority_value = _normalise_priority(priority)
        resource = await self._client.assessments.create(
            model=model,
            test_types=test_types,
            priority=priority_value,
        )
        return _to_legacy_assessment(resource)

    async def get_assessment(self, assessment_id: str) -> Assessment:
        resource = await self._client.assessments.retrieve(assessment_id)
        return _to_legacy_assessment(resource)

    async def list_assessments(self, limit: Optional[int] = None) -> List[Assessment]:
        resources = await self._client.assessments.list(limit=limit)
        return [_to_legacy_assessment(a) for a in resources]

    async def wait_for_completion(
        self,
        assessment_id: str,
        *,
        timeout_minutes: int = 60,
        poll_interval: int = 10,
        progress_callback: Optional[Callable[[Assessment], None]] = None,
    ) -> Assessment:
        wrapped = _wrap_async_callback(progress_callback)
        resource = await self._client.assessments.wait_for_completion(
            assessment_id,
            timeout_seconds=timeout_minutes * 60,
            poll_interval=poll_interval,
            progress_callback=wrapped,
        )
        return _to_legacy_assessment(resource)

    async def get_probes(
        self,
        *,
        category: Optional[str] = None,
        tier: Optional[str] = None,
        severity: Optional[str] = None,
    ) -> ProbesIndex:
        return await self._client.probes.list(
            category=category,
            tier=tier,
            severity=severity,
        )

    def redacted_api_key(self) -> str:
        return self._client.redacted_api_key()

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AsyncModelRed":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._client.__aexit__(exc_type, exc, tb)


def _normalise_priority(priority: Union[str, Priority]) -> Priority:
    if isinstance(priority, Priority):
        return priority
    return Priority(str(priority).lower())


def _to_legacy_model(model: _ResourceModel) -> Model:
    return Model(
        id=model.id,
        modelId=model.model_id,
        provider=model.provider,
        modelName=model.model_name,
        displayName=model.display_name,
        description=model.description,
        isActive=model.is_active,
        lastTested=model.last_tested,
        testCount=model.test_count,
        createdAt=model.created_at,
        updatedAt=model.updated_at,
        createdByUser=None,
    )


def _to_legacy_assessment(assessment: _ResourceAssessment) -> Assessment:
    return Assessment(
        id=assessment.id,
        modelId=assessment.model_id,
        status=assessment.status,
        testTypes=assessment.test_types,
        priority=assessment.priority,
        progress=assessment.progress,
        results=None,
        errorMessage=None,
        createdAt=assessment.created_at,
        completedAt=assessment.completed_at,
        estimatedDuration=None,
        detailedReport=assessment.detailed_report,
    )


def _wrap_sync_callback(
    callback: Optional[Callable[[Assessment], None]],
) -> Optional[Callable[[_ResourceAssessment], None]]:
    if callback is None:
        return None

    def _inner(resource_assessment: _ResourceAssessment) -> None:
        callback(_to_legacy_assessment(resource_assessment))

    return _inner


def _wrap_async_callback(
    callback: Optional[Callable[[Assessment], None]],
) -> Optional[Callable[[_ResourceAssessment], None]]:
    if callback is None:
        return None

    def _inner(resource_assessment: _ResourceAssessment) -> None:
        callback(_to_legacy_assessment(resource_assessment))

    return _inner


# -----------------------------------------------------------------------------
# Public exports
# -----------------------------------------------------------------------------
__all__ = [
    "ModelRed",
    "AsyncModelRed",
    "ModelRedClient",
    "AsyncModelRedClient",
    "Model",
    "Assessment",
    "ModelProvider",
    "AssessmentStatus",
    "Priority",
    "ProviderConfig",
    # Exceptions
    "ModelRedError",
    "AuthenticationError",
    "AuthorizationError",
    "SubscriptionLimitError",
    "ValidationError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "ServerError",
    "NetworkError",
]
