#!/usr/bin/env python3
"""Generate self-contained Honkai: Star Rail RPG cards.

This temporary maintenance script consolidates the two HSR lorebooks, removes the
obsolete hsr_status.v1 contract, embeds the complete lorebook into each Chara
Card V3 file, and attaches one coordinated UI regex set per card.
"""

from __future__ import annotations

import copy
import json
import re
from pathlib import Path
from typing import Any, Iterable

REPO = Path(__file__).resolve().parents[2]
HSR = REPO / "Sillytavern" / "Honkai Star Rail"
LORE_DIR = HSR / "Lorebook"
REGEX_DIR = HSR / "Regex"
BOT_DIR = HSR / "Bot"
VARIANT_DIR = BOT_DIR / "Variants"

MAIN_LORE_PATH = LORE_DIR / "Honkai Star Rail [LB].json"
TRACKER_LORE_PATH = LORE_DIR / "Honkai Star Rail Tracker Systems [LB].json"
BASE_CARD_PATH = BOT_DIR / "Honkai Star Rail RPG.json"

RAW_IMAGE_ROOT = (
    "https://raw.githubusercontent.com/DesZiDesu/sillytavern-card/main/"
    "Sillytavern/Honkai%20Star%20Rail/Images/"
)
FALLBACK_IMAGE_ROOT = (
    "https://rawcdn.githack.com/DesZiDesu/sillytavern-card/main/"
    "Sillytavern/Honkai%20Star%20Rail/Images/"
)

APPROVED_FIRST_MESSAGE = r'''<hsr_scene>
{"schema":"hsr_scene.v1","time":"06:17","period":"dawn","weather":"station-wide emergency lockdown","temperature_c":17,"location":"Herta Space Station","zone":"Sealed Research Wing · Containment Corridor C-12","situation":"The Antimatter Legion has breached the station. March 7th and Dan Heng have discovered {{user}} inside an unauthorized containment chamber while an unknown signal is transmitting from deeper within the sealed wing."}
</hsr_scene>

Red emergency lights sweep across the corridor in slow, mechanical intervals.

Beyond the reinforced observation window, fragments of the station drift against a field of distant stars. Every few seconds, the structure shudders under another impact. Warning sirens overlap with the clipped voice of the station’s evacuation system:

“Containment failure detected. Research Wing C will be sealed in four minutes.”

The chamber behind {{user}} is unlike the standard medical pods used throughout Herta Space Station. Its casing is made from black alloy marked with faded geometric symbols, and every identification field on the nearby terminal has been deliberately erased.

Only one line remains active:

SUBJECT RECORD: NOT FOUND  
ORIGIN: UNRESOLVED  
STELLARON RESONANCE: DETECTED

A damaged security drone lies motionless near the doorway. Scorch marks cut across the floor, leading toward a sealed laboratory at the far end of the corridor. Something inside that room is still transmitting—a weak, repeating signal that matches the rhythm of the containment chamber.

[HSRTHINK|March 7th|ice|No records, a sealed research pod, and Stellaron readings during an invasion... This is exactly how terrible adventures begin.]

[HSRCHAR|march-7th-ice|March 7th|ice|preservation|Astral Express]
[HSRSAY|March 7th|ice|Okay, mysterious stranger—good news first. You’re alive. Bad news: the station is under attack, this entire wing is about to lock down, and that machine behind you says you’re connected to a Stellaron somehow.]

March keeps her bow raised toward the dark laboratory, but her attention repeatedly returns to {{user}}. Her expression is cautious rather than hostile.

Beside her, Dan Heng examines the terminal with his cloud-piercer spear held low and ready. The station map on its screen flickers between three unstable routes.

[HSRCHAR|dan-heng|Dan Heng|wind|hunt|Astral Express]
[HSRSAY|Dan Heng|wind|There is no registered experiment matching this chamber. Someone removed the records before the attack began. That means your presence here may not be an accident.]

A heavy impact strikes somewhere above the corridor.

The sealed laboratory door buckles outward.

For a moment, a narrow gap opens between the metal panels. A pale blue light shines through it, followed by a distorted transmission:

“...subject awake... recovery protocol incomplete... do not allow the Express crew to leave with—”

The message cuts off.

March turns sharply toward the door.

[HSRCHAR|march-7th-ice|March 7th|ice|preservation|Astral Express]
[HSRSAY|March 7th|ice|That definitely sounded suspicious. We can head for the Master Control Zone, force that laboratory open, or check the maintenance passage for survivors—but we need to decide before this corridor seals.]

Dan Heng steps away from the terminal and faces {{user}} directly.

[HSRCHAR|dan-heng|Dan Heng|wind|hunt|Astral Express]
[HSRSAY|Dan Heng|wind|You are the only person here whose biometric signature can unlock that laboratory. The choice is yours. Come with us to safety, investigate the signal, or search for anyone trapped in this wing.]

The countdown above the blast door changes.

03:41  
03:40  
03:39

<hsr_status>
{"schema":"hsr_status.v2","lang":"en","character":"{{user}}","level":1,"vitality":{"hp":{"current":100,"max":100},"energy":{"current":20,"max":100},"bond":{"current":0,"max":100},"conditions":["Identity records missing","Weak Stellaron resonance detected","Recently released from containment","No critical injuries detected"]},"paths":{"current":"trailblaze","element":"physical","traces":[]},"equipments":{"light_cone":null,"relics":[],"consumables":[]},"quests":[{"name":"The Empty Record","status":"ongoing","objective":"Choose whether to evacuate with the Astral Express crew, investigate the sealed laboratory, or search the maintenance passage for survivors","progress":5,"info":"Research Wing C will be permanently sealed in less than four minutes. An unknown transmission appears connected to {{user}}."}],"party":[{"name":"{{user}}","role":"Unidentified containment subject","element":"physical","path":"trailblaze","hp":{"current":100,"max":100}},{"name":"March 7th","role":"Defensive support","element":"ice","path":"preservation","hp":{"current":920,"max":920}},{"name":"Dan Heng","role":"Reconnaissance and frontline combat","element":"wind","path":"hunt","hp":{"current":870,"max":870}}]}
</hsr_status>'''

UI_GUIDE = f'''ATTACHED UI AND GITHUB PORTRAIT GUIDE — this card is self-contained.

The card embeds the complete Honkai: Star Rail lorebook and exactly five regex scripts: Scene Tracker, one Header design, one Monologue design, one Dialogue design, and Status Tracker. Do not import the separate Tracker Systems lorebook; it has been consolidated into this lorebook. Do not use Narrator/Narrative UI yet.

OUTPUT ORDER:
1. Absolute first: <hsr_scene>{{valid hsr_scene.v1 JSON}}</hsr_scene>
2. Plain scene prose when needed.
3. Optional NPC thought: [HSRTHINK|Name|element|thought]
4. NPC portrait header: [HSRCHAR|slug|Name|element|path|faction]
5. Spoken line: [HSRSAY|Name|element|words]
6. Absolute final: <hsr_status>{{valid hsr_status.v2 JSON}}</hsr_status>

HEADER PORTRAITS:
The attached Header regex loads character portraits directly from the GitHub gallery. The primary URL pattern is:
{RAW_IMAGE_ROOT}<slug>.jpg
The fallback URL pattern is:
{FALLBACK_IMAGE_ROOT}<slug>.jpg

The slug must exactly match a JPG filename in Sillytavern/Honkai Star Rail/Images. Examples used by the approved first message:
[HSRCHAR|march-7th-ice|March 7th|ice|preservation|Astral Express]
[HSRCHAR|dan-heng|Dan Heng|wind|hunt|Astral Express]
Other verified examples:
[HSRCHAR|rin-tohsaka|Rin Tohsaka|quantum|erudition|Fate/Star Rail Night]
[HSRCHAR|gilgamesh|Gilgamesh|lightning|destruction|Fate/Star Rail Night]
[HSRCHAR|archer|Archer|fire|hunt|Fate/Star Rail Night]

Valid element slugs: physical, fire, ice, lightning, wind, quantum, imaginary. Never attribute HSRTHINK, HSRCHAR, or HSRSAY to {{user}}. Preserve all scene and status values unless events change them.'''


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def iter_regex_json() -> Iterable[tuple[Path, dict[str, Any]]]:
    for path in REGEX_DIR.rglob("*.json"):
        try:
            data = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(data, dict) and isinstance(data.get("scriptName"), str):
            yield path, data


def find_regex(*, filenames: tuple[str, ...], script_terms: tuple[str, ...]) -> dict[str, Any]:
    for name in filenames:
        matches = list(REGEX_DIR.rglob(name))
        if len(matches) == 1:
            return load_json(matches[0])
    candidates: list[tuple[Path, dict[str, Any]]] = []
    for path, data in iter_regex_json():
        script_name = data["scriptName"].casefold()
        if all(term.casefold() in script_name for term in script_terms):
            candidates.append((path, data))
    if len(candidates) != 1:
        details = ", ".join(str(p.relative_to(REPO)) for p, _ in candidates)
        raise RuntimeError(f"Could not uniquely locate regex {script_terms!r}; candidates: {details}")
    return candidates[0][1]


def patch_header_gallery(regex_obj: dict[str, Any]) -> dict[str, Any]:
    patched = copy.deepcopy(regex_obj)
    replacement = patched.get("replaceString", "")
    image_tag_pattern = re.compile(r'''src=(["'])([^"']*\$1\.jpg)\1''')
    new_src = (
        f'''src="{RAW_IMAGE_ROOT}$1.jpg" '''
        f'''onerror="this.onerror=null;this.src='{FALLBACK_IMAGE_ROOT}$1.jpg'"'''
    )
    replacement, count = image_tag_pattern.subn(new_src, replacement)
    if count == 0:
        # Handle known relative-path strings even if the tag formatting differs.
        known = (
            "../../Sillytavern/Honkai Star Rail/Images/$1.jpg",
            "../../Sillytavern/Honkai%20Star%20Rail/Images/$1.jpg",
            "../Images/$1.jpg",
        )
        for old in known:
            replacement = replacement.replace(old, f"{RAW_IMAGE_ROOT}$1.jpg")
        if RAW_IMAGE_ROOT not in replacement:
            raise RuntimeError(f"Header regex {patched.get('scriptName')} has no patchable $1.jpg image source")
    patched["replaceString"] = replacement
    patched["scriptName"] = f"{patched.get('scriptName', 'HSR Header')} — GitHub Gallery"
    return patched


def obsolete_tracker_entry(entry: dict[str, Any]) -> bool:
    text = "\n".join(
        str(entry.get(k, "")) for k in ("name", "comment", "content")
    ).casefold()
    return "hsr_status.v1" in text or "scene & status tracker output contract" in text


def make_world_entry(uid: int, name: str, content: str, order: int) -> dict[str, Any]:
    return {
        "uid": uid,
        "key": [],
        "keysecondary": [],
        "comment": name,
        "content": content,
        "constant": True,
        "selective": True,
        "selectiveLogic": 0,
        "order": order,
        "position": 4,
        "disable": False,
        "addMemo": True,
        "excludeRecursion": True,
        "probability": 100,
        "displayIndex": uid,
        "useProbability": True,
        "secondary_keys": [],
        "keys": [],
        "id": uid,
        "priority": 1000,
        "insertion_order": uid,
        "enabled": True,
        "name": name,
        "extensions": {
            "depth": 1,
            "weight": 1000,
            "addMemo": True,
            "displayIndex": uid,
            "useProbability": True,
            "characterFilter": None,
            "excludeRecursion": True,
            "vectorized": False,
            "ignoreBudget": True,
        },
        "case_sensitive": False,
        "depth": 1,
        "characterFilter": None,
        "vectorized": False,
    }


def normalize_worldbook() -> dict[str, Any]:
    main = load_json(MAIN_LORE_PATH)
    tracker = load_json(TRACKER_LORE_PATH)

    retained = [
        copy.deepcopy(entry)
        for entry in main.get("entries", {}).values()
        if not obsolete_tracker_entry(entry)
    ]
    tracker_entries = [copy.deepcopy(entry) for entry in tracker.get("entries", {}).values()]

    # Explicit always-on guide to regex usage and GitHub image slugs.
    guide = make_world_entry(902, "HSR • Attached UI & GitHub Portrait Guide", UI_GUIDE, 9_999_997)

    combined = retained + [guide] + tracker_entries
    combined.sort(key=lambda e: (int(e.get("displayIndex", 0)), int(e.get("uid", 0))))

    # Guarantee unique and stable dictionary keys without changing entry UIDs.
    main["entries"] = {str(index): entry for index, entry in enumerate(combined)}
    main["name"] = "Honkai Star Rail [LB]"
    main["description"] = (
        "Complete Honkai: Star Rail lorebook with canon setting, factions, worlds, "
        "characters, crossover entries, attached-UI instructions, GitHub portrait "
        "slug guidance, and the current hsr_scene.v1 / hsr_status.v2 contracts."
    )
    main["token_budget"] = max(int(main.get("token_budget", 0)), 2048)
    main.setdefault("extensions", {})["world_info_budget"] = max(
        int(main.get("extensions", {}).get("world_info_budget", 0)), 4096
    )
    return main


def to_character_book(worldbook: dict[str, Any]) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for entry in worldbook["entries"].values():
        position_num = int(entry.get("position", 0) or 0)
        entries.append(
            {
                "keys": list(entry.get("keys") or entry.get("key") or []),
                "secondary_keys": list(
                    entry.get("secondary_keys") or entry.get("keysecondary") or []
                ),
                "comment": str(entry.get("comment") or entry.get("name") or ""),
                "content": str(entry.get("content") or ""),
                "constant": bool(entry.get("constant", False)),
                "selective": bool(entry.get("selective", True)),
                "insertion_order": int(
                    entry.get("insertion_order", entry.get("order", 100)) or 100
                ),
                "enabled": bool(entry.get("enabled", not entry.get("disable", False))),
                "position": "before_char" if position_num in (0, 4) else "after_char",
                "use_regex": False,
                "extensions": copy.deepcopy(entry.get("extensions", {})),
            }
        )
    return {
        "name": worldbook["name"],
        "description": worldbook.get("description", ""),
        "scan_depth": int(worldbook.get("scan_depth", 50)),
        "token_budget": int(worldbook.get("token_budget", 2048)),
        "recursive_scanning": bool(worldbook.get("recursive_scanning", False)),
        "extensions": copy.deepcopy(worldbook.get("extensions", {})),
        "entries": entries,
    }


def get_ui_regexes() -> tuple[dict[str, Any], dict[str, Any], dict[str, dict[str, Any]]]:
    scene = find_regex(
        filenames=("HSR_Scene_Regex.json",),
        script_terms=("HSR", "Scene"),
    )
    status = find_regex(
        filenames=("HSR_Status_Regex.json",),
        script_terms=("HSR", "Status"),
    )

    variants: dict[str, dict[str, Any]] = {}
    specifications = {
        "A": {
            "header": (("HSR_Header_A_AstralTicket_Regex.json",), ("Header", "A", "Astral")),
            "monologue": (("HSR_Monologue_A_AstralTicket_Regex.json", "HSR_Monologue_InnerVoice_Regex.json"), ("Monologue", "A")),
            "dialogue": (("HSR_Dialogue_A_AstralTicket_Regex.json", "HSR_Dialogue_Transmission_Regex.json"), ("Dialogue", "A")),
        },
        "B": {
            "header": (("HSR_Header_B_WarpNameplate_Regex.json",), ("Header", "B", "Warp")),
            "monologue": (("HSR_Monologue_B_WarpRecord_Regex.json",), ("Monologue", "B")),
            "dialogue": (("HSR_Dialogue_B_WarpRecord_Regex.json",), ("Dialogue", "B")),
        },
        "C": {
            "header": (("HSR_Header_C_Constellation_Regex.json",), ("Header", "C")),
            "monologue": (("HSR_Monologue_C_DataBank_Regex.json",), ("Monologue", "C")),
            "dialogue": (("HSR_Dialogue_C_DataBank_Regex.json",), ("Dialogue", "C")),
        },
    }
    for key, spec in specifications.items():
        header = find_regex(filenames=spec["header"][0], script_terms=spec["header"][1])
        monologue = find_regex(
            filenames=spec["monologue"][0], script_terms=spec["monologue"][1]
        )
        dialogue = find_regex(
            filenames=spec["dialogue"][0], script_terms=spec["dialogue"][1]
        )
        variants[key] = {
            "header": patch_header_gallery(header),
            "monologue": monologue,
            "dialogue": dialogue,
        }
    return scene, status, variants


def synchronize_legacy_fields(card: dict[str, Any]) -> None:
    data = card["data"]
    for key in (
        "name",
        "description",
        "personality",
        "scenario",
        "first_mes",
        "mes_example",
        "tags",
    ):
        if key in data:
            card[key] = copy.deepcopy(data[key])


def build_card(
    base: dict[str, Any],
    character_book: dict[str, Any],
    scene: dict[str, Any],
    status: dict[str, Any],
    variant_key: str,
    variant: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    card = copy.deepcopy(base)
    label = {
        "A": "UI A — Astral Ticket",
        "B": "UI B — Warp Record",
        "C": "UI C — Data Bank",
    }[variant_key]
    name = "Honkai: Star Rail RPG" if variant_key == "A" else f"Honkai: Star Rail RPG — {label}"

    card["data"]["name"] = name
    card["data"]["first_mes"] = APPROVED_FIRST_MESSAGE
    card["data"]["character_book"] = copy.deepcopy(character_book)
    card["data"].setdefault("extensions", {})["world"] = ""
    card["data"]["extensions"]["regex_scripts"] = [
        copy.deepcopy(scene),
        copy.deepcopy(variant["header"]),
        copy.deepcopy(variant["monologue"]),
        copy.deepcopy(variant["dialogue"]),
        copy.deepcopy(status),
    ]
    card["data"]["creator_notes"] = (
        f"Self-contained {label} edition. The full consolidated HSR lorebook and five "
        "regex scripts are embedded. Header portraits load from the GitHub HSR gallery. "
        "No separate lorebook or regex import is required. Narrator/Narrative is omitted."
    )
    card["creatorcomment"] = card["data"]["creator_notes"]
    card["character_version"] = "2.0"
    card["data"]["character_version"] = "2.0"
    synchronize_legacy_fields(card)
    return card


def validate_card(card: dict[str, Any], variant_key: str, expected_lore_count: int) -> None:
    data = card["data"]
    regexes = data["extensions"]["regex_scripts"]
    if len(regexes) != 5:
        raise AssertionError(f"Variant {variant_key}: expected five regex scripts, got {len(regexes)}")
    if len(data["character_book"]["entries"]) != expected_lore_count:
        raise AssertionError(f"Variant {variant_key}: embedded lorebook count mismatch")
    if "hsr_status.v1" in json.dumps(data["character_book"], ensure_ascii=False).casefold():
        raise AssertionError(f"Variant {variant_key}: obsolete hsr_status.v1 remains")
    header = regexes[1]
    replacement = header.get("replaceString", "")
    if RAW_IMAGE_ROOT not in replacement:
        raise AssertionError(f"Variant {variant_key}: header lacks primary GitHub image root")
    if FALLBACK_IMAGE_ROOT not in replacement:
        raise AssertionError(f"Variant {variant_key}: header lacks fallback GitHub image root")
    first = data["first_mes"]
    for token in (
        "[HSRCHAR|march-7th-ice|March 7th|ice|preservation|Astral Express]",
        "[HSRCHAR|dan-heng|Dan Heng|wind|hunt|Astral Express]",
        "<hsr_scene>",
        "<hsr_status>",
    ):
        if token not in first:
            raise AssertionError(f"Variant {variant_key}: first message missing {token}")


def main() -> None:
    if not (HSR / "Images" / "march-7th-ice.jpg").is_file():
        raise FileNotFoundError("GitHub gallery image march-7th-ice.jpg is missing")
    if not (HSR / "Images" / "dan-heng.jpg").is_file():
        raise FileNotFoundError("GitHub gallery image dan-heng.jpg is missing")

    worldbook = normalize_worldbook()
    character_book = to_character_book(worldbook)
    scene, status, variants = get_ui_regexes()
    base = load_json(BASE_CARD_PATH)

    # Replace the broken two-lorebook setup with one consolidated standalone book.
    write_json(MAIN_LORE_PATH, worldbook)
    if TRACKER_LORE_PATH.exists():
        TRACKER_LORE_PATH.unlink()

    cards = {
        "A": build_card(base, character_book, scene, status, "A", variants["A"]),
        "B": build_card(base, character_book, scene, status, "B", variants["B"]),
        "C": build_card(base, character_book, scene, status, "C", variants["C"]),
    }
    expected_count = len(character_book["entries"])
    for key, card in cards.items():
        validate_card(card, key, expected_count)

    write_json(BASE_CARD_PATH, cards["A"])
    write_json(VARIANT_DIR / "Honkai Star Rail RPG - UI A - Astral Ticket.json", cards["A"])
    write_json(VARIANT_DIR / "Honkai Star Rail RPG - UI B - Warp Record.json", cards["B"])
    write_json(VARIANT_DIR / "Honkai Star Rail RPG - UI C - Data Bank.json", cards["C"])

    readme = f'''# Honkai: Star Rail RPG cards

Each JSON card in this folder is self-contained. It embeds the consolidated **{expected_count}-entry** HSR lorebook and exactly five regex scripts: Scene, one Header, one Monologue, one Dialogue, and Status.

- `Honkai Star Rail RPG.json` — canonical main card using **UI A / Astral Ticket**.
- `Variants/Honkai Star Rail RPG - UI A - Astral Ticket.json` — explicit A copy.
- `Variants/Honkai Star Rail RPG - UI B - Warp Record.json` — coordinated B set.
- `Variants/Honkai Star Rail RPG - UI C - Data Bank.json` — coordinated C set.

Import only one card. Do not separately import `Honkai Star Rail Tracker Systems [LB].json`; that temporary second lorebook was removed and its current v2 contracts were consolidated into the main lorebook.

The Header regex loads portraits from the repository gallery using the slug in `[HSRCHAR|slug|Name|element|path|faction]`. The approved opening uses the verified files `march-7th-ice.jpg` and `dan-heng.jpg`.
'''
    (BOT_DIR / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    # Final structural validation after writing.
    for path in [BASE_CARD_PATH, *sorted(VARIANT_DIR.glob("*.json")), MAIN_LORE_PATH]:
        load_json(path)

    print(
        json.dumps(
            {
                "lore_entries": expected_count,
                "cards": [
                    str(BASE_CARD_PATH.relative_to(REPO)),
                    *[str(p.relative_to(REPO)) for p in sorted(VARIANT_DIR.glob("*.json"))],
                ],
                "tracker_lorebook_removed": not TRACKER_LORE_PATH.exists(),
                "verified_gallery_images": ["march-7th-ice.jpg", "dan-heng.jpg"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
