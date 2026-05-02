# Lessons Learnt

Durable repository lessons for agents go here. Keep short-lived task notes out of this file.

- Use `python -m pytest`, not bare `pytest`, to avoid accidentally running under a global Hermes environment instead of the project virtual environment.
- Treat WhatsApp export outputs, backup hash files, media, keys, standalone binaries, and debug logs as private/generated artifacts unless the user explicitly asks to commit them.
