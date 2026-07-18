# Quincy — "Secretly Dancer Girlfriend"

A **standalone** SillyTavern character card (not an RPG/simulator). Import
`Card/Quincy.json` into SillyTavern and set her avatar from `Images/`.

## Concept

Quincy (24, half-Japanese / half-foreigner) is a sweet, doujin-literate
internet girl living a double life: a wholesome online personality by day, an
exotic club dancer by night, with a private paid-session / sexting menu on the
side. She never swears, she lives in your DMs, and she shows you everything —
except the one secret she keeps from her "normal" world.

You always **start as her best friend**. Whether you ever uncover her night
life, and whether the friendship becomes something more, unfolds through play.

## Greetings

The card ships with four openings (default + three alternates):

1. **Good-morning text spam** *(default)* — cozy best-friend Quincy.
2. **At the club** — you catch her working and the mask cracks.
3. **Cafe meetup** — wholesome, public, off-the-clock Quincy.
4. **Late-night text** — the lonely girl under the mask.

## Notes

- Adult content; all characters are 24+.
- Her hard limits (no rope bondage / hardcore BDSM; no creampie unless drunk)
  are written into the persona and should be respected in play.
- `Images/Quincy_reference.jpeg` is the visual reference used to build her
  appearance; replace or add a cropped avatar as you like.

## Gallery & lorebook

`Gallery/` holds four portraits, and `Lorebook/Quincy [LB].json` is a World Info
book (auto-linked to the card via `extensions.world`) with:

- **Quincy • Appearance & Portrait Directory (NPC)** — a constant entry: her
  signature colour (`#c86dd7`), `[NPC]`/`[CHAR]` header usage, canonical
  appearance, the "never shows her eyes in 18+ art" face rule, and the portrait
  list.
- **Quincy • Skin Tone (fetish-triggered)** — a keyed entry: her **default skin
  tone is pale/white**, and she only **tans / darkens** when a tanning / dark-skin
  / gyaru fetish is explicitly in play (then she returns to pale afterwards).

Portraits (two skin tones × face-visible / ID-card-censored):

| File | Skin | Face |
|------|------|------|
| `Gallery/Quincy_pale_face.jpeg` | pale (default) | visible |
| `Gallery/Quincy_pale_censored.jpeg` | pale (default) | hidden behind her "Quincy" ID card |
| `Gallery/Quincy_tanned_face.jpeg` | tanned | visible |
| `Gallery/Quincy_tanned_censored.jpeg` | tanned | hidden behind the ID card |

## Files

```
Standalone Card/
└── Quincy/
    ├── Card/Quincy.json          # the character card (chara_card_v3)
    ├── Lorebook/Quincy [LB].json # World Info: portrait directory + skin-tone rule
    ├── Gallery/                  # 4 portraits (pale/tanned × face/censored)
    ├── Images/                   # original reference art
    └── README.md
```
