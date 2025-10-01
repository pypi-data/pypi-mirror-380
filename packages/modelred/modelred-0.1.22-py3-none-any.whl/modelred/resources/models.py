"""Model metadata helpers for the ModelRed Python SDK."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional

from ..utils import parse_iso_datetime
from ..http import RequestOptions
from ..exceptions import NotFoundError
from .base import SyncAPIResource, AsyncAPIResource


@dataclass(slots=True)
class Model:
    """Lightweight representation of a registered model."""

    id: str
    model_id: str
    provider: str
    model_name: Optional[str]
    display_name: str
    description: Optional[str]
    is_active: bool
    last_tested: Optional[datetime]
    test_count: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


def parse_model(payload: Dict[str, Any]) -> Model:
    """Convert an API payload into a :class:`Model` instance."""

    return Model(
        id=payload["id"],
        model_id=payload.get("modelId", ""),
        provider=payload.get("provider", ""),
        model_name=payload.get("modelName"),
        display_name=payload.get("displayName", ""),
        description=payload.get("description"),
        is_active=payload.get("isActive", True),
        last_tested=parse_iso_datetime(payload.get("lastTested")),
        test_count=payload.get("testCount", 0),
        created_at=parse_iso_datetime(payload.get("createdAt")),
        updated_at=parse_iso_datetime(payload.get("updatedAt")),
    )


class ModelsClient(SyncAPIResource):
    """Synchronous helper for `/models` endpoints."""

    _RESOURCE_PATH = "/models"

    def list(self, *, options: Optional[RequestOptions] = None) -> list[Model]:
        payload = self._request("GET", self._RESOURCE_PATH, options=options)
        data = payload.get("data", [])
        return [parse_model(item) for item in data]

    def retrieve(
        self, identifier: str, *, options: Optional[RequestOptions] = None
    ) -> Model:
        try:
            payload = self._request(
                "GET", f"{self._RESOURCE_PATH}/{identifier}", options=options
            )
        except NotFoundError:
            # Fallback: attempt to resolve by external modelId
            for model in self.list(options=options):
                if model.model_id == identifier:
                    return model
            raise
        return parse_model(payload.get("data", payload))

    def create(
        self,
        *,
        model_id: str,
        provider: str,
        display_name: str,
        provider_config: Dict[str, Any],
        description: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> Model:
        body: Dict[str, Any] = {
            "modelId": model_id,
            "provider": provider,
            "displayName": display_name,
            "providerConfig": provider_config,
        }
        if description:
            body["description"] = description

        payload = self._request("POST", self._RESOURCE_PATH, json=body, options=options)
        return parse_model(payload.get("data", payload))

    def delete(
        self, identifier: str, *, options: Optional[RequestOptions] = None
    ) -> bool:
        model = self.retrieve(identifier, options=options)
        payload = self._request(
            "DELETE", f"{self._RESOURCE_PATH}/{model.id}", options=options
        )
        return bool(payload.get("success", True))


class AsyncModelsClient(AsyncAPIResource):
    """Async helper for `/models` endpoints."""

    _RESOURCE_PATH = "/models"

    async def list(self, *, options: Optional[RequestOptions] = None) -> list[Model]:
        payload = await self._request("GET", self._RESOURCE_PATH, options=options)
        data = payload.get("data", [])
        return [parse_model(item) for item in data]

    async def retrieve(
        self, identifier: str, *, options: Optional[RequestOptions] = None
    ) -> Model:
        try:
            payload = await self._request(
                "GET", f"{self._RESOURCE_PATH}/{identifier}", options=options
            )
        except NotFoundError:
            models = await self.list(options=options)
            for model in models:
                if model.model_id == identifier:
                    return model
            raise
        return parse_model(payload.get("data", payload))

    async def create(
        self,
        *,
        model_id: str,
        provider: str,
        display_name: str,
        provider_config: Dict[str, Any],
        description: Optional[str] = None,
        options: Optional[RequestOptions] = None,
    ) -> Model:
        body: Dict[str, Any] = {
            "modelId": model_id,
            "provider": provider,
            "displayName": display_name,
            "providerConfig": provider_config,
        }
        if description:
            body["description"] = description

        payload = await self._request(
            "POST", self._RESOURCE_PATH, json=body, options=options
        )
        return parse_model(payload.get("data", payload))

    async def delete(
        self, identifier: str, *, options: Optional[RequestOptions] = None
    ) -> bool:
        model = await self.retrieve(identifier, options=options)
        payload = await self._request(
            "DELETE", f"{self._RESOURCE_PATH}/{model.id}", options=options
        )
        return bool(payload.get("success", True))
