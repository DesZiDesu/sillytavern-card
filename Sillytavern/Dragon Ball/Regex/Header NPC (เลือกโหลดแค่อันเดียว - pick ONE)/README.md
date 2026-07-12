# Header NPC (imageless) — pick ONE

Fallback nameplate for characters with **no portrait** in `Images/` (Cabba, Launch, Monaka, one-scene NPCs...). Same designs as the main Header folder, portrait removed — **import the variant matching your main header** so both look like one system.

| File | Matches main header |
|---|---|
| `DB_HeaderNPC_A_ScouterHUD_Regex.json` | A — Scouter HUD |
| `DB_HeaderNPC_B_KiNameplate_Regex.json` | B — Ki Nameplate |
| `DB_HeaderNPC_C_DragonBallPlate_Regex.json` | C — Dragon Ball Plate |
| `DB_HeaderNPC_D_BattleCard_Regex.json` | D — Battle Card |

## Tag

```
[DBNPC|Name|#hex|region|power]
```

- **Name** — character name.
- **#hex** — signature color (pick one and keep it consistent for that NPC).
- **region** — short tag line, e.g. `Saiyan of Sadala · U6`.
- **power** — battle power (any string; `???` allowed). May be left empty.

Example: `[DBNPC|Cabba|#7fb8e8|Saiyan of Sadala · U6|98,000,000]`

Same ordering law as `[DBCHAR]`: monologue/narration above it, dialogue below it. ⚠️ Load exactly ONE file from this folder — all four share the `[DBNPC]` tag.
