# CLAUDE.md

This file exists for Claude-compatible agents.

Follow these files in order:
1. [AGENTS.md](AGENTS.md)
2. [developers/guidelines/AGENT_WORKFLOW.md](developers/guidelines/AGENT_WORKFLOW.md)
3. [developers/guidelines/CLI.md](developers/guidelines/CLI.md) for CLI behavior, OpenClaw, and Hermes automation contracts
4. [developers/lessons-learnt/general.md](developers/lessons-learnt/general.md) for durable repo memory

If any instruction conflicts, `AGENTS.md` wins.

Repo-specific reminders:
- Use `--no-banner` for automation examples.
- Keep `openclaw manifest --json` and `hermes manifest --json` parseable JSON on stdout.
- Do not commit generated WhatsApp export folders, media, backup database files, debug logs, or local binaries unless explicitly requested.
