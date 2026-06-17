# Next 30-Day Implementation Plan

## Week 1: Foundation Decisions

Objectives:

- Record accepted implementation decisions as ADRs.
- Convert open stack questions into implementation tickets.
- Finalize command envelope and task packet schemas.
- Create initial Linear project and issues.

Outputs:

- Architecture decision records.
- First schema drafts.
- Linear project populated.
- Docker Compose plan refined into concrete Python, PostgreSQL, and Redis services.

## Week 2: Local Kernel Skeleton

Objectives:

- Implement `execubot-api` skeleton.
- Implement Python worker skeleton.
- Implement task creation and task status.
- Add append-only `audit_events` table.
- Add Redis Streams publishing and consuming.
- Add initial Docker Compose stack.

Outputs:

- Local service starts with one command.
- Health check passes.
- Task can be created and inspected.
- Worker can consume a task from Redis Streams.
- CI verifies foundation checks and basic tests.

## Week 3: Routing + Telegram MVP

Objectives:

- Implement agent registry.
- Implement basic routing rules.
- Create Telegram bot service.
- Add operator allowlist and core commands.

Outputs:

- `/status`, `/agents`, `/task`, and `/task_status` work locally.
- Task IDs are returned to the operator.
- All Telegram commands write audit events.

## Week 4: Memory + Agent MVP Specs

Objectives:

- Implement memory API interface.
- Store task summaries and decisions.
- Defer `pgvector` until relational memory is stable.
- Define each specialist agent's first executable capability.
- Add approval gate state machine.

Outputs:

- Memory API prototype.
- Approval-required task state.
- Specialist agent implementation tickets ready.
- Alpha hardening risks documented.

## 30-Day Success Criteria

- A developer can run the local stack.
- ExecuBot can accept, store, and report a task.
- Telegram can create and inspect a task for one approved operator.
- Task and command events are auditable.
- Memory contracts are implemented enough for next-phase agent work.
- Specialist agent MVPs are ready to build.
