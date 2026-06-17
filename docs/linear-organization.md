# Linear Project Organization

## Workspace Structure

Recommended Linear setup:

- Team: `ExecuBot`
- Project: `ExecuBot Kernel v0.1`
- Roadmap: `Kernel Foundation`
- Cycles: weekly cycles during the first 30 days

## Labels

- `agent:execubot`
- `agent:engineering`
- `agent:product`
- `agent:operations`
- `agent:finance`
- `agent:data`
- `area:architecture`
- `area:docker`
- `area:telegram`
- `area:memory`
- `area:github`
- `area:security`
- `area:observability`
- `type:decision`
- `type:implementation`
- `type:research`
- `type:docs`

## Statuses

- Backlog
- Ready
- In Progress
- Blocked
- Review
- Done

## Milestone Mapping

| Linear Milestone | Repository Reference |
| --- | --- |
| Foundation | `backlog/milestones.md` Milestone 0 |
| Local Kernel Skeleton | `backlog/milestones.md` Milestone 1 |
| Telegram MVP | `backlog/milestones.md` Milestone 2 |
| Memory MVP | `backlog/milestones.md` Milestone 3 |
| Specialist Agent MVPs | `backlog/milestones.md` Milestone 4 |
| Integrations | `backlog/milestones.md` Milestone 5 |
| Alpha Hardening | `backlog/milestones.md` Milestone 6 |

## Issue Template

```text
Title:
Agent:
Area:
Problem:
Expected outcome:
Acceptance criteria:
Dependencies:
Risks:
Artifacts:
```

## First Issues To Create

1. Define command envelope schema.
2. Define task packet schema.
3. Select implementation language and runtime.
4. Build Docker Compose development skeleton.
5. Create local event log prototype.
6. Draft Telegram command authorization policy.
7. Define memory read/write API contracts.
8. Create Engineering Agent MVP spec.
9. Create Product Agent MVP spec.
10. Create observability and audit event schema.
