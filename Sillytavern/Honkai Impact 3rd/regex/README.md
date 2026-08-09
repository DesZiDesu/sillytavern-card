# HI3 Message UI — Valkyrie Command V2

A responsive SillyTavern regex UI set inspired by Honkai Impact 3rd menu and Valkyrie data presentation.

## Tokens

- `[HI3CHAR|slug|Name|type|Battlesuit|Faction]`
- `[HI3NPC|Name|type|Role|Faction]`
- `[HI3SAY|Name|type|text]`
- `[HI3THINK|Name|type|text]`

Supported type accents: `bio`, `psy`, `mech`, `qua`, `img`, `sd`, `neutral`.

## Design V2

- Light translucent Valkyrie data plates instead of the previous dark tactical panels.
- Cyan crystal structure with magenta secondary rails.
- Distinct light Dialogue and dark Monologue surfaces.
- Responsive reduction of secondary telemetry on screens below 560 px.
- Existing tokens and regex IDs are preserved for drop-in replacement.

## Preview

- `../previews/hi3_message_ui_preview.html` — responsive comparison board.
- `../previews/hi3_message_ui_preview_pc.html` — PC layout.
- `../previews/hi3_message_ui_preview_mobile.html` — 390 px mobile layout.
