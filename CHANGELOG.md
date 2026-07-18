# Changelog

All notable additions to this repository's cards, lorebooks, and regex are listed here.

## 2026-07-18 — Universal Smartphone lorebook (with in-world time rules)

- **New** `Sillytavern/Universal Smartphone/Lorebook/Phone [LB].json` — the AI-side phone lorebook:
  the unified `<PHONE>` smartphone protocol (schema, screen values, field reference, send-formats)
  plus its companion device systems (Banking, NEXUS social board, modern & Nokia chat messengers,
  phone-call kernel, codex/book reader), each keyed so it loads only when used. Completes the
  Universal Smartphone folder (previously regex-only).
- **In-world time rules**: the lorebook now states that `time`/`date` are the story clock (never the
  real world) and that each `ts` may be a plain in-world `"HH:MM"` (or an ISO 8601 timestamp with an
  in-world date) — matching the roleplay-time regex patch, so phone times stay on story time.

## 2026-07-18 — Global speech placement law reworked; Quincy standalone card + phone user-side UI

- **Global speech UI — new placement law** (`Global Lorebook/Global System [LB].json`, entries
  Monologue / Character Header / Dialogue / NPC Header): a header now **owns everything beneath it
  until the next header**. Order per speaker beat is **[THINK] monologue on top → [CHAR]/[NPC]
  header in the middle → [SAY] dialogue + narrative below**, and the dialogue/narrative may
  alternate freely (SAY → narrative → SAY …) under one header. A new header is printed **only when
  the speaker changes** — no more repeating the header for every line. Only a monologue may sit
  above a header; narration/dialogue above a header is forbidden. **`[CHAR]` (image) and `[NPC]`
  (no-image) headers behave identically** and are cross-referenced.
- **New standalone card** `Standalone Card/Quincy/` — "Secretly Dancer Girlfriend." Default greeting
  renders in the **Universal Smartphone UI** (`<PHONE>` state — a two-sided best-friend text thread);
  the three alternates (Club / Cafe / Late-night) use the Global speech tags and follow the new law.
- **Universal Smartphone user-side UI** (`Sillytavern/Universal Smartphone/Regex/`): new
  `Universal_Smartphone_v2_UserSide.json` renders your own phone actions (chat / social / shop /
  bank / contacts) inside the **same phone frame** as the main regex, using in-world (roleplay)
  time instead of the real-world clock. Main regex lightly patched so pre-send previews match.

## 2026-07-10 — WuWa speech system (header + dialogue + monologue), short-name links

- New **WuWa speech system** (`Wuthering Waves/Regex/`), WuWa-specific tags that don't collide
  with the Global speech block, fully **responsive** (`clamp()` + fluid widths, verified in a
  full multi-turn flow at PC and mobile with no overlap):
  - **Header** `[WCHAR|filename|Name|#hex|element · region]` — **4 designs, pick one**:
    A Resonance Bar (glass + animated equalizer), B Tacet Mark (rotating diamond frame),
    C Gold Plate (cut-corner + element tag), D Minimal Waveform.
  - **Dialogue** `[WSAY|#hex|text]` — **3 designs, pick one**: A Dialogue Box (game-UI tab),
    B Cinematic Subtitle (centered, flank lines), C Tailed Bubble (tail points at the header).
  - **Monologue** `[WTHINK|Name|#hex|text]` — **2 designs, pick one**: Rune Panel (corner
    brackets) · Echo (double-outline). All designs share the same tags, so AI output is identical
    whichever you install.
- **Short filename links**: `[WCHAR]`'s first field is just the image slug (e.g. `changli`) — the
  regex builds the full CDN URL, so the AI never pastes long URLs. Lorebook updated: all 48
  character HEADER lines rewritten to `[WCHAR|slug|…]`, the portrait directory reformatted to
  `Name | filename | #hex | element · region`, and a new constant **WuWa • Speech System** entry
  documents the tags, the short-filename rule and the THINK→WCHAR→WSAY placement law.
- **ZZZ short-name links too**: the four ZZZ header regexes now accept a short filename in field 1
  (`[CHAR|anby|Anby|#hex|faction]`) and build the CDN URL themselves. All 57 ZZZ HEADER lines and
  the 4-part directory rewritten to short filenames; constant entry 255 documents the rule.

## 2026-07-10 — ZZZ wiki image packer + repo reorganization

- New **`Tools/image-tools/zzz_wiki_image_packer.html`** — pulls **official Zenless Zone Zero
  art from the Fandom wiki only** (no boorus): reads the wiki's Agents category, gathers each
  agent's page images (portraits/splash/icons), name-filtered, `/revision/latest` stripped.
  Swipeable per-agent reels with tap-to-select, optional 1:1 640 crop or original PNG, folder
  zips split into ~25 MB parts. Distinct ZZZ lime/orange design — a separate tool, not the WuWa
  packer.
- **Reorganized** every standalone HTML tool out of the repo root into **`Tools/`**:
  `Tools/previews/` (regex-system previews), `Tools/galleries/`, `Tools/mockups/`,
  `Tools/image-tools/` (finders + packers). `index.html` stays at root as a landing page
  linking them. Card content under `Sillytavern/` is untouched.

## 2026-07-10 — WuWa portraits + both lorebooks: link directory, TH keywords, vectorized

- **WuWa official face portraits**: one face-focused official portrait per character (56),
  256px square, in `Wuthering Waves/Images/`. 47 matched characters gained a ready-made
  `[CHAR|url|Name|#hex]` HEADER line in their lorebook entry (signature #hex auto-sampled from
  the portrait); renders via the Global header. Headers verified.
- **Character Portrait Link Directory** (fixes "images don't load — AI doesn't know the URL"):
  new **constant** entries listing every character → portrait URL → signature #hex, so the AI
  always has the exact link in context. ZZZ: 4 parts (59 characters); WuWa: 3 parts (56).
  URLs are sha-pinned rawcdn.githack.
- **EN + TH keywords on every normal entry**: ZZZ — 210 entries gained Thai keywords alongside
  English (WuWa already had them). All non-constant entries in both lorebooks are now
  **vectorized** (green + link icon) for semantic RAG triggering.

## 2026-07-09 — ZZZ: user-side outgoing texts (<ZZZ_SMS>)

The player's own Knock Knock texts now render as phone UI on THEIR side of the chat.
- New regex **`ZZZ SMS (user outgoing texts)`** (`Zenless Zone Zero/Regex/ZZZ_SMS_Regex.json`):
  the player types a plain block — `<ZZZ_SMS>` · optional `to: Name` · one line per message ·
  `</ZZZ_SMS>` — and on send it renders the **mini outgoing panel**: `▸ TO: NAME · KNOCK KNOCK`
  mono header with pulsing send-plane, right-aligned yellow bubbles (pop-in stagger), animated
  **✓ → ✓✓ delivery ticks**, diagonal texture and the lime→orange hairline. No JSON to type;
  Thai/EN friendly; batching = write several lines, send once.
- **Lorebook** (new constant entry uid 256): the tag belongs to the player (AI must never emit
  it); on seeing it the AI treats each line as a sent text and replies with <ZZZ_PHONE> whose
  feed includes those texts as from:"me" with read state — contacts may also leave them unread
  or reply late.
- Preview: `_preview_zzz_sms.html`.

## 2026-07-09 — ZZZ: character header regex — 4 designs, pick one

A ZZZ-specific speech-block header replacing the plain Global • Header in ZZZ chats.
- New folder **`Zenless Zone Zero/Regex/Header (เลือกโหลดแค่อันเดียว - pick ONE)/`** with
  four regex that all match the same 4-field tag `[CHAR|image_url|Name|#hex|faction]` —
  **install exactly one** (README inside, TH):
  **A — Agent File Tag** (skewed frame, halftone dots, lime shadow, italic caps name,
  `// FACTION` mono line, lime→orange hairline) · **B — Knock Knock Contact** (round
  glow-ring avatar, pulsing status dot — matches the phone) · **C — Stripe Banner**
  (full-width skewed black banner, hex border, hazard stripes, blinking cursor) ·
  **D — ZZZ Minimal** (rounded avatar, name in hex, skewed lime faction chip,
  hex→lime hairline). Subtle motion via inline SVG SMIL (sanitizer-safe); inline HTML,
  no iframe. Disable the Global • Header scripts in ZZZ chats (field-count conflict).
- **Images**: all 59 portraits now live in `Zenless Zone Zero/Images/` (self-hosted;
  fetched via the browser packer since the wiki CDN and GitHub Actions were unavailable;
  Nekomata uses user-provided art). Velina Airgid + Norma Hollowell (3.0 Roscaelifer,
  previously missing) added — roster is 57 agents + Wise & Belle.
- **Lorebook**: all 59 HEADER lines rewritten to the 4-field form with each character's
  faction; sha-pinned rawcdn.githack URLs; constant entry (uid 255) updated with the
  4-field rules and setup note.
- Preview: `_preview_zzz_headers.html` (renders all four from the shipped regex).

## 2026-07-08 — ZZZ: character header images for all 55 agents (+ Wise & Belle)

Wiki portrait URLs for the whole 3.1 roster, wired into the lorebook for the [CHAR] header system.
- **Lorebook**: every playable Agent's entry now ends with a ready-made
  `HEADER: [CHAR|<wiki icon URL>|<Name>|<#hex>]` line — 55 entries updated (57 headers: the
  Anby entry also carries Soldier 0 - Anby, the Phaethon entry carries Wise & Belle). Each
  character gets a hand-picked **signature colour** used consistently across [CHAR]/[SAY]/
  [THINK]/<ZZZ_PHONE>/<ZZZ_KNOT>.
- New **constant entry** `ZZZ • Character Header Images` (uid 255): copy the HEADER line
  verbatim when the character speaks; reuse the same URL/hex as phone/forum avatars; minor
  NPCs without a HEADER line use imageless `[NPC]` — never guess URLs.
- Image choice: the wiki's square **`Agent <Full Name> Icon.png`** (the in-game face icon) —
  best fit for the 48px header avatar and round chat avatars. URLs are the stable
  `static.wikia.nocookie.net/...(md5 path)...` form (no `/revision/latest` suffix — that
  URL form is blocked on some networks/content-blockers), derived offline from
  page titles verified against the wiki (incl. `Soldier 0 - Anby`, `Orphie Magnusson & Magus`,
  `Alexandrina Sebastiane`, `Lucia Elowen`, `Yidhari Murphy`, `Komano Manato`,
  `Sigrid de L'Azur`…).
- **Verification gallery** `_gallery_zzz_agents.html`: open in a browser to test-load all 57 —
  tries Icon, auto-falls back to Portrait, badges ICON/PORTRAIT/FAIL, click any card to copy
  its [CHAR] tag. (Couldn't be network-verified from the sandbox; the gallery is the check.)

## 2026-07-08 — ZZZ: four more systems (<ZZZ_STATUS>, <ZZZ_KNOT>, <ZZZ_RESULT>, <ZZZ_TV>)

Completes the ZZZ system set alongside the Knock Knock phone. All four are JSON-payload iframe
regex in the same ZZZ lime/orange industrial style, EN/TH labels via `ui_lang`, avatars/images
via catbox code or URL, and each is documented by a constant lorebook entry (uids 251–254).
- **`ZZZ Status (Proxy HUD)`** (`Regex/ZZZ_Status_Regex.json`): `<ZZZ_STATUS>{json}</ZZZ_STATUS>`
  scene tracker — the game's 5-phase **time bar** (morning/noon/afternoon/evening/midnight),
  location, **Dennies** (auto comma), active commission with progress bar, party avatar row,
  **trust change chips** (▲/▼) and a note line. Omitted fields hide their tiles.
- **`ZZZ Inter-Knot Post`** (`Regex/ZZZ_InterKnot_Regex.json`): `<ZZZ_KNOT>{json}</ZZZ_KNOT>`
  anonymous-board post card — poster with avatar (**anonymous → paper-bag icon**, also the
  broken-image fallback), title, body, image, tag chips, likes, HOT/PINNED badges, optional
  **attached-commission banner** (reward + rank + VIEW), reply thread with `me:true` → lime
  name + YOU chip for Phaethon.
- **`ZZZ Commission Result`** (`Regex/ZZZ_Result_Regex.json`): `<ZZZ_RESULT>{json}</ZZZ_RESULT>`
  the Commission Complete screen — animated stamp banner (red **FAILED** variant, dimmed
  rewards), skewed **rank badge** (S gold · A orange · B blue · C/D gray) with halftone burst,
  objectives checklist with BONUS chips, rewards grid, note line.
- **`ZZZ TV Mode (HDD)`** (`Regex/ZZZ_TV_Regex.json`): `<ZZZ_TV>{json}</ZZZ_TV>` Hollow
  exploration — a wall of static **CRT TVs** with one lit event screen (turn-on flicker,
  scanlines, type-coloured glow), ~14 built-in SVG event icons, dim icons on surrounding TVs
  via `grid`, console text line with blinking caret, **Eous** corner marker and skewed choice
  buttons.
- Previews: `_preview_zzz_status.html`, `_preview_zzz_knot.html`, `_preview_zzz_result.html`,
  `_preview_zzz_tv.html`.

## 2026-07-08 — ZZZ: Knock Knock phone chat (<ZZZ_PHONE>)

The in-game Inter-Knot messenger for Zenless Zone Zero, rendered as an animated phone.
- New regex **`ZZZ Phone (Knock Knock)`** (`Zenless Zone Zero/Regex/ZZZ_Phone_Regex.json`):
  `<ZZZ_PHONE>{json}</ZZZ_PHONE>` renders a **game-authentic Knock Knock replica** — phone frame
  with status bar (clock/battery), app header with the contact's round avatar, name and
  online / offline / **typing…** status, ZZZ lime/orange accent chrome, and the chat feed:
  agents' white bubbles on the left with circular avatars, {{user}}'s light-yellow bubbles on
  the right with **✓/✓✓ read ticks**, per-message times, day dividers, centered system lines,
  an animated typing bubble and a fake input bar.
- **Tap-to-open Agent Profile**: tapping the header or any avatar opens the contact's profile
  page inside the phone — big avatar with signature-colour ring, faction chip, Inter-Knot ID,
  signature quote and a skewed **Trust** bar (`trust`/`trust_max`).
- **Stickers & images**: messages can be an image (`img`) or a sticker (`sticker`) — 4 built-in
  SVG bangboo stickers (`bangboo`, `bangboo_love`, `bangboo_shock`, `bangboo_sad`) or any
  catbox code / URL. Avatars use the same catbox-code-or-URL convention as the Global headers
  (missing avatar → coloured initial). Light **group-chat** support via per-message
  `name`/`avatar`/`hex` overrides.
- **EN/TH labels** via `ui_lang` (online/typing/read/placeholder/profile labels), Thai glyphs
  via Noto Sans Thai. Iframe render like MT Letter / AI Alert.
- **Lorebook** (`Zenless Zone Zero/Lorebook/…world_info.json`, new constant entry uid 250):
  documents the full JSON schema, the "phone chats only — face-to-face speech keeps the normal
  [THINK]/[CHAR]/[SAY] blocks" rule, re-render-the-whole-feed behaviour, stickers, and an example.
- Preview: `_preview_zzz_phone.html`.

## 2026-06-23 — Global: imageless NPC header ([NPC])

- New regex **`Global • NPC Header (no image)`** (`Global Regex/Global_NPC_Header.json`):
  `[NPC|Name|#hex|role]` renders a clean, **imageless** character header — the name in the
  character's signature colour followed by a trailing colour hairline (section-header style),
  with an optional role line beneath (no avatar, no border box, no leading marker). A drop-in
  replacement for `[CHAR]` in the speech block (same THINK→header→SAY law) for NPCs without
  art. `role` is optional (`[NPC|Name|#hex]` works and collapses with no gap). Inline-HTML like
  the other normal-character globals (no iframe).
- **Lorebook** (`Global Lorebook/Global System [LB].json`): new constant entry documenting the
  tag, the "use instead of [CHAR] when there's no image; not for the AI/System" rule, and an
  example.

## 2026-06-23 — Global: AI Alert / Notification system (<AI_ALERT>, "Transmission Stack")

A JSON-driven notification feed for the AI/System character (modelled on TRETARESIA's
`<TR_DEV>` card), letting the AI surface essentially anything to the user.
- New regex **`Global • AI Alert`** (`Global Regex/Global_AI_Alert.json`):
  `<AI_ALERT>{json}</AI_ALERT>` renders the **interactive "Transmission Stack"** — one
  focused holographic card at a time with a peeking stack, dot pager and ‹ › counter to
  browse. **Tap-to-open**: each card opens its detail, and a **message / comms** card opens
  into a readable **chat-bubble reader** (sender avatar + full text + Reply / Mark read).
- 11 alert **categories** (message · comms · detection · intel · system · warning · reminder ·
  transaction · social · task · location) each with its own SVG icon, and 5 **priorities**
  (info/normal/high/critical/success) driving the accent colour. Header colour follows the
  AI's `hex` (matches its `[AICHAR]`). EN/TH labels via `ui_lang`; empty-feed state handled.
- **Lorebook** (`Global Lorebook/Global System [LB].json`): new constant entry documenting the
  full schema, categories, priorities, the "use only for the AI/System being spoken to" rule,
  and an example.
## 2026-06-23 — Global: nudge the dialogue bubble down

- **`Global • Dialogue`** (`Global Regex/Global_Dialogue.json`): increased the `[SAY]` bubble's
  top margin (8px → 16px) so it sits a little lower beneath the header. Visual-only tweak.

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

## 2026-06-22 — Wistoria RPG: responsive widgets + Monologue fix

- **All regex widgets are now responsive**: outer containers use width:100% + box-sizing
  with a 720px cap, so they fill the chat column on phones and scale up on wide screens
  (no more fixed-narrow boxes / overflow).
- **Fixed the Monologue** ([THINK]): the old "Torn Reverie" drew a dashed underline under
  every wrapped line (looked broken). Redesigned to a clean note — name + a single dashed
  flourish, then plain italic thought text. Applied to the card + WS_Monologue_Regex.json.
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
