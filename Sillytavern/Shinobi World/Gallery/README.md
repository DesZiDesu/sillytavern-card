# Shinobi World Gallery

Repository-backed portrait directory for the optional Shinobi Chronicle UI packs.

Use a bare filename in the existing `[CHAR]` image slot, for example:

`[CHAR|sasuke.png|Sasuke Uchiha|#6f71a8|Jōnin|Konohagakure]`

The Chronicle header resolves that filename from `Sillytavern/Shinobi World/Gallery/<filename>` on the repository `main` branch.

Do not put a full URL in the Chronicle `[CHAR]` tag. Add the actual image file to this folder first. The existing default Shinobi World header regexes are unchanged.
