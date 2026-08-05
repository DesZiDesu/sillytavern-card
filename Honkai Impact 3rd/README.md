# Honkai Impact 3rd — SillyTavern Bot Project

This is the main workspace for building the **Honkai Impact 3rd SillyTavern bot**.

The portrait gallery is only one resource used by the bot; it is not the bot project itself.

## Project structure

- `characters/` — SillyTavern character-card JSON/PNG exports and character-specific source files
- `lorebooks/` — world-info and lorebook JSON files
- `prompts/` — system prompts, scenario prompts, author notes, and reusable prompt fragments
- `regex/` — importable SillyTavern message UI regex scripts
- `previews/` — browser previews used to review UI components before card integration
- `assets/` — bot-facing media references, including UI portraits and the HI3 character galleries
- `references/` — research notes and source material used while authoring the bot
- `project.json` — machine-readable project registry

## Portrait resources

The existing portrait utilities remain in [`../hi3-portraits/`](../hi3-portraits/). The bot workspace links to those resources through `assets/galleries/`.

## Message UI

The first **Hyperion Tactical Interface** set is available under `regex/` and includes:

- Character Header with portrait
- NPC Header without portrait
- Dialogue
- Monologue

Review the complete responsive layout in [`previews/hi3_message_ui_preview.html`](previews/hi3_message_ui_preview.html). Narrator and Status UI are intentionally not included yet.

## Status

The RPG card has a description draft and the initial message UI kit. First Message, Personality, Scenario, Lorebooks, Narrator, and Status UI remain pending.
