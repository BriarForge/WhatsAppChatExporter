# WhatsApp Chat Exporter Agent Instructions

> Single source of truth for OpenClaw, Hermes, Claude, Codex, Copilot, and other coding agents working in this repository. Compatibility files should point here instead of restating policy.

## Critical Instructions

1. **CLI Integrity**
   - Keep the CLI headless and automation-safe. Do not introduce GUI prompts or network calls unless guarded by explicit flags.
   - Preserve these console entry points: `wtsexporter`, `waexporter`, `whatsapp-chat-exporter`, `openclaw-whatsapp-exporter`, and `hermes-whatsapp-exporter`.
   - Keep `openclaw manifest --json` and `hermes manifest --json` machine-readable and free of banner/progress/log noise.
   - Use `--no-banner` in examples meant for agents, CI, OpenClaw, or Hermes.

2. **Verification**
   - Before committing code changes, run:
     ```bash
     python -m pytest -q --ignore=tests/test_nuitka_binary.py
     ```
   - For release/binary changes, also run the full test suite, including `tests/test_nuitka_binary.py`, with Nuitka installed.
   - Use `python -m pytest`, not bare `pytest`, so the project virtual environment is used.

3. **Python Packaging**
   - CLI entry points live in `pyproject.toml` under `[project.scripts]`.
   - Any CLI behavior change must update tests and, when user-visible, `README.md` or `developers/guidelines/CLI.md`.
   - Do not commit generated exports, local iOS backup files, standalone binaries, debug logs, or media artifacts unless explicitly requested.

4. **Agent Workflow**
   - Plan before non-trivial changes.
   - Use sub-agents/workers for large, parallel, or context-heavy work when the host supports them.
   - Keep shared workflow rules in `developers/guidelines/AGENT_WORKFLOW.md` and keep agent-specific files thin.
   - Record durable repo lessons in `developers/lessons-learnt/general.md`.

5. **Git Workflow**
   - Stage only intentional source, test, and documentation files. Never use blind `git add .` when generated export artifacts are present.
   - Use concise Conventional Commit messages unless the user asks for a different format.
   - Push only after verification passes and the user has asked to proceed.

## Documentation Index

- CLI reference: `developers/guidelines/CLI.md`
- Shared agent workflow: `developers/guidelines/AGENT_WORKFLOW.md`
- Lessons learnt: `developers/lessons-learnt/general.md`
- OpenClaw/Hermes manifest: `whatsapp-chat-exporter openclaw manifest --json`
