# Dragon Ball — Status HUD (`DB_Status_Regex.json`)

A collapsible, Xenoverse-style fighter HUD for the **player**. Import `DB_Status_Regex.json` into SillyTavern's Regex (it renders inside a fenced code block as a sandboxed iframe, so full CSS/JS work).

## How the AI uses it

Emit a single tag containing a **JSON object**. The HUD renders from it:

```
<DB_STATUS>{ ...json... }</DB_STATUS>
```

- Starts **collapsed** as a thin bar (name · mini HP/Ki · power); tap to expand.
- Tabs: **Profile · Vitality · Skills · Items**, plus **Missions** — which only appears when `missions` is a non-empty array.
- Any omitted field is hidden automatically. Keep numbers as `[current, max]` pairs.

## JSON schema

```jsonc
{
  "name": "Kaen",                       // fighter name (thin bar + header)
  "title": "Saiyan Fighter · Earth",    // small subtitle (optional)
  "power": "1,200,000",                 // battle power — any string: number, "∞ ???", "Immeasurable"
  "level": 24,                          // optional
  "race": "Saiyan",
  "age": 24,
  "gender": "Male",
  "alignment": "Chaotic Good",
  "race_ability": "<b>Zenkai Boost</b> — ... <b>Oozaru</b> — ...",  // <b>…</b> allowed for emphasis
  "origin": "Short backstory line.",

  "hp":      [6800, 10000],             // [current, max]
  "stamina": [4100, 9000],
  "ki":      [7500, 8000],              // rendered as a stock-block gauge
  "ki_stocks": 6,                       // how many blocks the Ki gauge shows (default 6)

  "injuries": ["Fractured left arm — moderate", "Ki exhaustion — mild"],  // [] = "Unharmed."
  "status":   ["Zenkai primed"],

  "forms": [                            // transformation progression (angular nodes)
    { "n": "Base",           "tier": "×1",   "state": "unlocked" },
    { "n": "Super Saiyan",   "tier": "×50",  "state": "active"   },  // one 'active' = current form
    { "n": "Super Saiyan 2", "tier": "×100", "state": "locked"   }
  ],                                    // state: "active" | "unlocked" | "locked"

  "techniques": [
    { "n": "Kamehameha", "d": "Signature ki wave", "c": "1,500 Ki" }  // d/c optional
  ],
  "passives": ["Saiyan Pride", "Combat Genius"],

  "items": [
    { "n": "Senzu Bean", "q": 2 },      // q = quantity (default 1)
    { "n": "Scouter",    "q": 1 }
  ],
  "zeni": "45,000",

  "missions": [                         // OMIT or [] and the Missions tab disappears
    {
      "name": "The Saiyan Threat",
      "rank": "A",                      // small badge (optional)
      "desc": "Raditz has landed on Earth...",
      "objectives": [
        { "t": "Locate Raditz's pod", "done": true },
        { "t": "Defeat Raditz", "done": false, "prog": "0/1" }  // prog optional
      ],
      "rewards": ["8,000 Zeni", "Senzu Bean ×1", "+50,000 Power"]
    }
  ]
}
```

## Notes
- The tag is **`DB_STATUS`** — unique to Dragon Ball, no collision with other cards' status tags.
- Post it whenever the player's state changes (after a fight, a transformation, gaining/spending items, accepting or progressing a mission).
- Objectives flip to a struck-through cyan check when `"done": true`.
