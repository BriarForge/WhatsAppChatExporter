# WhatsApp Chat Exporter CLI

Command-line interface for headless WhatsApp chat export automation.

## Entry Points

Installed package commands:

```bash
wtsexporter
waexporter
whatsapp-chat-exporter
openclaw-whatsapp-exporter
hermes-whatsapp-exporter
```

`whatsapp-chat-exporter` is the canonical descriptive command. `openclaw-whatsapp-exporter` and `hermes-whatsapp-exporter` are first-party aliases for agent fleets and automation inventories.

## Agent Manifest

OpenClaw and Hermes agents can discover the stable CLI contract without parsing human help text:

```bash
whatsapp-chat-exporter openclaw manifest --json
whatsapp-chat-exporter hermes manifest --json
```

Rules for the manifest command:
- stdout is JSON only when `--json` is present,
- stderr is empty on success,
- no banner, progress bar, logging, filesystem write, network call, or backup access occurs,
- schema is `dev.openclaw.cli-manifest.v1`.

## Version and Help

```bash
whatsapp-chat-exporter --version
whatsapp-chat-exporter --help
```

`--version` is banner-free for scripts.

## Automation Defaults

For agent, CI, or unattended usage:

```bash
whatsapp-chat-exporter --no-banner <device-mode> [inputs] [outputs]
```

Recommended practices:
- pass explicit input paths (`--db`, `--wa`, `--media`, `--backup`) instead of relying on the current directory,
- pass explicit output paths (`--output`, `--json`, `--md`, `--txt`),
- use `--no-html` when only JSON, text, or Markdown is needed,
- avoid `--check-update` and `--check-update-pre` unless network access is intended,
- provide a crypt15 key value explicitly; `--key` without a value can prompt interactively.

## GitHub Markdown Export

Create a repository-ready Markdown folder:

```bash
whatsapp-chat-exporter --no-banner -i --backup "$BACKUP" --no-html --md github-export
```

Output shape:

```text
github-export/
  README.md
  chats/
    ChatName.md
  assets/
    ChatName/
      media-files
```

Markdown image links are repository-relative so GitHub renders copied images in the chat files.

## Exit Codes

The CLI follows standard Python/argparse behavior:
- `0`: success,
- `2`: argument parsing or validation error,
- non-zero exporter-specific values: input, decryption, database, or runtime failure.

## Testing CLI Changes

For parser/manifest changes:

```bash
python -m pytest tests/test_agent_cli.py -q
```

For exporter behavior changes:

```bash
python -m pytest -q --ignore=tests/test_nuitka_binary.py
```

For release/binary changes, run the full suite with Nuitka installed:

```bash
python -m pytest -q
```
