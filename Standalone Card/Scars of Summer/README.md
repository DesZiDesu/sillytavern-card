# Scars of Summer — Ryoka (countryside childhood-friend summer)

A **standalone** SillyTavern scenario card (not an RPG/simulator). A fan
roleplay adaptation of the Shinachiku-castella / Kagura Games title *Scars of
Summer* (夏色のコワレモノ). Import `Card/Scars of Summer.json` into SillyTavern and
set the avatar from `Images/` or `Gallery/`.

## Concept

Due to family circumstances, **{{user}} takes the protagonist's role (Keita)**
and returns to spend the summer in the sleepy rural hometown he left years ago.
Waiting there is his childhood friend **Ryoka (18)** — prickly and standoffish
on the surface, lonely and painfully soft underneath, and secretly overjoyed
he's back. Over one hot, cicada-loud summer their old bond rekindles into first
love and, at {{user}}'s pace, into something physical.

The heroine is **Ryoka**; the card is titled after the scenario (matching this
repo's other scenario cards), and Ryoka speaks through the Global speech UI
headers.

## Greetings (four starting routes)

The card ships with a default opening plus three alternates — each drops you
into a different moment of the same summer:

1. **Arrival** *(default)* — the prickly reunion at the unmanned station.
2. **The Coffee Shop** — catch her flustered on the phone mid-shift.
3. **Summer Festival** — yukata, fireworks, and a resurfacing childhood promise.
4. **Storm Night** — a blackout, one futon, and the mask fully down (heated route).

## Global system compatibility

Built for the repo's **Global Regex + Global Lorebook** set:

- Greetings use the Global speech UI tags — `[CHAR|url|Ryoka|#2f6fb0]` (image
  header) and `[NPC|Ryoka|#2f6fb0|subtitle]` (imageless), `[SAY|#2f6fb0|…]`
  dialogue bubbles, and `[THINK|Ryoka|#2f6fb0|…]` monologues — and follow the
  global placement law (monologue on top, header in the middle, dialogue +
  narrative below).
- Signature colour: **`#2f6fb0`** (summer navy-blue).
- The portrait/setting lorebook is **embedded in the card**
  (`data.character_book`) so it travels on import, and is also linked by name via
  `extensions.world` (`Scars of Summer [LB]`) so it sits alongside the Global
  Lorebook without conflict.

## Lorebook entries

- **Ryoka • Appearance & Portrait Directory** *(constant)* — signature colour,
  canonical appearance, and the `[CHAR]` image-header URLs (served from this repo
  under `@main`).
- **Scars of Summer • Town & Season** *(keyed)* — the rural summer setting and
  the "scar" theme (the childhood promise).
- **Ryoka • Outfits & the swimsuit habit** *(keyed)* — uniform / café / yukata /
  home, and the competitive swimsuit she hides under her blouse.

## Files

```
Standalone Card/
└── Scars of Summer/
    ├── Card/Scars of Summer.json     # the character card (chara_card_v3)
    ├── Lorebook/Scars of Summer [LB].json  # standalone copy of the embedded World Info
    ├── Gallery/                      # portraits served for the [CHAR] header
    │   ├── Ryoka_cafe.jpeg
    │   └── Ryoka_dakimakura.jpeg
    ├── Images/Ryoka_reference.jpeg   # visual reference used to build her
    └── README.md
```

## Notes

- Adult content; **all characters are 18+**. Ryoka is a legal adult (18).
- {{user}} is the sole love interest — the branching is across *starting moments*
  of the same {{user}}×Ryoka summer, not toward other partners.
- Art reference: Shinachiku-castella (source-game illustrations).
