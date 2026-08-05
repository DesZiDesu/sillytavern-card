# HI3 Message UI — Hyperion Tactical Interface

Initial SillyTavern regex UI kit for the Honkai Impact 3rd RPG card.

## Components

- Character Header with portrait: `[HI3CHAR|slug|Name|type|Battlesuit|Faction]`
- NPC Header without portrait: `[HI3NPC|Name|type|Role|Faction]`
- Dialogue: `[HI3SAY|Name|type|text]`
- Monologue: `[HI3THINK|Name|type|text]`

## Type keywords

Use lowercase: `bio`, `psy`, `mech`, `qua`, `img`, `sd`, or `neutral`.

## Portrait path

Character Header loads portraits from:

`Honkai Impact 3rd/assets/ui/portraits/<slug>.png`

The initial preview includes:

- `herrscher-of-flamescion.png`
- `herrscher-of-truth.png`

Additional gallery portraits can be materialized into this folder later without changing the regex token contract.

## Import

Import all four JSON files into SillyTavern regex scripts. Each file is standalone and contains its own fonts and CSS. No narrator or status component is included in this version.

## Preview

Open `../previews/hi3_message_ui_preview.html` through GitHub Pages or RawGitHack.
