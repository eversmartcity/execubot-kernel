# Development Roadmap

## Milestone 0: Foundation

Define the architecture, repository conventions, agent roles, backlog, and implementation sequencing.

Exit criteria:

- Repository structure exists.
- Architecture and memory plans are documented.
- Docker and GitHub workflow plans exist.
- Linear organization model is ready to create.
- First 30-day implementation plan is actionable.

## Milestone 1: Local Kernel Skeleton

Build a local-only orchestration skeleton with no external autonomy.

Planned outcomes:

- Command envelope schema.
- Task packet schema.
- ExecuBot routing stub.
- Agent registry config.
- Docker Compose development stack using Python, FastAPI, PostgreSQL, and Redis.
- Redis Streams local task queue.
- Append-only PostgreSQL `audit_events` table.
- Alembic migrations.

## Milestone 2: Telegram MVP

Add a controlled Telegram command interface for a single operator.

Planned outcomes:

- `python-telegram-bot` service.
- `/status`, `/agents`, `/task`, `/approve`, `/cancel`, `/help`.
- Operator allowlist.
- Command audit trail.
- Human approval gates.
- Basic progress replies.

## Milestone 3: Memory MVP

Add project memory and task history with explicit read/write contracts.

Planned outcomes:

- Session memory.
- Project metadata store.
- PostgreSQL memory tables with `pgvector` added later.
- Memory access policy.
- Agent memory summaries.

## Milestone 4: Specialist Agent MVPs

Introduce limited specialist agents with constrained capabilities.

Planned outcomes:

- Engineering Agent can inspect repos and propose patches.
- Product Agent can refine specs and prioritize backlog.
- Operations Agent can draft runbooks and check health signals.
- Finance Agent can summarize cost records.
- Data Agent can define analytics and memory indexes.

## Milestone 5: GitHub + Linear Integration

Connect planning and delivery surfaces.

Planned outcomes:

- GitHub issue and PR templates.
- CI checks.
- Linear project, milestones, labels, and issue templates.
- Task status synchronization design.

## Milestone 6: Alpha Hardening

Prepare the platform for controlled daily use.

Planned outcomes:

- Security review.
- Observability dashboard.
- Error handling policy.
- Backup and restore plan.
- Deployment runbook.
- Operator acceptance tests.
