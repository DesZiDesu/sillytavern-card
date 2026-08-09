# Shinobi World Gallery

Repository-backed portrait directory for the optional Shinobi Chronicle UI packs.

Use an exact filename from the gallery binding lorebook:

`[SWCHAR|filename.jpg|Name|#HEX]`

or the metadata form:

`[SWCHAR|filename.jpg|Name|#HEX|Village|Rank]`

The optional Chronicle header resolves the filename from `Sillytavern/Shinobi World/Gallery/<filename>` on the repository `main` branch. The Gallery lorebook contains both English and Thai keywords for every approved character/form and keeps each form-specific filename separate.

Do not put a full URL, Catbox code, or generic `[CHAR]` token in the namespaced `[SWCHAR]` marker. The default Shinobi World header regex remains independent.
