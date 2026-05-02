# .ai/ - Agent Configuration

This folder makes WhatsApp Chat Exporter first-party ready for OpenClaw, Hermes, and IDE-hosted coding agents.

## Structure

```text
.ai/
  instructions.md          # Points to the canonical repo instructions
  skills/                  # Reusable agent playbooks
```

## Usage for agents

1. Read `.ai/instructions.md` first.
2. Follow `AGENTS.md` as the source of truth.
3. Load task-specific skills under `.ai/skills/` when relevant.
4. Use the CLI manifest for automation discovery:

```bash
whatsapp-chat-exporter openclaw manifest --json
whatsapp-chat-exporter hermes manifest --json
```

The manifest is intentionally banner-free JSON on stdout.
