---
name: Test Python CLI
description: Run the fast Python verification suite and focused CLI tests for WhatsApp Chat Exporter.
---

# Test Python CLI

Use this when changing parser behavior, console entry points, exporters, or documentation that describes CLI behavior.

## Focused CLI checks

```bash
python -m pytest tests/test_agent_cli.py -q
```

## Fast suite

```bash
python -m pytest -q --ignore=tests/test_nuitka_binary.py
```

## Full release-level suite

Install Nuitka first, then run:

```bash
python -m pytest -q
```

## Pitfalls

- Use `python -m pytest`, not bare `pytest`.
- Do not commit generated exports, media, local backup files, debug logs, or standalone binaries.
- Manifest commands must stay banner-free and JSON-only on stdout when `--json` is used.
