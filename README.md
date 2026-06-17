# ExecuBot Kernel v0.1

ExecuBot Kernel is the foundation for a Docker-based AI agent orchestration platform. Version `0.1` is intentionally planning-first: it defines the architecture, operating model, repository shape, delivery roadmap, and backlog before implementation begins.

## Phase 1 Scope

- Repository structure
- System architecture diagram
- Development roadmap
- Linear project organization
- Docker environment plan
- Telegram command interface plan
- Memory architecture plan
- GitHub workflow setup
- Task breakdown for future specialist agents

## Initial Agents

- **ExecuBot**: central orchestrator, command router, policy gate, and task dispatcher.
- **Engineering Agent**: implementation, code review, CI health, and technical design.
- **Product Agent**: requirements, prioritization, user flows, and release definition.
- **Operations Agent**: runbooks, deployment readiness, incident response, and observability.
- **Finance Agent**: cost tracking, budget alerts, vendor spend, and financial reporting.
- **Data Agent**: data contracts, analytics events, memory indexing, and reporting.

## Repository Map

```text
.
├── README.md
├── pyproject.toml
├── alembic.ini
├── execubot/
│   ├── api/
│   │   └── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── models.py
│   └── migrations/
├── docs/
│   ├── architecture.md
│   ├── docker-environment.md
│   ├── github-workflow.md
│   ├── linear-organization.md
│   ├── memory-architecture.md
│   ├── roadmap.md
│   ├── telegram-interface.md
│   ├── task-breakdown.md
│   └── decisions.md
├── agents/
│   ├── execubot.md
│   ├── engineering-agent.md
│   ├── product-agent.md
│   ├── operations-agent.md
│   ├── finance-agent.md
│   ├── data-agent.md
│   └── registry.yaml
├── docker/
│   ├── README.md
│   ├── docker-compose.dev.yml
│   └── env.example
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       └── foundation-checks.yml
├── backlog/
│   ├── milestones.md
│   ├── backlog.md
│   ├── milestone-2-local-kernel-skeleton.md
│   └── next-30-days.md
└── tests/
```

## Architecture Summary

ExecuBot receives external commands, normalizes them into tasks, applies authorization and routing policy, and dispatches work to specialist agents. Agents run as isolated services in Docker, use shared memory services through typed interfaces, and emit structured events for auditability.

See [docs/architecture.md](docs/architecture.md) for the full v0.1 architecture.

## Accepted Stack

- Python with FastAPI for `execubot-api`.
- Python worker service for background processing.
- Redis Streams for queueing.
- PostgreSQL for relational state, memory records, and audit.
- Alembic for migrations.
- PostgreSQL with `pgvector` later for semantic memory.
- `python-telegram-bot` for the Telegram interface.
- Docker Compose for local development.
- `.env` for local secrets only; no secrets committed.

## Current Status

This repository is in **Phase 1: Foundation**. Runtime implementation is intentionally deferred until the architecture, backlog, and workflow are stable enough for specialist agents to execute independently.

## Local Development

Prerequisites:

- Python 3.12+
- PostgreSQL 16+

Create a local environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Copy the documented environment variables and adjust local values:

```powershell
Copy-Item docker\env.example .env
```

Run database migrations:

```powershell
alembic upgrade head
```

Start the API:

```powershell
uvicorn execubot.api.main:app --reload
```

Check health:

```powershell
Invoke-RestMethod http://localhost:8000/health
```

Run tests:

```powershell
python -m unittest discover
```

Current skeleton scope includes FastAPI, `.env` config loading, PostgreSQL connection setup, Alembic migrations, and initial models for `audit_events`, `memory_items`, `tasks`, and `approvals`. Redis, Telegram, Discord, Celery, Temporal, and vector search are intentionally not included yet.

## Next Step

Use [backlog/next-30-days.md](backlog/next-30-days.md) to start the first implementation sprint.
