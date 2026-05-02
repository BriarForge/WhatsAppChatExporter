# Universal Agent Workflow

This document adapts a cross-agent workflow to WhatsApp Chat Exporter. It is written for any coding agent: OpenClaw, Hermes, Claude, Codex, Copilot, Cursor, Windsurf, or similar tools. Agent-specific entry files should point here instead of duplicating policy.

## 1. Plan Before Coding

For non-trivial work, start by identifying:
- intended user-visible behavior,
- files likely to change,
- tests that should fail first,
- verification commands,
- generated artifacts that must not be committed.

## 2. Use Sub-Agents for Large Work

Delegate bounded side work when the host supports sub-agents and the task is large, multi-step, parallelizable, or context-heavy.

Good delegation boundaries:
- CLI parser and packaging metadata,
- exporters and data-model behavior,
- tests and fixtures,
- documentation and agent instructions,
- release/binary packaging.

The coordinating agent owns scope, integration, final verification, and the final git diff.

Each delegated task should return:
- concise summary,
- files changed or inspected,
- commands run and results,
- assumptions and risks,
- recommended next step.

Never have two agents editing the same file at the same time.

## 3. Protect User Data and Generated Artifacts

WhatsApp exports can contain private messages, contact data, media, backup databases, and encryption material. Do not commit or paste user data. Do not commit generated export folders, media files, local backup hashes, keys, binaries, or debug logs unless explicitly requested.

## 4. Verify Before Claiming Completion

Run focused tests first, then the fast suite:

```bash
python -m pytest -q --ignore=tests/test_nuitka_binary.py
```

For release/binary work, install Nuitka and run:

```bash
python -m pytest -q
```

Report skipped full-binary verification explicitly if it was not run.

## 5. Keep CLI Automation Stable

- Keep `--version` machine-readable and banner-free.
- Keep `openclaw manifest --json` and `hermes manifest --json` strict JSON on stdout.
- Use `--no-banner` for automation examples.
- Document network side effects and interactive prompts.
- Update `developers/guidelines/CLI.md` when CLI behavior changes.

## Learned Rules

Store durable lessons in `developers/lessons-learnt/general.md`. Update `AGENTS.md` only when a lesson becomes repository-wide policy.
