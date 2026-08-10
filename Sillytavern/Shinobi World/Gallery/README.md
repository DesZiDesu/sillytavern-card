# Shinobi World Gallery

Repository-backed portrait directory for the optional Shinobi Chronicle UI packs.

## Constant NPC image registry

The Gallery lorebook is intentionally a **constant NPC registry**, not a keyword-triggered image-entry list. It is split into four always-active entries:

- Characters #1–#50
- Characters #51–#100
- Characters #101–#150
- Characters #151–#159

Each item maps an exact character/form name to one exact repository filename:

`Exact Character/Form Name — exact-filename.jpg`

The entries also show English and Thai aliases as reference names. They are not activation keys and do not need to be matched before the image can be used. `Gallery/manifest.json` remains authoritative for filenames and file paths.

## Chronicle output

Use:

`[SWCHAR|filename.jpg|Name|#HEX]`

or:

`[SWCHAR|filename.jpg|Name|#HEX|Village|Rank]`

The optional Chronicle header resolves the filename from `Sillytavern/Shinobi World/Gallery/<filename>` on the repository `main` branch.

If no exact form exists, use `[SWNPC|Name|#HEX|Role]` without an image. Do not put a full URL, Catbox code, base64 data, or a generic `[CHAR]` token in the namespaced `[SWCHAR]` marker. The default Shinobi World header regex remains independent.
