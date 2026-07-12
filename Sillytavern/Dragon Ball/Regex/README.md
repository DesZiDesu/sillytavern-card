# Dragon Ball — Regex Systems

Per-message styling + a player status HUD for SillyTavern, like the ZZZ / Wuthering Waves / Wistoria systems. All tags are **Dragon-Ball-specific** so they never collide with the Global / ZZZ / WuWa regex.

## Files

| File | What it does | Tag |
|---|---|---|
| `Header / Dialogue / Monologue / Narrator` folders | Per-message speech styling (install ONE per folder) | `[DBCHAR] [DBSAY] [DBTHINK] [DBNARR]` |
| `DB_Status_Regex.json` | Collapsible Xenoverse-style **player status HUD** (Profile · Vitality · Skills · Items · Missions) | `<DB_STATUS>{json}</DB_STATUS>` |

The status HUD is documented in **`DB_Status_SCHEMA.md`** (full JSON schema). It always installs on its own — it doesn't conflict with the speech regex.

---

## Speech System

Per-message header / dialogue / monologue styling. Tags are **Dragon-Ball-specific** (`[DBCHAR] [DBSAY] [DBTHINK] [DBNARR]`).

## ⚠️ Install ONE file per folder — one at a time

There are 4 folders. Import **exactly one** `.json` from each (4 files total). Every file in a folder shares the same tag, so loading two would double-render. **Download / import one at a time.**

| Folder | Pick one | Tag |
|---|---|---|
| Header | A Scouter · B Ki Nameplate · C Dragon Ball Plate · D Battle Card | `[DBCHAR]` |
| Dialogue | A Manga Bubble · B Battle Subtitle · C Impact Bubble | `[DBSAY]` |
| Character Monologue | A Manga Thought · B Battle Thought | `[DBTHINK]` |
| Narrator | A Manga Caption · B Battle Caption | `[DBNARR]` |

**Tip:** Manga designs (A) share one look; Battle designs (B) share another. Mix within a family for a cohesive result.

## Tags

```
[DBCHAR|path|Name|#hex|region|power]     header (nameplate)
[DBSAY|Name|#hex|text]                   spoken dialogue
[DBTHINK|Name|#hex|text]                 a character's inner thought
[DBNARR|text]                            scene narration (no character)
```

- **path** — the character image under `Images/`, **without** `.jpg`. e.g. `son_goku_super/06_super_saiyan_blue`, `vegeta_super/04_super_saiyan_blue`, `beerus/03_serious`. (See `../FORMS.md` / `Images/_manifest.json` for every path.)
- **#hex** — the character's signature color, e.g. `#c62828` (Goku red), `#6a7bff` (Vegeta blue).
- **region** — a short tag line, e.g. `Super Saiyan Blue · Saiyan`, `God of Destruction · U7`.
- **power** — optional power level: a number (`150,000,000`), `∞ ???`, `Immeasurable`, etc. Shown as `PWR …`.
- Dialogue / thought **text** may span multiple lines.

## Ordering law

> **Monologue and Narrator render ABOVE the header. Dialogue renders BELOW the header.**

A full turn reads top-to-bottom:

```
[DBTHINK|Vegeta|#6a7bff|So he wants to test me…]      ← inner thought (above)
[DBCHAR|vegeta_super/04_super_saiyan_blue|Vegeta|#6a7bff|Super Saiyan Blue · Saiyan|2.5 Billion]
[DBSAY|Vegeta|#6a7bff|Don't get cocky, Kakarot.]      ← spoken line (below)
```

Images are served from the repo's `main` branch via githack, so any committed portrait resolves automatically.
