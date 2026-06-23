from __future__ import annotations

from datetime import datetime
from typing import Any
import uuid

from pydantic import BaseModel, ConfigDict, Field

from execubot.core.models import TaskStatus


class AuditEventCreate(BaseModel):
    event_type: str = Field(..., min_length=1, max_length=120)
    actor: str | None = Field(default=None, max_length=120)
    task_id: uuid.UUID | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class AuditEventRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    event_type: str
    actor: str | None
    task_id: uuid.UUID | None
    payload: dict[str, Any]
    created_at: datetime


class MemoryItemCreate(BaseModel):
    scope: str = Field(..., min_length=1, max_length=80)
    key: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    metadata: dict[str, Any] = Field(default_factory=dict)


class MemoryItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    scope: str
    key: str
    content: str
    metadata: dict[str, Any] = Field(validation_alias="metadata_")
    created_at: datetime
    updated_at: datetime


class TaskCreate(BaseModel):
    source: str = Field(..., min_length=1, max_length=80)
    goal: str = Field(..., min_length=1)
    assigned_agent: str | None = Field(default=None, max_length=120)
    correlation_id: str | None = Field(default=None, max_length=120)


class TaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    source: str
    goal: str
    status: TaskStatus
    assigned_agent: str | None
    correlation_id: str | None
    created_at: datetime
    updated_at: datetime
