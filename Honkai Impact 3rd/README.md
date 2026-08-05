# Honkai Impact 3rd — SillyTavern Bot Project

This is the main workspace for building the **Honkai Impact 3rd SillyTavern bot**.

The portrait gallery is only one resource used by the bot; it is not the bot project itself.

## Project structure

- `characters/` — SillyTavern character-card JSON/PNG exports and character-specific source files
- `lorebooks/` — world-info and lorebook JSON files
- `prompts/` — system prompts, scenario prompts, author notes, and reusable prompt fragments
- `assets/` — bot-facing media references, including the HI3 character galleries
- `references/` — research notes and source material used while authoring the bot
- `project.json` — machine-readable project registry

## Portrait resources

The existing portrait utilities remain in [`../hi3-portraits/`](../hi3-portraits/). The bot workspace links to those resources through `assets/galleries/`.

## Status

The workspace structure is ready. Actual character cards, lorebooks, and prompts should be added here as the bot is authored; no persona or lore content has been fabricated automatically.
