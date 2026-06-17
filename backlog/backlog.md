# Backlog

## P0 Foundation

- Define command envelope schema.
- Define task packet schema.
- Backend runtime selected: Python with FastAPI.
- Worker selected: Python worker service.
- Queue selected: Redis Streams.
- Database selected: PostgreSQL.
- Migration tool selected: Alembic.
- Define local Docker Compose stack.
- Define agent registry format.
- Define approval gate model.
- Define audit event schema.
- Define memory API contracts.

## P1 Local MVP

- Build `execubot-api` skeleton.
- Build `execubot-worker` skeleton.
- Add health check endpoint.
- Add task creation endpoint.
- Add task status endpoint.
- Implement Redis Streams local queue.
- Implement append-only `audit_events` table.
- Add basic config loading.
- Add unit test harness.
- Add Docker Compose smoke test.

## P1 Telegram MVP

- Create Telegram bot service.
- Add operator allowlist.
- Implement `/help`.
- Implement `/status`.
- Implement `/agents`.
- Implement `/task`.
- Implement `/task_status`.
- Implement `/approve`.
- Implement `/reject`.
- Implement `/cancel`.

## P2 Memory MVP

- Create memory service interface.
- Store task summaries.
- Store project decisions.
- Add memory search endpoint.
- Add semantic indexing prototype.
- Add memory redaction workflow.
- Add memory promotion workflow.

## P2 Specialist Agents

- Implement Engineering Agent read-only repo inspection.
- Implement Product Agent backlog refinement.
- Implement Operations Agent runbook generation.
- Implement Finance Agent cost summary prototype.
- Implement Data Agent schema and report generation.
- Add common agent task packet parser.

## P3 Integrations

- Add GitHub issue intake.
- Add GitHub PR status reporting.
- Add Linear issue creation.
- Add Linear status updates.
- Add notification routing.
- Add cross-system correlation IDs.

## P3 Hardening

- Add role-based authorization.
- Add secret scanning.
- Add structured logging.
- Add metrics.
- Add trace IDs.
- Add backup plan.
- Add restore validation.
- Add deployment runbook.
