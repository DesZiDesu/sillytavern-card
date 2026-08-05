# Honkai Impact 3rd — SillyTavern Bot Project

This is the main workspace for building the **Honkai Impact 3rd SillyTavern bot**.

## Project structure

- `characters/` — SillyTavern character cards and source data
- `lorebooks/` — world-info and lorebook JSON files
- `prompts/` — reusable prompts and author notes
- `regex/` — importable SillyTavern message UI regex scripts
- `previews/` — PC, mobile, and responsive UI previews
- `assets/` — UI portraits and shared bot-facing media
- `references/` — canon and terminology research
- `project.json` — machine-readable project registry

## Portrait resources

The portrait gallery remains in [`../hi3-portraits/`](../hi3-portraits/) and is linked through `assets/galleries/`.

## Message UI — Valkyrie Command V2

The current UI set uses a HI3-inspired light Valkyrie data language with cyan crystal structure and magenta rails:

- Character Header with portrait
- NPC Header without portrait
- Dialogue — Voice Link
- Monologue — Cognitive Trace

Previews:

- [Responsive review board](previews/hi3_message_ui_preview.html)
- [PC preview](previews/hi3_message_ui_preview_pc.html)
- [Mobile preview](previews/hi3_message_ui_preview_mobile.html)

Token contracts remain unchanged. Narrator and Status UI are still pending.

## Status

The RPG card has a description draft and message UI V2. First Message, Personality, Scenario, Lorebooks, Narrator, and Status UI remain pending.
