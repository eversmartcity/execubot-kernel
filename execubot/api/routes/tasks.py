from __future__ import annotations

from typing import Annotated
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from execubot.api.schemas import TaskCreate, TaskRead
from execubot.core.database import get_session
from execubot.core.models import Task, TaskStatus


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskRead, status_code=201)
def create_task(
    payload: TaskCreate,
    session: Annotated[Session, Depends(get_session)],
) -> Task:
    task = Task(
        source=payload.source,
        goal=payload.goal,
        assigned_agent=payload.assigned_agent,
        correlation_id=payload.correlation_id,
        status=TaskStatus.CREATED,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    task_id: uuid.UUID,
    session: Annotated[Session, Depends(get_session)],
) -> Task:
    task = session.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
