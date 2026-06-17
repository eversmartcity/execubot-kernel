# Docker Environment Plan

## Goals

- Provide repeatable local development.
- Isolate agent execution.
- Make dependencies explicit.
- Support future production deployment without redesigning service boundaries.

## Planned Services

| Service | Purpose | Phase |
| --- | --- | --- |
| `execubot-api` | Python FastAPI orchestration API and command gateway. | Milestone 2 |
| `execubot-worker` | Python worker service for Redis Streams task handling. | Milestone 2 |
| `telegram-bot` | `python-telegram-bot` command interface. | Milestone 3 |
| `postgres` | Relational metadata, task state, memory records, and audit index. | Milestone 2 |
| `redis` | Redis Streams queue, short-term coordination, rate limits. | Milestone 2 |
| `observability` | Local logs and metrics surface. | Milestone 3 |
| `agent-engineering` | Engineering Agent container. | Milestone 4 |
| `agent-product` | Product Agent container. | Milestone 4 |
| `agent-operations` | Operations Agent container. | Milestone 4 |
| `agent-finance` | Finance Agent container. | Milestone 4 |
| `agent-data` | Data Agent container. | Milestone 4 |

## Environment Files

- `docker/env.example`: documented variables.
- `.env`: local developer secrets, ignored by Git in the future.
- `.env.test`: deterministic test configuration.

## Isolation Model

- Each specialist agent runs in its own container.
- Agent containers receive scoped workspace mounts.
- External credentials are provided through narrow environment variables or secret mounts.
- ExecuBot owns task assignment and approval state.
- Agents write artifacts to shared output volumes, not arbitrary host paths.

## Development Compose File

`docker/docker-compose.dev.yml` is the local development stack. During Milestone 2 it should be updated to build concrete Python images for `execubot-api` and `execubot-worker`.

## Accepted Implementation Decisions

- Language/framework: Python with FastAPI.
- Worker: Python worker service.
- Queue: Redis Streams.
- Database: PostgreSQL.
- Memory/vector store: PostgreSQL first, `pgvector` later.
- Migrations: Alembic.
- Telegram: `python-telegram-bot`.
- Docker: Docker Compose local development stack.
- Secrets: `.env` for local only, with no secrets committed.

## Remaining Docker Questions

- Whether each specialist agent uses the same base image or a custom toolchain image.
- Exact local volume layout for agent workspaces and artifacts.
- Production secret management and deployment target.
