# How Many Times Have We Reincarnated? — RPG

A **Game-Master / scenario card** for an endless reincarnation survival RPG.
`{{user}}` and the heroine die and are reborn **together** into a brand-new
world — a different genre every time (mundane, fantasy, sci-fi, horror, and
everything between) — keeping **all memories** across every life. Import
`Card/How Many Times Have We Reincarnated RPG.json`.

> **Heroine name is a placeholder.** She's currently **Nana** — rename her
> freely; she keeps the same name across all lives.

## Premise

- **The cycle:** when either of them dies, both wake in a new world, freshly
  born there. Death just spins the wheel again.
- **Memory persists:** they keep every past life's memories (plus fitted
  knowledge of the new world) and always recognise each other.
- **The heroine** is, at her core, a petite, extremely short, underdeveloped
  otaku shut-in (21) with glasses — that mind rides inside a **random new body**
  every life. She **starts** painfully shy, timid, clueless and courageless, and
  **changes** across the lives depending on what she survives and how `{{user}}`
  leads her. The growth persists (she keeps her memories).
- **Her hidden power, `[Request]`:** she can wish for anything and the world
  quietly grants it through natural-looking "luck" — and she has **no idea it's a
  power**, she just thinks she's lucky.
- **`{{user}}`** can customise a new body each life or keep a default look as an
  anchor she always recognises.
- **Every world is harsh** and, in time, tries to kill them both (usually not
  instantly — the danger builds).
- Each rebirth also gives her **one new fetish/whim** she's curious to try (both
  characters are 21+); she's too shy to act on it early and bolder as she grows.

## Greetings (4)

1. **The First Door** *(default)* — the first death and first rebirth; timid Nana.
2. **We Stopped Counting** — many lives in, a sharper Nana, cyberpunk.
3. **The House Remembers** — folk-horror life 7, a village that won't let you leave.
4. **An Ordinary Tuesday** — a deceptively safe mundane life 3.

## Global-system compatibility

- Greetings use the Global speech-UI tags (`[NPC]`/`[SAY]`/`[THINK]`) with Nana's
  signature colour **`#a06cd5`**, and follow the global placement law.
- Each life opens with a plain-text **Life Record** panel (world · genre · her
  body · `{{user}}`'s body · her whim · danger). A regex to render it into a
  styled panel — and a fuller life/progression tracker — can be added later.
- The lorebook is **embedded** in the card (`data.character_book`) and also shipped
  standalone in `Lorebook/`, linked by name via `extensions.world`.

## Lorebook entries

Core loop (constant), the Life Record format (constant), and keyed entries for
the `[Request]` ability, body randomisation, world generation & themes, the
per-life fetish/whim, `{{user}}`'s role, and Nana's persistent growth arc.

## Files

```
How Many Times Have We Reincarnated RPG/
├── Card/…RPG.json          # chara_card_v3 (lorebook embedded)
├── Lorebook/…[LB].json     # standalone World Info copy
├── Images/                 # base look (glasses, expressions) + 2 example bodies
└── README.md
```

## Notes

- Adult content; **all characters are 21+**.
- Image URLs in the lorebook point at `@main` raw paths, so the reference art
  resolves once this is merged to `main`.
- Not yet built: a Regex/tracker suite (this is the "card + lorebook first" pass).
