# Changelog

All notable additions to this repository's cards, lorebooks, and regex are listed here.

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
