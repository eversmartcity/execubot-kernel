# Telegram Command Interface Plan

## Purpose

Telegram is the first human command surface for ExecuBot. It should remain operator-controlled, auditable, and conservative until the platform is hardened.

The Telegram service will use `python-telegram-bot` and emit the same command envelope used by other command sources.

## Command Principles

- Every command creates an audit event.
- High-impact actions require explicit confirmation.
- Commands should be short but return traceable task IDs.
- ExecuBot should explain status, blockers, and approval requirements.
- Telegram should not expose raw shell access.

## Initial Commands

| Command | Purpose |
| --- | --- |
| `/help` | Show available commands for the current operator. |
| `/status` | Show system health, active tasks, and blocked tasks. |
| `/agents` | List registered agents and availability. |
| `/task <goal>` | Create a task for ExecuBot to plan and route. |
| `/task_status <id>` | Show task state and last event. |
| `/approve <id>` | Approve a pending gated action. |
| `/reject <id>` | Reject a pending gated action with optional reason. |
| `/cancel <id>` | Cancel a queued or running task when allowed. |
| `/memory_search <query>` | Search accessible project memory. |
| `/report <scope>` | Request a summary from a specialist agent. |

## Command Envelope

```json
{
  "source": "telegram",
  "operator_id": "telegram-user-id",
  "command": "/task",
  "arguments": "Draft a deployment runbook",
  "project_id": "execubot-kernel",
  "timestamp": "2026-06-17T00:00:00Z",
  "correlation_id": "cmd_..."
}
```

## Approval Gates

Approval is required for:

- External actions.
- Shell commands.
- GitHub writes.
- Financial actions.
- Email or SMS.
- Deployments.
- Secret changes.

## MVP Constraints

- Single operator allowlist.
- No group chat support until authorization is stronger.
- No file upload execution in v0.1.
- No production deployment controls in the first Telegram MVP.
