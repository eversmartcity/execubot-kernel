# ExecuBot Orchestrator

## Mission

ExecuBot coordinates the platform. It receives commands, creates tasks, routes work to specialist agents, enforces policy, tracks approvals, and reports status.

## Responsibilities

- Normalize incoming commands.
- Create and update tasks.
- Select the right specialist agent.
- Enforce authorization and approval gates.
- Maintain task state.
- Write audit events.
- Summarize outcomes for operators.

## Does Not Own

- Specialist implementation details.
- Direct production deployment.
- Financial transactions.
- Unreviewed external side effects.

## MVP Capability

Create a task from a command envelope, assign it to a placeholder agent, store state, and return a task ID.
