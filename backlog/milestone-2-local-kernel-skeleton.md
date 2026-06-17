# Milestone 2 Implementation Plan: Local Kernel Skeleton

This plan converts the documentation foundation into the first runnable local kernel. It maps to the roadmap item previously called "Local Kernel Skeleton" and uses the accepted v0.1 stack.

## Goal

Create a local Docker Compose stack where `execubot-api` can accept a task, persist task state, append audit events, publish work to Redis Streams, and where `execubot-worker` can consume the task and update status.

## Accepted Stack

- API: Python with FastAPI.
- Worker: Python worker service.
- Queue: Redis Streams.
- Database: PostgreSQL.
- Migrations: Alembic.
- Memory/vector store: PostgreSQL first, `pgvector` later.
- Secrets: `.env` for local only, no secrets committed.
- Audit: append-only `audit_events` table.

## Proposed Repository Additions

```text
execubot/
|-- api/
|   |-- main.py
|   |-- routes/
|   `-- schemas/
|-- core/
|   |-- config.py
|   |-- database.py
|   |-- audit.py
|   |-- queue.py
|   `-- models.py
|-- worker/
|   `-- main.py
`-- migrations/
    |-- env.py
    `-- versions/

tests/
|-- test_health.py
|-- test_tasks.py
`-- test_audit.py

pyproject.toml
alembic.ini
Dockerfile.api
Dockerfile.worker
```

## Database Scope

Initial tables:

- `tasks`: task ID, source, status, goal, assigned agent, timestamps.
- `task_events`: task-specific status events.
- `audit_events`: append-only audit stream for commands, decisions, approvals, and errors.
- `agent_registry`: registered agents and availability metadata.

Initial task statuses:

- `created`
- `queued`
- `running`
- `approval_required`
- `completed`
- `failed`
- `cancelled`

## API Scope

Initial endpoints:

- `GET /health`
- `POST /tasks`
- `GET /tasks/{task_id}`
- `GET /agents`
- `GET /audit/events?task_id=...`

Out of scope for this milestone:

- Telegram bot.
- GitHub writes.
- Linear writes.
- Specialist agent execution.
- Semantic search.
- Production deployment.

## Redis Streams Scope

Streams:

- `execubot.tasks`: tasks ready for worker processing.
- `execubot.events`: optional worker/event notifications after initial API flow works.

Consumer group:

- `execubot-workers`

Worker behavior:

1. Read from `execubot.tasks`.
2. Mark task `running`.
3. Append audit event.
4. Simulate a no-op agent routing result.
5. Mark task `completed` or `approval_required` depending on requested action type.
6. Acknowledge the stream message.

## Approval Model Scope

The local skeleton should classify the following as approval-required:

- External actions.
- Shell commands.
- GitHub writes.
- Financial actions.
- Email or SMS.
- Deployments.

The skeleton does not execute these actions. It only stores the approval requirement and returns that state to the operator.

## Implementation Sequence

1. Create Python project metadata and dependency groups.
2. Add FastAPI service with `/health`.
3. Add configuration loading from `.env`.
4. Add PostgreSQL connection and Alembic setup.
5. Create initial migrations for `tasks`, `task_events`, `audit_events`, and `agent_registry`.
6. Implement task creation and lookup endpoints.
7. Implement audit event writer.
8. Implement Redis Streams publisher.
9. Implement Python worker consumer.
10. Wire Docker Compose to build and run API, worker, PostgreSQL, and Redis.
11. Add tests for health, task creation, audit writing, and approval-required classification.
12. Add CI checks for tests and foundation structure.

## Acceptance Criteria

- `docker compose -f docker/docker-compose.dev.yml up --build` starts API, worker, PostgreSQL, and Redis.
- `GET /health` returns healthy.
- `POST /tasks` creates a persisted task and appends an audit event.
- A created task is published to Redis Streams.
- The worker consumes the task and updates task status.
- Requests that imply gated actions result in `approval_required`.
- No local secrets are committed.
- Alembic can create the database schema from scratch.

## Risks

- Redis Streams consumer-group handling can create stuck pending messages if not acknowledged correctly.
- Approval classification needs to stay conservative until policies are more mature.
- The first schema should stay small to avoid overfitting before Telegram and memory work begin.

## Open Questions

- Use SQLAlchemy ORM models, SQLAlchemy Core, or SQLModel.
- Use `uv`, Poetry, or plain `pip`/requirements for dependency management.
- Use `pytest-asyncio` for async API/database tests or keep database access synchronous initially.
- Whether task IDs should be UUIDv7, ULID, or standard UUID4.
- Whether API and worker share one package or separate deployable packages inside the repo.
