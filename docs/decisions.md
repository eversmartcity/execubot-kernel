# Architecture Decisions

This file records significant project decisions. Add one entry per decision so future agents can understand why the platform took its current shape.

## ADR-0001: Start Documentation-First

Date: 2026-06-17

Status: Accepted

Decision:

ExecuBot Kernel v0.1 starts with architecture, roadmap, operating model, and task breakdown before runtime implementation.

Rationale:

The project coordinates multiple future specialist agents. Clear boundaries, schemas, milestones, and approval rules reduce rework before implementation begins.

Consequences:

- Docker and CI files are intentionally lightweight placeholders.
- Runtime selection was finalized in ADR-0002.
- Specialist agents receive documented responsibilities before code-level tasks.

## ADR-0002: Use Python, FastAPI, Redis Streams, PostgreSQL, and Alembic

Date: 2026-06-17

Status: Accepted

Decision:

ExecuBot Kernel v0.1 will use Python with FastAPI for the API service, a Python worker service for background task handling, Redis Streams for queueing, PostgreSQL for relational state, and Alembic for database migrations.

Rationale:

This stack is straightforward to run locally with Docker Compose, has mature libraries for APIs, background workers, migrations, and Telegram bots, and keeps the first implementation small enough for rapid iteration.

Consequences:

- Milestone 2 implementation should create `execubot-api` and `execubot-worker` as Python services.
- Queue contracts should target Redis Streams consumer groups.
- Database changes should be represented as Alembic migrations from the start.
- CI should add Python formatting, linting, tests, and migration checks once code exists.

## ADR-0003: Use PostgreSQL First, Add pgvector Later

Date: 2026-06-17

Status: Accepted

Decision:

ExecuBot Kernel v0.1 will use PostgreSQL for task state, metadata, memory records, and audit events. Semantic memory will use PostgreSQL with `pgvector` later instead of adding a separate vector database during the first local skeleton.

Rationale:

PostgreSQL keeps the local stack smaller and avoids premature infrastructure complexity. `pgvector` provides a clear upgrade path when semantic retrieval becomes necessary.

Consequences:

- Initial memory tables should be relational.
- Vector columns and indexes should be deferred until the Memory MVP.
- Docker Compose only needs PostgreSQL and Redis for the first local skeleton.

## ADR-0004: Telegram Uses python-telegram-bot

Date: 2026-06-17

Status: Accepted

Decision:

The Telegram command interface will use `python-telegram-bot`.

Rationale:

The library fits the Python stack, supports async command handlers, and is sufficient for a single-operator MVP.

Consequences:

- Telegram command handlers should emit the same command envelope used by other inputs.
- Telegram remains a separate service in Docker Compose once Milestone 3 begins.

## ADR-0005: Local Secrets Use .env Only

Date: 2026-06-17

Status: Accepted

Decision:

Local development secrets will be read from `.env`. Secret values must not be committed.

Rationale:

This is enough for local development and keeps secret management simple until production deployment exists.

Consequences:

- `.env` and `.env.*` remain ignored except documented examples.
- Docker Compose should use documented environment variables.
- Production secret management remains a future deployment decision.

## ADR-0006: Human Approval Required For High-Impact Actions

Date: 2026-06-17

Status: Accepted

Decision:

Human approval is required for external actions, shell commands, GitHub writes, financial actions, email/SMS, and deployments.

Rationale:

The platform is designed for agent orchestration, but v0.1 must preserve operator control around side effects and risk.

Consequences:

- Task state must support approval-required and approval-rejected states.
- Agents may propose gated actions but may not execute them without approval.
- Telegram must support `/approve` and `/reject` before risky actions are enabled.

## ADR-0007: Audit Uses Append-Only audit_events Table

Date: 2026-06-17

Status: Accepted

Decision:

Audit records will be written to an append-only `audit_events` table.

Rationale:

Append-only events provide traceability for commands, task transitions, routing decisions, approvals, errors, and external action requests.

Consequences:

- Milestone 2 must include an initial `audit_events` migration.
- Application code should add events instead of mutating or deleting historical audit records.
- Audit retention and export policies can be added during hardening.
