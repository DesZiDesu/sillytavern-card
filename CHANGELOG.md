# Changelog

All notable additions to this repository's cards, lorebooks, and regex are listed here.

## 2026-06-19 — Wistoria RPG: Character Forge v3 (auto-send + preset/custom everywhere)

Rebuilt the interactive creation system for `Sillytavern/Wistoria Wand and Sword RPG/`.
- **Auto-send**: "Forge & Send" now writes the `<WS_CONFIRM>` block straight into the chat
  input and submits it (native value-setter + input event, then clicks send) — no manual
  copy-paste. A copy/show-block fallback remains if the host blocks scripted send.
- **Preset + Custom on every field**: each field shows localized preset chips plus a
  ✎ Custom option; option labels switch with the EN/ไทย toggle. Far more options per field.
- **Add Abilities/Skills** (name · type · effect) and **Add Relationships** (name · relation ·
  note) as repeatable lists; **add custom attributes** alongside the 0–10 sliders.
- Still mobile-first (iPhone 13 ≤390px), Thai fonts (Bai Jamjuree/Kanit/Mitr), dark/light.
- Updated the embedded card regex, the standalone `Regex/WS_Creation_Regex.json` &
  `WS_Confirm_Regex.json`, and the creation lorebook entry's field schema.

## 2026-06-16 — Wistoria RPG: brand-new interactive Character Forge

Replaced the simple creation/confirm widgets with a fresh, **interactive, deeply
detailed** character-creation system for `Sillytavern/Wistoria Wand and Sword RPG/`.

- **`WS Creation` (`<WS_CREATE>`)** — the *Character Forge*: a 7-tab interactive form
  (Identity · Appearance · Origin · Arts & Arms · Persona · Bonds · Scene) with text
  inputs, single/multi-select chips, 8 attribute sliders (0–10), toggles, a live
  **completeness meter**, and a **Seal & Copy** button that compiles every field into a
  `<WS_CONFIRM>` block to paste into chat.
- **`WS Confirm` (`<WS_CONFIRM>`)** — a redesigned read-only *sealed registration* sheet,
  sectioned to match the Forge, with attribute bars and a Wis badge.
- **Bilingual EN/TH** with a live language toggle and proper **Thai webfonts**
  (Bai Jamjuree, Kanit, Mitr) alongside Cinzel/Spectral; dark/light theme toggle.
- **Mobile-first / iPhone-13 compatible** (≤390px), 16px inputs (no iOS zoom),
  scrollable tab bar, ≥38px tap targets.
- ~50 fields covering every detail; the creation lorebook entry documents the full schema.
  Designed fresh — not ported from other cards.

## 2026-06-15 — Wistoria: Wand and Sword RPG — Season 2 overhaul (v2.0)

Major expansion of `Sillytavern/Wistoria Wand and Sword RPG/` (both the Card and the
companion `[LB]` lorebook, kept fully in sync across all three content stores).

- **Season 2 content added.** New lore covering the Bloom & Tower-ascent arcs: the
  antagonist organization **the Goetia** (authors of the *Doomsday*), **Baal / the Key
  to the Heavens**, **the Doomsday**, the **eight factions & Tower strata / Guards**, and
  updated entries for the False Sky/Baal, the Magia Vander roster, the Bloom ceremony,
  the Tower, the dungeon/bestiary, organizations (Watchers + **Arbiters**), and the
  arc/publication timeline.
- **Full NPC roster (S1 → present).** The NPC LIST now spans 30 canon characters,
  including the new Season-2 figures **Clairie Serah** (Arbiter High Mage) and **Sarissa
  Alfeld** (Ice-Faction adjutant), plus the Goetia — **Walther Lyndon, Arvin Olus, Shade,
  Marze, Headless, Morta Lattar** — each with a knowledge gate and signature hex colour.
  New per-character lorebook entries were added for all of them.
- **Denser lorebook entries.** Every world/character entry was rewritten longer and
  clearer (no more thin one-liners). **Keywords are now bilingual (TH + EN)**; constant
  entries carry no keywords, as requested.
- **Custom Wistoria-aesthetic UI.** The Tracker, Character Header, Dialogue and Monologue
  regex were redesigned into a cohesive "arcane academy grimoire" look — obsidian-blue
  base, gold + ice-blue accents, ornate gold corner brackets, Cinzel/Spectral serif type
  — matching the existing gold Status panel.
- **No-puppeteering rule.** Added a strict Player-Agency protocol (EN + TH) as a constant
  lorebook entry, in the card's `agency` description block, and in
  `post_history_instructions`: the model must never speak, think, or narrate actions for
  `{{user}}` (ห้ามพูดแทน ห้ามคิดแทน ห้ามบรรยายการกระทำแทน user).

All content remains adult-safe and knowledge-gated to avoid spoiling late reveals.
## 2026-06-18 — KonoSuba RPG (collapsible Skill Tree)

- **Status widget** `Regex/KS_Status_Regex.json` — the always-visible Skill Tree at the
  bottom of the Adventurer Card is now **collapsible**. It starts **collapsed** when the
  card is opened (showing just the "Skill Tree" header + unspent-SP balance + a chevron),
  so the card stays short; tapping the header expands/collapses the category tabs and the
  learnable-skill list. The SP balance stays visible in both states.

## 2026-06-18 — KonoSuba RPG (card cleanup + lorebook speech/header split)

- **Card** `Card/Konosuba RPG.json` — stripped the embedded regex (`extensions.regex_scripts`
  emptied) and removed the embedded lorebook (`character_book`). The card now stays clean
  and relies on the separately-imported regex suite and the standalone `Konosuba [LB]`
  lorebook (the `world` link is retained).
- **Lorebook** `Lorebook/Konosuba [LB].json` — split the two combined interface entries into
  four single-purpose entries so each tag stands alone: **Monologue** `[THINK]`,
  **Dialogue** `[SAY]`, **Header — Framed Avatar** `[CHAR]`, and **Header — Borderless
  Nameplate** `[NPC]`. Each header entry now spells out *when* to use it (`[CHAR]` for
  named/recurring/focal characters, `[NPC]` for minor/one-off/background speakers).

## 2026-06-18 — KonoSuba RPG (card + lorebook + regex suite)

Added a complete new series under `Sillytavern/Konosuba RPG/` — a comedic KonoSuba
isekai RPG built on the same widget architecture as the other RPG cards, themed as a
blue/aqua-and-gold "Adventurer's Card".

**Card** — `Card/Konosuba RPG.json`
- V3 card; narrative-engine prompt (premise, comedic-but-dangerous tone, agency,
  18+ maturity, a mechanics summary, and the full interface-tag contract). First
  message renders the `<KS_CREATE>` registration screen; references the lorebook
  `Konosuba [LB]`.

**Regex (10 scoped scripts)** — `Regex/`
- **Header** `[CHAR|img|Name|#hex]` (framed avatar; image-less NPCs get a tinted
  silhouette) and **Header (no border)** `[NPC|Name|#hex]` (a clean borderless
  nameplate), **Monologue** `[THINK|Name|#hex|thought]`,
  **Dialogue** `[SAY|#hex|words]` — the contiguous speech block.
- **Skill Label** `[SKILL|Skill|Category|SP cost|#hex]` — a skill/spell activation banner.
- **Tracker** `[TRACK|…]` — day, date **with year**, time, arc, region, locale,
  position, weather, temperature, your-position, situation.
- **Status** `<KS_STATUS>{json}</KS_STATUS>` — the Adventurer Card: Level + EXP bar,
  the new **Skill Points** system, Guild rank, attributes (STR/VIT/AGI/DEX/INT/MGC/LUK),
  HP/MP vitals, learned skills (grouped, with SP cost), party, an **Intimacy** tab
  (18+: per-partner relationship stage, affection meter, intimacy level, likes/kinks,
  limits, notes & history), quests, an Eris/debt wallet, and an always-visible
  interactive **Skill Tree** (category tabs + Learn buttons that show Learned /
  Learn·cost / Need-cost states and auto-send a `[LEARN|…]` request to spend points).
- **Learn request** `[LEARN|Skill|Category|cost]` — renders the Skill Tree's auto-sent
  "learn this skill" message as a card; the lorebook tells the model to verify the
  points + a teacher, deduct the cost, add the skill, and re-render the card.
- **Confirm** `<KS_CONFIRM>{json}</KS_CONFIRM>` — the sealed registration card.
- **Creation** `<KS_CREATE>` — a 5-step wizard with **fully free customisation**
  (custom toggle on every field), a **freely adjustable Level** (number + slider) so a
  long-settled local can start high-level and a fresh arrival low, a **Skill-Point budget**
  that derives from level and is spent on a canonical skill/spell catalogue to learn
  starting skills, editable attributes/HP/MP/Eris, a party builder, an isekai
  "blessing/cheat" field, EN/TH language and dark/light theme toggles. On submit it emits
  a `<KS_CONFIRM>` card and auto-sends.

**Lorebook** — `Lorebook/Konosuba [LB].json` (38 entries)
- **Constant system entries (no keywords):** the tag-format instructions (Tracker,
  Header, Speech block, Skill label, Status, Creation flow), core directives, and the
  detailed **game systems** — Adventurers & the Guild, Levels/EXP/**Skill Points**,
  Classes & advancement, Attributes/HP/MP, and the Magic system — plus the NPC LIST with
  fixed hex colours.
- **Keyword entries (Thai + English keys):** world overview; places (Axel, Belzerg
  Capital, Crimson Demon Village, Alcanretia, Elroad, Wiz's shop); factions (Axis Church,
  Eris Church, Demon King's Army); economy (Eris/debt); the Crimson Demon race; a monster
  bestiary; a skills/spells catalogue; and detailed profiles of the cast — Kazuma, Aqua,
  Megumin, Darkness, Wiz, Vanir, Yunyun, Eris/Chris, the supporting cast, Chomusuke/Wolbach,
  and the Demon King & his Generals (Beldia, Hans, Sylvia).

All character content is written for adults (18+). Lore researched against the KonoSuba wiki.

## 2026-06-11 — TR [LB]: new NPC format + new High Elf character

Synced `Sillytavern/TRETARESIA RPG/Lorebook/TR [LB].json` to the latest working
state and reworked the NPC roster:

- **Adopted a new detailed NPC entry format** (Setting / Genres / Role Context →
  Core Details → Backstory → Relationships → Personality & Behavior → Dialogue
  Style → Behavioral & Verbal Examples → During Sex Examples → Intimacy Profile
  → Core Appearance → Outfits). All five existing NPCs — Eswyn Marrowen,
  Lureleth, Kessa Drailen, Meilin, Roun Caelis — were rewritten into this format,
  preserving their established lore, powers, hex colours and hooks.
- **New character: Liriael "Liri" Vaethorn (High Elf)** — a runaway crown-heir of
  the Verdant Court at the World Tree, reincarnated from Earth with fragmentary
  past-life memories, who fled the duty of queenship to live as a free commoner.
  Added as her own entry (uid 57) and as line 6 of the NPC LIST (hex #7FC25A).

All characters are written as adults (18+), consistent with the card's mandate.

## 2026-06-09 — Global Tags & Fetish Lorebook [18+]

Added a new standalone global lorebook: **`Sillytavern/Global Lorebook/Global Tags & Fetish [LB].json`**

A reusable, character-agnostic reference library for tags / fetishes / kinks. Each tag is its **own keyword-triggered entry** (EN + selected TH keys) describing, in detail, what it is, how it is done, what happens, and its effects — so the definition is injected only when that thing actually comes up in play.

**Contents — 131 entries (1 usage header + 130 tags):**
- **Usage header (constant, 18+):** binding rules — all characters are adults, vocabulary-not-a-script, safeword/limits always override, fiction-only devices are roleplay conventions, and a hard exclusion of any minor/childlike content.
- **Oral & Mouth (7):** fellatio, deepthroat, cunnilingus, sixty-nine, facefucking, rimming, sloppy BJ.
- **Penetration & Core Acts (7):** vaginal, anal, creampie/nakadashi, double penetration, mating press, gokkun, facial.
- **Sex Positions (14):** missionary, cowgirl, reverse cowgirl, doggy, prone bone, mating press, spooning, standing, lotus, full nelson, piledriver, amazon, face-sitting, speed bump.
- **Power Exchange & BDSM (12):** D/s, master/mistress, bondage, orgasm control, forced orgasm, pet play, praise, degradation, service submission, brat taming, CNC, chastity.
- **Bondage & Restraint Gear (8):** rope/shibari, handcuffs, spreader bar, gag, blindfold, collar & leash, suspension, bondage furniture.
- **Impact & Sensation (8):** spanking, flogging, nipple play, wax, breath play, biting/marking, electro, tickling.
- **Psychological & Verbal (6):** dirty talk, begging, humiliation, mind break, hypnosis (fiction), corruption.
- **Group & Multiple (6):** threesome, gangbang, orgy, spit-roast, harem, cuckold/cuckquean.
- **Exhibition & Voyeurism (4):** exhibitionism, voyeurism, public sex, recording (fiction).
- **Body & Appearance (6):** breast focus/paizuri, ass focus, thigh job/sumata, foot focus, size difference, lactation.
- **Pregnancy & Breeding (4):** breeding, pregnancy, heat/estrus (fantasy), cum inflation (fantasy).
- **Fantasy & Transformation — adult (8):** monster/beast, tentacles, futanari, succubus/incubus, slime, oviposition, transformation/TG, mind control (fantasy).
- **Messy & Bodily (5):** squirting, bukkake, watersports, drool/spit, sweat.
- **Taboo / Extreme — fiction only (4):** dubcon, somnophilia, free-use, yandere.
- **Sex Toys (15):** vibrator, dildo, strap-on/pegging, butt plug, anal beads, wand massager, remote egg, cock ring, nipple clamps, gag, fleshlight/onahole, sounding, pump, sex machine/sybian, restraint kit.
- **Doujin Tropes & Jargon (16):** ahegao, nakadashi, NTR, netori, heart pupils, cross-section/X-ray, belly bulge, costumes, stockings/zettai ryouiki, body writing, cum marking (fantasy), time stop (fiction), gyaru, ojou-sama, POV, aphrodisiac.

All content is consensual adult (18+) fiction; fiction-only devices are roleplay conventions. No minor/childlike content is included.
