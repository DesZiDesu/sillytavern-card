# Honkai: Star Rail — Regex Interface Kit

A SillyTavern UI kit for Honkai: Star Rail roleplay. It includes character and
NPC headers, dialogue, monologue, narrator styling, the always-visible
**Desolation Chronicle Scene Tracker**, and the collapsible five-tab
**Astral Archive Status Tracker**.

The trackers support English and Thai. Element keywords drive the Status accent
colour automatically.

## Install

1. In SillyTavern, open **Extensions → Regex → Import Regex**.
2. Import `HSR_Scene_Regex.json` and `HSR_Status_Regex.json`.
3. Import any header/dialogue/narrator styles you use.
4. Import both lorebooks:
   - `Lorebook/Honkai Star Rail [LB].json`
   - `Lorebook/Honkai Star Rail Tracker Systems [LB].json`

The Tracker Systems lorebook has high-priority contracts and overrides the older
`hsr_status.v1` instruction contained in the original lorebook.

## Regex depth

Both Scene and Status tracker regexes use `maxDepth: 2`.

## Compact UI tokens

| Component | Token |
|---|---|
| Character header | `[HSRCHAR\|slug\|Name\|element\|path\|faction]` |
| NPC header | `[HSRNPC\|Name\|element\|path\|faction]` |
| Monologue | `[HSRTHINK\|Name\|element\|text]` |
| Dialogue | `[HSRSAY\|Name\|element\|text]` |
| Narrator | `[HSRNARR\|text]` |
| Scene Tracker | `<hsr_scene>{...}</hsr_scene>` |
| Status Tracker | `<hsr_status>{...}</hsr_status>` |

Example:

```text
[HSRCHAR|kafka|Kafka|lightning|nihility|Stellaron Hunters]
[HSRSAY|Kafka|lightning|Everything is proceeding according to the script.]
```

## Scene Tracker

The Scene Tracker must be the absolute first block in every assistant roleplay
response. It remains visible and uses the Desolation Chronicle dark archive
layout. Text wraps inside the UI; mobile screens use a two-column layout rather
than horizontal overflow.

```json
<hsr_scene>
{
  "schema": "hsr_scene.v1",
  "time": "21:35",
  "period": "night",
  "weather": "หิมะโปรย",
  "temperature_c": -8,
  "location": "เขตบริหาร · Belobog",
  "zone": "ทางเดินตะวันตก",
  "situation": "กำลังหลบการลาดตระเวนของ Silvermane Guards"
}
</hsr_scene>
```

Keep the key order unchanged. Preserve previous values unless the scene changes.

## Status Tracker

The Status Tracker must be the absolute final block in every assistant roleplay
response. It uses `hsr_status.v2` and is validated by
`HSR_Status_Schema.json`.

The rendered UI is a native HTML `<details>` panel with no `open` attribute:

- It starts collapsed.
- Tap the summary bar to expand or collapse it.
- Inside the expanded panel, the tabs are:
  `Vitality / Paths / Equipments / Quests / Party`.
- Long names and descriptions wrap inside the panel and are not intentionally
  truncated.
- On narrow screens, content grids become one column.

```json
<hsr_status>
{
  "schema": "hsr_status.v2",
  "lang": "th",
  "character": "Reinhardt",
  "level": 42,
  "vitality": {
    "hp": { "current": 760, "max": 1000 },
    "energy": { "current": 82, "max": 100 },
    "bond": { "current": 64, "max": 100 },
    "conditions": [
      "อ่อนล้าเล็กน้อย",
      "ไม่มีบาดแผลร้ายแรง"
    ]
  },
  "paths": {
    "current": "destruction",
    "element": "quantum",
    "traces": [
      {
        "name": "Fractured Horizon",
        "level": 6,
        "desc": "เพิ่มความเสียหายหลังได้รับการโจมตีโดยตรง"
      }
    ]
  },
  "equipments": {
    "light_cone": {
      "name": "On the Fall of an Aeon",
      "level": 70,
      "superimposition": 2,
      "desc": "Destruction-class amplification"
    },
    "relics": [
      {
        "name": "Genius of Brilliant Stars",
        "slot": "Head",
        "set": "Quantum Set",
        "level": 12,
        "desc": "Quantum damage configuration"
      }
    ],
    "consumables": [
      {
        "name": "Emergency Recovery Kit",
        "qty": 2,
        "desc": "Restores vitality"
      }
    ]
  },
  "quests": [
    {
      "name": "Echoes Beneath Belobog",
      "status": "ongoing",
      "objective": "Recover the missing survey beacon",
      "progress": 68,
      "info": "Avoid the Silvermane patrol"
    }
  ],
  "party": [
    {
      "name": "Reinhardt",
      "role": "Leader",
      "element": "quantum",
      "path": "destruction",
      "hp": { "current": 760, "max": 1000 }
    }
  ]
}
</hsr_status>
```

All five top-level Status sections must remain present. Empty collections should
be `[]`; `light_cone` may be `null`. Preserve state between turns unless events
change it.

## Valid elements

`physical` · `fire` · `ice` · `lightning` · `wind` · `quantum` · `imaginary`

## Valid paths

`destruction` · `hunt` · `erudition` · `harmony` · `nihility` ·
`preservation` · `abundance` · `remembrance` · `elation` · `propagation` ·
`trailblaze`

## Character portraits

The first field in `[HSRCHAR|slug|...]` is the image filename without its
extension. Portraits are loaded from:

`Sillytavern/Honkai Star Rail/Images/<slug>.jpg`

Examples: `march-7th-ice`, `dan-heng`, `kafka`, `trailblazer-fire-f`,
`rin-tohsaka`, `gilgamesh`. If a portrait file is absent, the header remains
usable without the image.
