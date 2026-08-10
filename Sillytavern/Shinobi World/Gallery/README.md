# Shinobi World Gallery

Repository-backed portrait directory for the optional Shinobi Chronicle UI packs.

The Gallery now contains **336 exact character/form portraits**: 159 original Gallery images plus 177 approved preview-only images promoted on 2026-08-10.

Use an exact filename from the constant NPC registry lorebook:

`[SWCHAR|filename.jpg|Name|#HEX]`

or the metadata form:

`[SWCHAR|filename.jpg|Name|#HEX|Village|Rank]`

The optional Chronicle header resolves the filename from `Sillytavern/Shinobi World/Gallery/<filename>` on repository `main`. The Gallery lorebook is always active and is split into seven constant 50-item batches, with English and Thai aliases included as reference text—not keyword triggers.

Do not put a full URL, Catbox code, base64 image, or generic `[CHAR]` token in the namespaced `[SWCHAR]` marker. The default Shinobi World header Regex and lorebook remain independent.
