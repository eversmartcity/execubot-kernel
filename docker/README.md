# Docker Planning

This directory contains the development environment plan for ExecuBot Kernel.

The current Compose file is a placeholder. Milestone 1 should replace placeholder services with concrete images after the runtime, framework, and queue choices are finalized.

## Planned Commands

```powershell
docker compose -f docker/docker-compose.dev.yml up --build
docker compose -f docker/docker-compose.dev.yml down
```

## First Concrete Services

- `postgres`
- `redis`
- `execubot-api`
- `execubot-worker`
