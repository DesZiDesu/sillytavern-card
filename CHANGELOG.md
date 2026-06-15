# Changelog

All notable additions to this repository's cards, lorebooks, and regex are listed here.

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
