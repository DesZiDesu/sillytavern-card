# Dragon Ball — Notify Pop-ups (`DB_Notify_Regex.json`)

Kakarot-style **quest toast** notifications (design B from `Tools/previews/db_notify_options.html`) for when the player **obtains an item**, **unlocks a form**, or **learns a technique**. Import `DB_Notify_Regex.json` into SillyTavern's Regex (it renders inside a fenced code block as a sandboxed iframe, like the status HUD). Installs on its own — no conflict with the speech regex, status HUD, or tracker.

## How the AI uses it

Emit a single tag containing a **JSON array** (a single object also works). One toast renders per entry:

```
<DB_NOTIFY>[ {...}, {...} ]</DB_NOTIFY>
```

## JSON schema

```jsonc
[
  {
    "type": "item",                    // gold "ITEM OBTAINED!" banner
    "name": "Senzu Bean",
    "qty": 2,                          // optional → shown as ×2
    "rarity": "Rare",                  // optional
    "note": "Restores full HP & Ki",   // optional small line
    "to": "Item Pouch"                 // where it's stored → "STORED → ITEM POUCH" (default: Inventory)
  },
  {
    "type": "form",                    // gold "FORM UNLOCKED!" banner + gold mastery bar
    "name": "Super Saiyan",
    "tier": "×50",                     // optional multiplier
    "mastery": 62,                     // 0–100 → meter + "IN TRAINING"; 100 → "MASTERED"
    "note": "Ki drain drops as mastery rises"
  },
  {
    "type": "technique",               // blue "TECHNIQUE LEARNED!" banner + blue mastery bar
    "name": "Kamehameha",
    "cost": "1,500 Ki",                // optional
    "from": "Master Roshi",            // optional teacher/source
    "mastery": 100                     // 100 = MASTERED (green tag)
  }
]
```

## Rules

- **Items never get a meter** — just the green `STORED → …` chip.
- **Forms & techniques** carry `mastery` (0–100). Below 100 the toast shows a segmented XP bar, the % remaining to full mastery, and an `IN TRAINING` chip; at `100` the chip turns green `MASTERED`.
- Omit `mastery` and the toast just says `OBTAINED` with no bar.
- Post the tag **only when something new happens** (picked up an item, first reached a form, learned a technique) or when mastery % meaningfully changes. Batch same-moment events into one array.
- Any omitted field is hidden. Never use raw `<` or `>` inside values.

**Card / Author's Note instruction** — paste this so the AI emits the tag:

> Whenever the player obtains an item, unlocks a transformation, or learns a technique — or a form/technique's mastery % changes — append `<DB_NOTIFY>[ ... ]</DB_NOTIFY>` with one JSON object per event: items `{ "type":"item", "name", "qty", "note", "to" }`; forms `{ "type":"form", "name", "tier", "mastery":0-100, "note" }`; techniques `{ "type":"technique", "name", "cost", "from", "mastery":0-100 }`. `mastery` is % toward full mastery (100 = mastered). Track mastery persistently and raise it gradually through training and battle use.
