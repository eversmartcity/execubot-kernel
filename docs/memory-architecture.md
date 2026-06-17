# Memory Architecture Plan

## Goals

- Give agents useful context without unbounded access.
- Separate ephemeral task context from durable project knowledge.
- Keep writes auditable and reversible where possible.
- Support retrieval by task, project, agent, and semantic query.

## Memory Layers

| Layer | Lifetime | Storage Candidate | Examples |
| --- | --- | --- | --- |
| Working Memory | One task/run | Redis Streams and short-lived worker state | Current plan, tool output summaries, active approvals |
| Session Memory | Conversation/task thread | PostgreSQL | Command history, task state, short summaries |
| Project Memory | Long-lived | PostgreSQL | Decisions, runbooks, architecture notes |
| Semantic Memory | Long-lived | PostgreSQL with `pgvector` later | Embedded docs, prior task summaries, research |
| Audit Memory | Immutable or append-only | PostgreSQL `audit_events` table | Commands, routing decisions, approvals, errors |

## Memory API Responsibilities

- `write_event`: append an immutable event.
- `write_summary`: store a human-readable task or decision summary.
- `search`: retrieve relevant memories under policy.
- `get_task_context`: assemble context for an agent run.
- `promote_memory`: move reviewed content from task/session memory into project memory.
- `redact_memory`: mark sensitive or invalid memory as unavailable.

## Access Policy

| Agent | Default Access |
| --- | --- |
| ExecuBot | Full task, routing, policy, and audit context. |
| Engineering Agent | Engineering tasks, repo context, implementation decisions. |
| Product Agent | Requirements, roadmap, user decisions, backlog. |
| Operations Agent | Runbooks, incidents, deployment and health context. |
| Finance Agent | Cost records, budget notes, vendor metadata. |
| Data Agent | Analytics definitions, schemas, memory indexes. |

## Write Policy

- Agents can propose durable memory writes.
- ExecuBot validates and tags writes.
- Sensitive content is redacted before semantic indexing.
- Important decisions are stored as structured decision records.
- Audit events are append-only.
- Milestone 2 implements the initial append-only `audit_events` table.
- `pgvector` is deferred until the Memory MVP.

## Future Schema Concepts

- `tasks`
- `task_events`
- `agent_runs`
- `agent_registry`
- `memory_documents`
- `memory_chunks`
- `decisions`
- `approvals`
- `artifacts`
