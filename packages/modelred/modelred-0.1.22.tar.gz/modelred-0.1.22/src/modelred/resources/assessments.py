"""Assessment-related helpers for the ModelRed Python SDK."""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Sequence

from ..utils import parse_iso_datetime
from ..http import RequestOptions
from ..exceptions import ModelRedError
from .base import SyncAPIResource, AsyncAPIResource


class AssessmentStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class AssessmentPriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(slots=True)
class Assessment:
    """Lightweight representation of an assessment job."""

    id: str
    model_id: str
    status: AssessmentStatus
    test_types: List[str]
    priority: AssessmentPriority
    progress: int
    created_at: Optional[datetime]
    completed_at: Optional[datetime]
    detailed_report: Optional[Dict[str, Any]]


def parse_assessment(payload: Dict[str, Any]) -> Assessment:
    """Convert an API payload into an :class:`Assessment` instance."""

    status_value = payload.get("status", AssessmentStatus.QUEUED.value)
    priority_value = payload.get("priority", AssessmentPriority.NORMAL.value)

    try:
        status = AssessmentStatus(status_value.lower())
    except ValueError:
        status = AssessmentStatus.QUEUED

    try:
        priority = AssessmentPriority(priority_value.lower())
    except ValueError:
        priority = AssessmentPriority.NORMAL

    return Assessment(
        id=payload["id"],
        model_id=payload.get("modelId", ""),
        status=status,
        test_types=list(payload.get("testTypes", [])),
        priority=priority,
        progress=payload.get("progress", 0),
        created_at=parse_iso_datetime(payload.get("createdAt")),
        completed_at=parse_iso_datetime(payload.get("completedAt")),
        detailed_report=payload.get("detailedReport"),
    )


class AssessmentsClient(SyncAPIResource):
    """Synchronous helper for `/assessments` endpoints."""

    _RESOURCE_PATH = "/assessments"

    def list(
        self,
        *,
        limit: Optional[int] = None,
        options: Optional[RequestOptions] = None,
    ) -> list[Assessment]:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = str(limit)
        payload = self._request(
            "GET", self._RESOURCE_PATH, params=params or None, options=options
        )
        data = payload.get("data", [])
        return [parse_assessment(item) for item in data]

    def retrieve(
        self, assessment_id: str, *, options: Optional[RequestOptions] = None
    ) -> Assessment:
        payload = self._request(
            "GET", f"{self._RESOURCE_PATH}/{assessment_id}", options=options
        )
        return parse_assessment(payload.get("data", payload))

    def create(
        self,
        *,
        model: str,
        test_types: Sequence[str],
        priority: AssessmentPriority = AssessmentPriority.NORMAL,
        options: Optional[RequestOptions] = None,
    ) -> Assessment:
        body = {
            "model": model,
            "testTypes": list(test_types),
            "priority": priority.value,
        }
        payload = self._request("POST", self._RESOURCE_PATH, json=body, options=options)
        return parse_assessment(payload.get("data", payload))

    def wait_for_completion(
        self,
        assessment_id: str,
        *,
        timeout_seconds: int = 3600,
        poll_interval: int = 10,
        progress_callback: Optional[Callable[[Assessment], None]] = None,
        options: Optional[RequestOptions] = None,
    ) -> Assessment:
        deadline = time.time() + timeout_seconds
        last_status: Optional[AssessmentStatus] = None
        while time.time() < deadline:
            assessment = self.retrieve(assessment_id, options=options)
            if progress_callback and assessment.status != last_status:
                progress_callback(assessment)
                last_status = assessment.status
            if assessment.status in (
                AssessmentStatus.COMPLETED,
                AssessmentStatus.FAILED,
                AssessmentStatus.CANCELLED,
            ):
                return assessment
            time.sleep(max(1, poll_interval))
        raise ModelRedError(
            f"Assessment '{assessment_id}' did not complete within {timeout_seconds} seconds."
        )


class AsyncAssessmentsClient(AsyncAPIResource):
    """Async helper for `/assessments` endpoints."""

    _RESOURCE_PATH = "/assessments"

    async def list(
        self,
        *,
        limit: Optional[int] = None,
        options: Optional[RequestOptions] = None,
    ) -> list[Assessment]:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = str(limit)
        payload = await self._request(
            "GET", self._RESOURCE_PATH, params=params or None, options=options
        )
        data = payload.get("data", [])
        return [parse_assessment(item) for item in data]

    async def retrieve(
        self, assessment_id: str, *, options: Optional[RequestOptions] = None
    ) -> Assessment:
        payload = await self._request(
            "GET", f"{self._RESOURCE_PATH}/{assessment_id}", options=options
        )
        return parse_assessment(payload.get("data", payload))

    async def create(
        self,
        *,
        model: str,
        test_types: Sequence[str],
        priority: AssessmentPriority = AssessmentPriority.NORMAL,
        options: Optional[RequestOptions] = None,
    ) -> Assessment:
        body = {
            "model": model,
            "testTypes": list(test_types),
            "priority": priority.value,
        }
        payload = await self._request(
            "POST", self._RESOURCE_PATH, json=body, options=options
        )
        return parse_assessment(payload.get("data", payload))

    async def wait_for_completion(
        self,
        assessment_id: str,
        *,
        timeout_seconds: int = 3600,
        poll_interval: int = 10,
        progress_callback: Optional[Callable[[Assessment], None]] = None,
        options: Optional[RequestOptions] = None,
    ) -> Assessment:
        deadline = time.time() + timeout_seconds
        last_status: Optional[AssessmentStatus] = None
        while time.time() < deadline:
            assessment = await self.retrieve(assessment_id, options=options)
            if progress_callback and assessment.status != last_status:
                progress_callback(assessment)
                last_status = assessment.status
            if assessment.status in (
                AssessmentStatus.COMPLETED,
                AssessmentStatus.FAILED,
                AssessmentStatus.CANCELLED,
            ):
                return assessment
            await asyncio.sleep(max(1, poll_interval))
        raise ModelRedError(
            f"Assessment '{assessment_id}' did not complete within {timeout_seconds} seconds."
        )
