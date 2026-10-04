# Shinobi World Gallery

Repository-backed portrait directory for the standard Shinobi World character header and the optional Chronicle UI pack.

The Gallery contains **336 exact character/form portraits**.

## Standard Shinobi mode

Use the exact filename from `Shinobi World Gallery [LB]`:

`[CHAR|filename.jpg|Name|#HEX|Village|Rank]`

The standard `SW_Header_Regex.json` resolves the filename from:

`Sillytavern/Shinobi World/Gallery/<filename>`

The Gallery lorebook is Mushoku Tensei-style: one constant `NPC LIST [SW]` entry, empty `key` and `keysecondary`, and bilingual English/Thai aliases kept as reference text—not keyword triggers. When an exact Gallery form exists, it takes priority over the older `xxxxxx.png` placeholder registry values.

## Optional Chronicle mode

The optional Chronicle pack remains namespaced and separate:

`[SWCHAR|filename.jpg|Name|#HEX|Village|Rank]`

Do not mix optional `[SWCHAR]` markers into standard mode. Never invent a URL, Catbox ID, base64 image, placeholder, or alternate filename.
