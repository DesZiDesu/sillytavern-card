# Honkai Impact 3rd — SillyTavern Bot Project

This is the main workspace for building the **Honkai Impact 3rd SillyTavern bot**.

## Project structure

- characters/ — SillyTavern character cards and source data
- lorebooks/ — world-info and lorebook JSON files
- prompts/ — reusable prompts and author notes
- regex/ — importable SillyTavern message UI Regex scripts
- previews/ — PC, mobile, and responsive UI previews
- assets/ — UI portraits and shared bot-facing media
- references/ — canon and terminology research
- project.json — machine-readable project registry

## Gallery

The Character Header uses the real repository gallery in Gallery/. Use an exact gallery filename stem in the HI3CHAR marker, for example:

[HI3CHAR|040_Herrscher_of_Flamescion_(Avatar)|Kiana Kaslana|psy|Herrscher of Flamescion|Schicksal · Hyperion]

The gallery URL is the primary image source. Legacy assets/ui/portraits/ stems remain a fallback for older markers.

## Message UI — Valkyrja Operations V3

Install regex/HI3_Message_UI_V3_Package.json once to import the four-entry package:

- Character Header with gallery portrait
- NPC Header without portrait
- Dialogue — Voice Link
- Monologue — Cognitive Trace

The V3 language uses light command surfaces, clipped data plates, cyan/magenta rails, gold type accents, and a dark cognitive surface for monologue.

## Status

The message UI package is at V3. First Message, Personality, and Scenario fields remain pending.
