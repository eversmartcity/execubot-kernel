"""create initial kernel tables

Revision ID: 20260617_0001
Revises:
Create Date: 2026-06-17
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "20260617_0001"
down_revision = None
branch_labels = None
depends_on = None


task_status = postgresql.ENUM(
    "created",
    "queued",
    "running",
    "approval_required",
    "completed",
    "failed",
    "cancelled",
    name="task_status",
)

approval_status = postgresql.ENUM(
    "pending",
    "approved",
    "rejected",
    "cancelled",
    name="approval_status",
)


def upgrade() -> None:
    task_status.create(op.get_bind(), checkfirst=True)
    approval_status.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "tasks",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("source", sa.String(length=80), nullable=False),
        sa.Column("goal", sa.Text(), nullable=False),
        sa.Column("status", task_status, nullable=False),
        sa.Column("assigned_agent", sa.String(length=120), nullable=True),
        sa.Column("correlation_id", sa.String(length=120), nullable=True, unique=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_tasks_status_created_at", "tasks", ["status", "created_at"])

    op.create_table(
        "memory_items",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("scope", sa.String(length=80), nullable=False),
        sa.Column("key", sa.String(length=200), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_memory_items_scope_key", "memory_items", ["scope", "key"])

    op.create_table(
        "audit_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("event_type", sa.String(length=120), nullable=False),
        sa.Column("actor", sa.String(length=120), nullable=True),
        sa.Column("task_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("tasks.id"), nullable=True),
        sa.Column("payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_audit_events_task_id_created_at", "audit_events", ["task_id", "created_at"])

    op.create_table(
        "approvals",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("task_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("tasks.id"), nullable=False),
        sa.Column("action_type", sa.String(length=120), nullable=False),
        sa.Column("status", approval_status, nullable=False),
        sa.Column("requested_by", sa.String(length=120), nullable=True),
        sa.Column("decided_by", sa.String(length=120), nullable=True),
        sa.Column("reason", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("decided_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_approvals_task_id_status", "approvals", ["task_id", "status"])


def downgrade() -> None:
    op.drop_index("ix_approvals_task_id_status", table_name="approvals")
    op.drop_table("approvals")
    op.drop_index("ix_audit_events_task_id_created_at", table_name="audit_events")
    op.drop_table("audit_events")
    op.drop_index("ix_memory_items_scope_key", table_name="memory_items")
    op.drop_table("memory_items")
    op.drop_index("ix_tasks_status_created_at", table_name="tasks")
    op.drop_table("tasks")
    approval_status.drop(op.get_bind(), checkfirst=True)
    task_status.drop(op.get_bind(), checkfirst=True)
