# Shinobi World — Optional Chronicle Set

Four selectable Chronicle-style UI options for Shinobi World. Import **one option only**.

- A — Chronicle Classic
- B — Illuminated Shinobi
- C — Dark Archive
- D — Scroll Chronicle

These files are isolated from the default Shinobi World Regex. The optional set uses a dedicated `SW` marker namespace, so it does not match the default `[CHAR]`, `[NPC]`, `[SAY]`, or `[THINK]` tags and does not collide with another folder's Global Chronicle scripts.

## Marker contract

Gallery portrait, compact form:
`[SWCHAR|filename.jpg|Name|#HEX]`

Gallery portrait with metadata:
`[SWCHAR|filename.jpg|Name|#HEX|Village|Rank]`

NPC without an exact gallery portrait:
`[SWNPC|Name|#HEX|Role]`

Dialogue:
`[SWSAY|#HEX|spoken words]` or `[SWSAY|Speaker Name|#HEX|spoken words]`

Inner thought:
`[SWTHINK|Name|#HEX|inner thought]`

Keep each marker on its own final line after the prose. The marker is for the Regex renderer and must not be narrated.

## Gallery rules

- The Gallery lorebook is a **constant NPC image registry**, not a keyword-entry lorebook.
- It contains four always-active mapping entries: #1–#50, #51–#100, #101–#150, and #151–#159.
- Read the exact form name → exact filename mapping and copy the filename character-for-character.
- English and Thai aliases are included as reference names; they are not activation keys.
- Use the exact filename from `Sillytavern/Shinobi World/Gallery/` and `Gallery/manifest.json`.
- Match the exact age, era, clothing, village, rank, title, and transformation; do not substitute a generic portrait for another form.
- Never invent a URL, Catbox ID, base64 image, filename, or path.
- If there is no exact binding, use `[SWNPC|Name|#HEX|Role]`.

## Install

1. Keep the default Shinobi Regex and main `Shinobi World [LB]` unchanged.
2. Import one `SW_Chronicle_*_All.json` option.
3. Import `Shinobi World Gallery [LB].json` for the constant NPC image registry.
4. Import `Shinobi_Chronicle_Gallery_Instructions.json` if you want the namespaced output rules as a separate constant instruction entry.
5. Do not import Options A–D together.
