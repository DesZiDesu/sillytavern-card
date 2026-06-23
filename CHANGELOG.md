# Changelog

All notable additions to this repository's cards, lorebooks, and regex are listed here.

## 2026-06-23 — Global: AI / System character block (Jarvis-style, "Neural Mesh")

New global UI for an **artificial-intelligence / system** character the user talks to directly
(a Jarvis / FRIDAY-style assistant) — kept separate from normal NPCs.
- Three new global regex (`Global Regex/`): **`Global • AI Header`** `[AICHAR|Name|#hex]`,
  **`Global • AI Dialogue`** `[AISAY|#hex|text]`, **`Global • AI Monologue`** `[AITHINK|#hex|text]`
  — the same THINK→CHAR→SAY placement law as the normal block.
- **No avatar image**: the header renders an **animated custom SVG "neural mesh" sigil**
  (rotating node-network, pulsing nodes, breathing glow, blinking status, a scan-line sweep),
  a thin wide-spaced name with a glow pulse, dialogue with a fill-in edge + typing caret, and a
  monologue "processing" line with blip dots. Accent colour is driven by the `#hex` (default
  ice-blue `#8fe9ff`), so each AI can have its own colour; same hex across all three tags.
- **Lorebook** (`Global Lorebook/Global System [LB].json`): new constant entry describing the
  AI block with a STRICT "use only for the AI/System being spoken to — never normal NPCs or the
  main character" rule, placement law, and a self-check. (Also synced the file to the latest
  export, which adds the Tracker entry.)

## 2026-06-23 — TRETARESIA RPG: Skill System + tabbed Creation + interactive Mission Board

- **Skill System lorebook entry** (`Lorebook/TR [LB].json`, non-constant, keyed): defines
  Skills as a *blessing* the world mistakes for ordinary magic, sorted by **category, not
  rank** — **Intrinsic · Common · Extra · Unique · Ultimate · Resistance** (Tensura-style).
  Includes how each rank of society misreads them and how to record them (`type` = category in
  the Status `skills` array, Skill Header on use, `<TR_DEV>` on change).
- **Character Forge (`Regex/TR_Creation_Regex.json`) → tabbed**: the long single-scroll form
  is split into **5 tappable tabs** — Identity · Looks · Power · Path · Story — so it no longer
  runs off the screen. BEGIN/RANDOMIZE stay pinned; submitting with no name jumps back to the
  Identity tab. Added **Skill-category presets** to power/skill creation: an Origin-Skill
  category select (defaults Intrinsic) and a category dropdown in the ability adder
  (the six categories + Custom…), stored on each ability (`cat`/`tier`).
- **Mission Board (`Regex/TR_Missions_Regex.json`) → interactive**: postings are now
  **tappable** — tap a paper and it **pulls out** into a full-detail view (full description,
  rank, reward, poster, board, status) with **Accept Mission** and **Exit** buttons. Exit
  returns to the board to browse others. **Accepting** sends a user-side message that renders
  as a personal **"Mission Accepted" contract slip** (new `view:"accepted"` mode in the same
  regex). Taken/closed postings show their stamp and disable Accept.

## 2026-06-20 — Wistoria RPG: Status restyle — pure black, element-coloured, magic-circle crest

- **Pure-black** Status base; the entire accent colour is now **driven by the character's
  magic** — auto-derived from their element (Fire→red, Ice→blue, Wind→green, Lightning→gold,
  Earth→amber, Light→pale, Darkness→violet, Fantasy→teal…), or set explicitly via a new
  `ui_hex` field. (Replaces the fixed gold.)
- **Crest → Magic Circle**: 18 hand-built arcane-sigil designs; the AI picks ONE per
  character via a new `sigil` (1–18) field after creation (auto-assigned from the name if
  omitted). Rendered in the accent colour.
- Updated the Status lorebook schema (`ui_hex`, `sigil`) + a panel-appearance note; synced
  the card, embedded book, and `Regex/WS_Status_Regex.json`.

## 2026-06-20 — Wistoria RPG: new Fantasy Status (build-adaptive) + Learn flow

Replaced the Status window with a brand-new **Fantasy** design (dark arcane tome, gold
filigree, element-tinted), collapsible, EN/TH (Trirong/Cinzel fonts), iPhone-friendly.
- **Build-adaptive Combat Core**: auto-picks **Mageblade · Wis** (magicless/sword, loaded
  element + ~50min hold + reload charges), **Arcane Channel** (mage: mana + element + tier +
  Supreme charge), or **Forge · Artifice** (dwarf/artificer) — and tints to the element.
- **8 tabs**: Overview · Arts · Gear · Bonds · Vitals · Attributes · Quests · Profile,
  covering every build (magicless/mage/multos/elf/dwarf/nightwalker/faculty/graduate).
- **Progression/points**: Academy Credits → Ascent Rank ladder, Aptitude Points, deepest
  floor, Tower stratum.
- **Interactive Arts**: learned arts (mastery bars + element icons) + a **Learnable** list
  whose Learn buttons spend Aptitude Points and **auto-send `[LEARN|name|element|cost]`**;
  added the **WS Learn** banner regex to render that request.
- Gear/Artifices/Items + Familiar, Vitals + Conditions, Bonds/Intimacy, full Profile + Wallet.
- Rewrote the Status lorebook entry with the full schema + adaptive-core + learn-flow rules.
- Exported `Regex/WS_Status_Regex.json` and `Regex/WS_Learn_Regex.json`. Card now ships 10 regex.

## 2026-06-19 — Wistoria RPG: Skill / Spell Label with element icons

- New **`WS Skill Label`** regex: `[SKILL|Name|Element/Type|Tier/Note|#hex]` renders a glowing
  "Incantation Banner" (Design A) at the moment of a cast — diamond glyph + gold corner
  brackets + vertical CAST + hex glow.
- The **icon auto-matches the element** (Fire→flame, Ice/Water→crystal, Wind→swirl,
  Lightning/Thunder→bolt, Earth→peak, Light→sun, Darkness→moon, Fantasy→eye, Wis/Sword→blade;
  EN + TH keywords), via a small script; colour follows the caster's hex.
- Added a constant lorebook entry documenting the tag, the element→icon map, and usage;
  exported `Regex/WS_Skill_Regex.json`. Synced across all stores.

## 2026-06-19 — Wistoria RPG: redesigned headers + speech, new [NPC] nameplate

- **Two header styles.** `[CHAR|img|Name|#hex]` = framed **ID-Plaque** header (portrait,
  serif caps, element diamond, hex double-rule) for named/focal characters; new
  `[NPC|Name|#hex]` = borderless **Nameplate Bar** (no image) for minor/one-off speakers.
- **Dialogue** `[SAY]` set to the **Parchment Scroll** bubble; **Monologue** `[THINK]` set to
  the **Torn Reverie** note. All chosen from a 3-option-per-component design round.
- Added the `WS NPC Header` regex; exported the speech set as standalone regex files
  (`WS_Header_CHAR_Regex.json`, `WS_Header_NPC_Regex.json`, `WS_Dialogue_Regex.json`,
  `WS_Monologue_Regex.json`). Rewrote the Header lorebook entry to document both styles
  and when to use each; synced across all stores.

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

## 2026-06-19 — Jujutsu Kaisen: fill NPC header image list

- **Lorebook** `Lorebook/Jujutsu Kaisen [LB].json` (`NPC LIST [JJK]`) — replaced every
  `[xxxxxx.png]` placeholder in the `<npc_header_list>` with its real catbox image code
  so the JJK Character Header regex renders each NPC's portrait. Existing entry text and
  hex colours were preserved.
- **Added the extra forms/images** supplied alongside the list, each sharing its base
  character's hex colour: Nobara (Shinjuku, eye patch), Gojo (Student Awakened; Teacher
  Unmasked), Maki (First-Year), Toge (First-Year — and the existing entry relabelled
  Second-Year), Yuta (Restored), Nanami (Student), Shoko (Student), Yaga (Teacher),
  Mei Mei (Student), Sukuna (Yuji's Vessel), Toji (Revived), Naoya (Vengeful Spirit),
  and Rika (Shikigami / Cursed Spirit). Added **Kurourushi** as a new entry.
- List now totals **90 entries/forms** (was 74 placeholders).

## 2026-06-13 — Re Zero RPG: remove Return by Death / Quick Reply system

Removed the experimental Return by Death kit at the user's request:
- Deleted `Quick Replies/RZ_ReturnByDeath_QR.json`, `Quick Replies/Return-by-Death
  Setup.md`, `Regex/RZ_Memory_Regex.json`, and `Regex/RZ_ExtractMemory_Regex.json`.
- Reverted the card: dropped the embedded `RZ Loop Memory` / `RZ Extract Memory`
  regex and the `[Return by Death Marker]` output rule. The monologue-spacing fix
  and the `[Player Agency — ABSOLUTE]` rule are kept.

## 2026-06-13 — Re Zero RPG: monologue spacing fix + Return by Death v2

- **RZ Monologue regex:** increased the bubble's vertical margin
  (`12px auto 6px` → `22px auto 36px`) so the THINK bubble's downward tail dots no
  longer collide with the character header below it.
- **Return by Death v2:** loop memory is now **cumulative** (`rbd_log`, one line per
  loop) and the whole log is injected each rewind; after the `/cut` the kit
  re-posts a **persistent Loop Memory panel** (so there is on-screen UI showing
  what happened and which loop you are on); all player-facing button/popup text is
  now Thai. Requires the updated card so the engine emits the `[RZMEM|…]` marker on
  death — without it there is nothing to remember.

## 2026-06-12 — Re Zero RPG: Return by Death kit (Quick Replies + regex)

Added a starter kit that reproduces Subaru's **Return by Death** in SillyTavern:

- **`Sillytavern/Re Zero RPG/Quick Replies/RZ_ReturnByDeath_QR.json`** — a 4-button
  Quick Reply set: 🔖 *Set Save Point*, ☠ *Return by Death* (confirm → bump death
  counter → capture carried-over memory → `/inject` it → `/cut` back to the save
  point), 📖 *Loop Memory*, 🧹 *Clear Memory*.
- **`Sillytavern/Re Zero RPG/Regex/RZ_Memory_Regex.json`** — renders a `[RZMEM|loop|
  save|cause|carried]` marker into a styled "Retained Memory" panel matching the
  card's dark/blood-red aesthetic.
- **`Sillytavern/Re Zero RPG/Quick Replies/Return-by-Death Setup.md`** — install +
  wiring guide. Core idea: the loop memory survives chat deletion because it lives
  in a chat variable + a persistent prompt injection, not in the deleted messages.

**Native memory capture (no extension):** the ☠ button keeps a confirm popup, then
auto-extracts the loop's memory straight from the AI's `[RZMEM|…]` marker via the
in-app `/regex` command (helper script
`Sillytavern/Re Zero RPG/Regex/RZ_ExtractMemory_Regex.json`) — no typing, no
add-ons. A `[Return by Death Marker]` rule was added to the card's
`post_history_instructions` so the engine emits that marker on every death.

STScript flags may need minor per-version tweaks; the regex panels are
version-independent.

## 2026-06-12 — Re Zero RPG: synced to latest + player-agency rule

- **Synced to the latest working state:** updated both
  `Sillytavern/Re Zero RPG/Card/Re Zero RPG.json` and
  `Sillytavern/Re Zero RPG/Lorebook/Re Zero [LB].json` to the newest versions.
- **New `[Player Agency — ABSOLUTE]` rule** added to the card. The narrator and
  every NPC are now strictly forbidden from writing, speaking, narrating, or
  implying {{user}}'s dialogue, actions, gestures, inner thoughts, feelings, or
  decisions, and from leading or deciding what {{user}} says/thinks/does. The
  engine renders only the world, NPCs, and consequences, then yields the turn
  and waits for {{user}}'s own input. The rule lives in the card `description`
  (the active system prompt) and is reinforced in `post_history_instructions`
  so it is enforced every turn, in any mode.
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
