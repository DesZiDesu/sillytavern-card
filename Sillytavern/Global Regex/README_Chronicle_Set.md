# Global Chronicle Set

Replacement Global Regex scripts using the final Chronicle Set visual language.

## Import

Disable or delete the older Global speech scripts, then import:

1. `Global_Header.json`
2. `Global_Header_URL.json`
3. `Global_NPC_Header.json`
4. `Global_Monologue.json`
5. `Global_Dialogue.json`

`Global_Chronicle_Set_All.json` contains the same five definitions as one multi-regex import file.

## Tags

```text
[THINK|Name|#HEX|inner thought]
[CHAR|catbox-file.png|Name|#HEX]
[SAY|Name|#HEX|spoken words]
```

Full URL image:

```text
[CHAR|https://example.com/image.jpg|Name|#HEX]
```

NPC without image, with optional role:

```text
[NPC|Name|#HEX|Role]
```

Dialogue remains backward-compatible with the existing Global format:

```text
[SAY|#HEX|spoken words]
```

The named form displays the speaker label; the legacy form renders the same Chronicle record without a label.
