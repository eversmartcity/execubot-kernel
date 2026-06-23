from __future__ import annotations

import enum
from datetime import datetime
import uuid

from sqlalchemy import DateTime, Enum, ForeignKey, Index, JSON, String, Text, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from execubot.core.database import Base


class TaskStatus(str, enum.Enum):
    CREATED = "created"
    QUEUED = "queued"
    RUNNING = "running"
    APPROVAL_REQUIRED = "approval_required"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ApprovalStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_type: Mapped[str] = mapped_column(String(120), nullable=False)
    actor: Mapped[str | None] = mapped_column(String(120))
    task_id: Mapped[uuid.UUID | None] = mapped_column(Uuid(as_uuid=True), ForeignKey("tasks.id"))
    payload: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    task: Mapped["Task | None"] = relationship(back_populates="audit_events")


class MemoryItem(Base):
    __tablename__ = "memory_items"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scope: Mapped[str] = mapped_column(String(80), nullable=False)
    key: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    metadata_: Mapped[dict] = mapped_column("metadata", JSON, nullable=False, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source: Mapped[str] = mapped_column(String(80), nullable=False)
    goal: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, name="task_status", values_callable=lambda enum_cls: [item.value for item in enum_cls]),
        nullable=False,
        default=TaskStatus.CREATED,
    )
    assigned_agent: Mapped[str | None] = mapped_column(String(120))
    correlation_id: Mapped[str | None] = mapped_column(String(120), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    audit_events: Mapped[list[AuditEvent]] = relationship(back_populates="task")
    approvals: Mapped[list["Approval"]] = relationship(back_populates="task")


class Approval(Base):
    __tablename__ = "approvals"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), ForeignKey("tasks.id"), nullable=False)
    action_type: Mapped[str] = mapped_column(String(120), nullable=False)
    status: Mapped[ApprovalStatus] = mapped_column(
        Enum(
            ApprovalStatus,
            name="approval_status",
            values_callable=lambda enum_cls: [item.value for item in enum_cls],
        ),
        nullable=False,
        default=ApprovalStatus.PENDING,
    )
    requested_by: Mapped[str | None] = mapped_column(String(120))
    decided_by: Mapped[str | None] = mapped_column(String(120))
    reason: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    decided_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    task: Mapped[Task] = relationship(back_populates="approvals")


Index("ix_audit_events_task_id_created_at", AuditEvent.task_id, AuditEvent.created_at)
Index("ix_memory_items_scope_key", MemoryItem.scope, MemoryItem.key)
Index("ix_tasks_status_created_at", Task.status, Task.created_at)
Index("ix_approvals_task_id_status", Approval.task_id, Approval.status)
