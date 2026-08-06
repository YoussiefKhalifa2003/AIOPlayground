# AIOPlayground

Demo target repo for **[AIO](https://github.com/YoussiefKhalifa2003)** — the LAN hybrid workplace app.

This repository is intentionally small. AIO points `GITHUB_REPO` here so board cards moved to **agent_backlog** can open sample pull requests against a real GitHub project without touching the main AIO codebase.

## What this is for

- Practice / demo GitHub PRs from AIO
- Safe place for agent-generated PR descriptions and branches
- Not the AIO application itself

## Linked from AIO

In AIO’s `.env` (local only, never commit secrets):

```env
GITHUB_REPO=YoussiefKhalifa2003/AIOPlayground
GITHUB_TOKEN=…   # fine-grained or classic token with repo access
```

Then in AIO: **Board** → drag a card to **agent_backlog** → coding job may open a PR on this repo.

## Notes

- Keep this repo non-empty (`main` must exist) so PR creation works.
- Treat agent PRs as demos — review before merging.
