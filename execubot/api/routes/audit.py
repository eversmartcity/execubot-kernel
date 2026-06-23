from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from execubot.api.schemas import AuditEventCreate, AuditEventRead
from execubot.core.database import get_session
from execubot.core.models import AuditEvent


router = APIRouter(prefix="/audit/events", tags=["audit"])


@router.post("", response_model=AuditEventRead, status_code=201)
def create_audit_event(
    payload: AuditEventCreate,
    session: Annotated[Session, Depends(get_session)],
) -> AuditEvent:
    event = AuditEvent(**payload.model_dump())
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


@router.get("", response_model=list[AuditEventRead])
def list_audit_events(
    session: Annotated[Session, Depends(get_session)],
    limit: Annotated[int, Query(ge=1, le=500)] = 100,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[AuditEvent]:
    statement = select(AuditEvent).order_by(AuditEvent.created_at.desc()).offset(offset).limit(limit)
    return list(session.scalars(statement).all())
