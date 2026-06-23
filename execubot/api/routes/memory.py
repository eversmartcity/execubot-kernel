from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from execubot.api.schemas import MemoryItemCreate, MemoryItemRead
from execubot.core.database import get_session
from execubot.core.models import MemoryItem


router = APIRouter(prefix="/memory/items", tags=["memory"])


@router.post("", response_model=MemoryItemRead, status_code=201)
def create_memory_item(
    payload: MemoryItemCreate,
    session: Annotated[Session, Depends(get_session)],
) -> MemoryItem:
    item = MemoryItem(
        scope=payload.scope,
        key=payload.key,
        content=payload.content,
        metadata_=payload.metadata,
    )
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("", response_model=list[MemoryItemRead])
def list_memory_items(
    session: Annotated[Session, Depends(get_session)],
    scope: str | None = None,
    limit: Annotated[int, Query(ge=1, le=500)] = 100,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[MemoryItem]:
    statement = select(MemoryItem).order_by(MemoryItem.created_at.desc()).offset(offset).limit(limit)
    if scope is not None:
        statement = statement.where(MemoryItem.scope == scope)
    return list(session.scalars(statement).all())
