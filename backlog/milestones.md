# Milestones

## Milestone 0: Foundation

Outcome: planning, structure, and project organization are ready.

Deliverables:

- Architecture document.
- Repository structure.
- Roadmap.
- Docker environment plan.
- Telegram interface plan.
- Memory architecture plan.
- Linear organization plan.
- GitHub workflow setup.
- Specialist agent task breakdown.

## Milestone 1: Local Kernel Skeleton

Outcome: local orchestrator can create and track tasks without external autonomy.

Deliverables:

- Runtime selected.
- Service skeleton.
- Command envelope schema.
- Task packet schema.
- Local task state store.
- Redis Streams local queue.
- Agent registry config.
- Basic health endpoint.
- Alembic migration for `audit_events`.

Note: This is also tracked as the first implementation plan under "Milestone 2: Local Kernel Skeleton" because implementation numbering starts after the documentation foundation.

## Milestone 2: Telegram MVP

Outcome: a single authorized operator can create and monitor tasks through Telegram.

Deliverables:

- Telegram bot service.
- Operator allowlist.
- Core command handlers.
- Approval workflow.
- Audit logging.

## Milestone 3: Memory MVP

Outcome: agents can retrieve and write scoped memory through a controlled API.

Deliverables:

- Memory API.
- Session/task summaries.
- Project memory store.
- Vector memory prototype.
- Redaction and promotion policy.

## Milestone 4: Specialist Agent MVPs

Outcome: each initial agent has a constrained, useful first capability.

Deliverables:

- Engineering Agent MVP.
- Product Agent MVP.
- Operations Agent MVP.
- Finance Agent MVP.
- Data Agent MVP.
- Agent output artifact convention.

## Milestone 5: GitHub + Linear Integration

Outcome: planning and delivery workflows connect to the kernel.

Deliverables:

- GitHub issue and PR workflows.
- Linear project and issue templates.
- Status synchronization plan.
- Agent branch naming convention.

## Milestone 6: Alpha Hardening

Outcome: controlled daily use is possible with auditability and rollback paths.

Deliverables:

- Security review.
- Observability dashboard.
- Backup and restore runbook.
- Operator acceptance tests.
- Deployment plan.
