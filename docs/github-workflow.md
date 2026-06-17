# GitHub Workflow Setup

## Branching

- `main`: stable foundation and accepted implementation.
- `feature/<short-name>`: implementation branches.
- `docs/<short-name>`: documentation-only changes.
- `agent/<agent-name>/<task-id>`: future specialist-agent branches.

## Pull Request Rules

- All changes must have a PR.
- PRs should link to a Linear issue when available.
- PRs must include testing or explain why testing is not applicable.
- Agent-generated PRs require human review before merge.
- Changes touching policy, secrets, approval flow, memory writes, or execution permissions require extra scrutiny.

## Initial Checks

The first workflow is intentionally lightweight:

- Validate documentation links where feasible.
- Confirm expected foundation files exist.
- Add Python-specific checks once Milestone 2 service code exists.

## Future Checks

- Unit tests.
- Type checks for Python services.
- Python linting and formatting.
- Alembic migration check.
- Docker image build.
- Compose smoke test.
- Security scan.
- Secret scan.
- Markdown lint.

## PR Template

See `.github/pull_request_template.md`.
