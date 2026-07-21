# Scars of Summer — Ryoka (countryside childhood-friend summer)

A **standalone** SillyTavern scenario card (not an RPG/simulator). A fan
roleplay adaptation of the Shinachiku-castella / Kagura Games title *Scars of
Summer* (夏色のコワレモノ). Import `Card/Scars of Summer.json` into SillyTavern and
set the avatar from `Images/` or `Gallery/`.

## Concept

Due to family circumstances, **{{user}} takes the protagonist's role (Keita)**
and returns to spend the summer in the sleepy rural hometown he left years ago.
Waiting there is his childhood friend **Ryoka (18)** — a sweet, chill, airheaded
girl who's naive, ditzy and gullible, openly thrilled he's back, trusts him
completely and is easily led. Over one hot, cicada-loud summer their old bond
rekindles into a dizzy first crush, first love and, at {{user}}'s pace, into
something physical.

The heroine is **Ryoka**; the card is titled after the scenario (matching this
repo's other scenario cards), and Ryoka speaks through the Global speech UI
headers.

## Greetings (four starting routes)

The card ships with a default opening plus three alternates — each drops you
into a different moment of the same summer:

1. **Arrival** *(default)* — the sweet, bubbly reunion at the unmanned station.
2. **The Coffee Shop** — catch her flustered on the phone mid-shift.
3. **Summer Festival** — yukata, fireworks, and a resurfacing childhood promise.
4. **Storm Night** — a blackout, one futon, and she trustingly cuddles up (heated route).

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

- **Ryoka • Appearance, Portrait Directory & Image Usage Law** *(constant)* —
  signature colour, canonical appearance, how to emit an image
  (`[CHAR|url|Ryoka|#2f6fb0]` or inline `![Ryoka](url)`), and the **image-gating
  law** (match art to the current situation; at most one per reply; NTR art is
  hard-forbidden outside an NTR route).
- **Scars of Summer • Town & Season** *(keyed)* — the rural summer setting and
  the "scar" theme (the childhood promise).
- **Ryoka • Outfits & the swimsuit habit** *(keyed)* — uniform / café / yukata /
  home, and the competitive swimsuit she hides under her blouse.
- **Ryoka • Pool / swim / wet images** *(keyed: pool, swim, wet…)* — poolside
  swimsuit art, default-route safe.
- **Ryoka • Intimate / climax images** *(keyed: creampie, climax…)* — explicit
  {{user}} afterglow art, for explicit {{user}} scenes only.
- **Ryoka • NTR / corruption images** *(keyed: ntr, cheat, corruption…)* —
  third-party art matching the source game's darker routes, **hard-gated** and
  forbidden in the default sweet romance.

## Progression tracker (visible state system)

Ryoka **changes over the summer**, and you can watch it happen. A status panel
renders at the top of every reply — driven by the embedded **`SoS • Ryoka
Tracker`** regex — showing five meters plus her current stage, day, outfit, mood,
and a "what changed" note:

| Meter | Meaning |
|-------|---------|
| **Affection** | how much she likes / loves you |
| **Trust** | how safe and open she feels |
| **Desire** | physical wanting in the moment (fast, fluctuates by scene) |
| **Guard** | her caution/wariness — starts **low** (she's trusting and easily led), rarely rises |
| **Corruption** | stays `0` in the faithful romance; only moves on an NTR route |

The model emits a `[RYOKA|stage|day|affection|trust|desire|guard|corruption|outfit|mood|note]`
line and the regex turns it into the meter card. **Values move slowly and only
in response to your actions** — kindness, patience and remembering things lower
her guard and raise affection/trust; pushing too fast or being careless cools
her and pushes the guard back up. She progresses through stages:

`Sweet Reunion → Close & Cozy → Smitten → First Love → Lovers → Head-over-heels`

…and the current stage drives how she behaves *and* gates the art: the
intimate/climax images only unlock at **First Love+** inside an explicit scene,
and the NTR imagery only in an NTR route where corruption is rising. The rules
live in the constant **Ryoka • Progression Tracker** lorebook entry.

The regex is **embedded in the card** (so it just works on import) and also
shipped as `Regex/SoS_RyokaTracker_Regex.json`. If the panel ever shows as raw
`[RYOKA|…]` text, import that regex file (or enable character-scoped regex).

## Reference-image gallery (situationally gated)

The lorebook doubles as an **image directory** the AI can pull from mid-chat, so
Ryoka's art surfaces only when the scene matches. `Full-body reference` and
`café` are always safe; everything else is keyed to a context:

| File | Situation | Gate |
|------|-----------|------|
| `Ryoka_cafe.jpeg` | default / café / uniform | any route |
| `Ryoka_dakimakura.jpeg` | full-body reference | any route |
| `Ryoka_pool_wet_blouse.jpg` | wet blouse over swimsuit, poolside | pool/swim |
| `Ryoka_pool_swimsuit_peel.jpg` | peeling her swimsuit down (solo) | pool/swim |
| `Ryoka_climax_creampie_1.jpg` | explicit afterglow (POV) | explicit {{user}} climax |
| `Ryoka_climax_creampie_2.jpg` | explicit afterglow, variant | explicit {{user}} climax |
| `Ryoka_ntr_photo_blackmail.jpg` | photographed / exposed | **NTR route only** |
| `Ryoka_ntr_public_grope.jpg` | groped in public by an older man | **NTR route only** |
| `Ryoka_ntr_interracial_1.jpg` | interracial NTR, before | **NTR route only** |
| `Ryoka_ntr_interracial_2_cum.jpg` | interracial NTR, after | **NTR route only** |
| `Ryoka_ntr_bound_group.jpg` | bound group / gangbang | **NTR route only** |
| `Ryoka_ntr_bikini_mating.jpg` | bikini mating-press | **NTR route only** |
| `Ryoka_ntr_futon.jpg` | affair on a futon | **NTR route only** |

The gating law is the constant portrait entry; the model shows **at most one
image per reply** and only when the scene truly matches. NTR images depict Ryoka
with third parties and **never** appear in the default childhood-friend romance.

## Files

```
Standalone Card/
└── Scars of Summer/
    ├── Card/Scars of Summer.json     # the character card (chara_card_v3)
    ├── Lorebook/Scars of Summer [LB].json  # standalone copy of the embedded World Info
    ├── Regex/SoS_RyokaTracker_Regex.json   # progression-tracker renderer (also embedded)
    ├── Gallery/                      # 13 reference images, served via @main raw URLs
    │   ├── Ryoka_cafe.jpeg           # default portrait ([CHAR] header)
    │   ├── Ryoka_dakimakura.jpeg     # full-body reference
    │   ├── Ryoka_pool_*.jpg          # pool/swim (2)
    │   ├── Ryoka_climax_*.jpg        # explicit {{user}} climax (2)
    │   └── Ryoka_ntr_*.jpg           # gated NTR/corruption (7)
    ├── Images/Ryoka_reference.jpeg   # visual reference used to build her
    └── README.md
```

## Notes

- Adult content; **all characters are 18+**. Ryoka (Enomoto Ryouka) is a legal
  adult (18).
- In the **default** routes {{user}} is the sole love interest — the four
  starting greetings branch across *moments* of the same {{user}}×Ryoka summer.
  The NTR/corruption art is provided (the source game is an NTR title) but is
  **gated** to explicit NTR/corruption play and never bleeds into the sweet route.
- Large source files were downscaled (long edge ≤ 1920 px) for chat-friendly
  loading; originals were up to 22 MB.
- Art reference: Shinachiku-castella (source-game illustrations).
