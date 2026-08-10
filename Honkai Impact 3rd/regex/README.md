# HI3 Message UI — Valkyrja Operations V3

A single-install SillyTavern Regex package for Honkai Impact 3rd conversation rendering.

## Install

Import `HI3_Message_UI_V3_Package.json` once. It contains all four Regex entries:

- Character Header — V3 Valkyrja data surface
- NPC Header — V3 auxiliary contact surface
- Dialogue — V3 voice-link surface
- Monologue — V3 cognitive surface

Do not import both the package and the individual source entries at the same time, or the same marker can be rendered twice.

## Marker contract

`[HI3CHAR|gallery-stem|Name|type|Battlesuit|Faction]`
`[HI3NPC|Name|type|Role|Faction]`
`[HI3SAY|Name|type|text]`
`[HI3THINK|Name|type|text]`

Character Header example:

`[HI3CHAR|040_Herrscher_of_Flamescion_(Avatar)|Kiana Kaslana|psy|Herrscher of Flamescion|Schicksal · Hyperion]`

The first HI3CHAR field is the exact filename stem from `Honkai Impact 3rd/Gallery/`; the Regex appends `.png`. The gallery image is loaded first from:

`Honkai Impact 3rd/Gallery/<gallery-stem>.png`

If an older marker still uses an `assets/ui/portraits/` stem, the header keeps a compatibility fallback after the gallery request fails.

## V3 rendering contract

- One marker per line is recommended.
- `markdownOnly: true`
- `runOnEdit: true`
- placement `[1,2]`
- Character Header is a full-width light V3 data plate with a Gallery portrait.
- NPC Header is a full-width light V3 contact plate and never contains or requests an image.
- Dialogue is a light V3 command surface with a compact voice-link header and relay footer.
- Monologue is the dark V3 cognitive layer with a private-channel footer.
- All panels use the same angular clipped surface, top signal rail, micro-labels, accent chips, and responsive desktop/mobile rules.
- Supported accent types: bio, psy, mech, qua, img, sd, neutral.
- Keep `|` and `]` out of field values.
