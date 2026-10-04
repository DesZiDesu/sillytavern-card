# Wuthering Waves RPG

Sandbox RPG card with a Thai opening at Jinzhou. The player controls their own character; the bot narrates the world and NPCs.

## Import

1. Import `Lorebook/Wuthering Waves [LB].json` in SillyTavern World Info.
2. Import `Card/Wuthering Waves RPG.json` as a character.
3. Accept the card's character regex scripts when prompted. The card includes **Header A — Resonance Bar**, **Dialogue A — Dialogue Box**, and **Monologue — Echo**, all enabled. Do not also enable another design for the same tags.
4. Confirm the character is linked to **Wuthering Waves [LB]** in World Info, then start a new chat.

The lorebook is supplied separately and is not embedded in the card. `extensions.world` names the lorebook to attach; confirm the link if your SillyTavern version or import settings do not attach it automatically. Enable character regex in SillyTavern if your settings disable it. A model/API connection is still required.

## Speech and portraits

NPC blocks use optional `[WTHINK|Name|#hex|thought]`, then `[WCHAR|filename|Name|#hex|subtitle]`, then `[WSAY|#hex|dialogue]`. The header and dialogue are adjacent; narration stays outside the block. These tags never represent the player.

The three portrait directory entries map all **74 named character/creature filenames** to `Images/<filename>.jpg`, plus `npc.jpg` for unlisted or original NPCs. The 17 Gallery-only assets are also available under Images so existing header designs work without a tag change. Display names and subtitles may be translated; slugs and colours stay fixed. For an unlisted NPC, use `npc`, `#a9b5c8`, and the NPC's own name.

Images load from the repository's direct raw.githubusercontent.com endpoint and require network access. Directory additions are image mappings, not new canon biographies. The player's choice of identity, era and goals overrides the default opening.
