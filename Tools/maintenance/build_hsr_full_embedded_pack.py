#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import subprocess
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HSR = ROOT / "Sillytavern" / "Honkai Star Rail"
OUT = ROOT / "generated-hsr-pack"
BASE_COMMIT = "ffa9a6c04b1863118b3c8b5a61e6014675869a2f"

MAIN_LORE = "Sillytavern/Honkai Star Rail/Lorebook/Honkai Star Rail [LB].json"
TRACKER_LORE = "Sillytavern/Honkai Star Rail/Lorebook/Honkai Star Rail Tracker Systems [LB].json"
LORE_PATH = HSR / "Lorebook" / "Honkai Star Rail [LB].json"
CARD_A = HSR / "Bot" / "Honkai Star Rail RPG.json"
CARD_A_EXPLICIT = HSR / "Bot" / "Variants" / "Honkai Star Rail RPG - UI A - Astral Ticket.json"
CARD_B = HSR / "Bot" / "Variants" / "Honkai Star Rail RPG - UI B - Warp Record.json"
CARD_C = HSR / "Bot" / "Variants" / "Honkai Star Rail RPG - UI C - Data Bank.json"
README_PATH = HSR / "Bot" / "README.md"


def from_base(path: str) -> dict[str, Any]:
    raw = subprocess.check_output(["git", "show", f"{BASE_COMMIT}:{path}"], cwd=ROOT)
    return json.loads(raw.decode("utf-8"))


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def obsolete(entry: dict[str, Any]) -> bool:
    text = "\n".join(str(entry.get(k, "")) for k in ("name", "comment", "content")).casefold()
    return "hsr_status.v1" in text or "scene & status tracker output contract" in text


def sanitize_legacy_mentions(entry: dict[str, Any]) -> dict[str, Any]:
    cleaned = copy.deepcopy(entry)
    for field in ("content", "comment", "name"):
        value = cleaned.get(field)
        if isinstance(value, str):
            cleaned[field] = value.replace("hsr_status.v1", "legacy status schema")
    return cleaned


def complete_entry(
    uid: int,
    name: str,
    content: str,
    keys: list[str],
    *,
    constant: bool,
    order: int,
    position: int,
    priority: int,
    ignore_budget: bool = False,
) -> dict[str, Any]:
    extensions: dict[str, Any] = {
        "depth": 1 if constant else 4,
        "weight": priority,
        "addMemo": True,
        "displayIndex": uid,
        "useProbability": True,
        "characterFilter": None,
        "excludeRecursion": True,
        "vectorized": False,
    }
    if ignore_budget:
        extensions["ignoreBudget"] = True
    return {
        "uid": uid,
        "key": keys,
        "keysecondary": [],
        "comment": name,
        "content": content,
        "constant": constant,
        "selective": True,
        "selectiveLogic": 0,
        "order": order,
        "position": position,
        "disable": False,
        "addMemo": True,
        "excludeRecursion": True,
        "probability": 100,
        "displayIndex": uid,
        "useProbability": True,
        "secondary_keys": [],
        "keys": keys,
        "id": uid,
        "priority": priority,
        "insertion_order": uid,
        "enabled": True,
        "name": name,
        "extensions": extensions,
        "case_sensitive": False,
        "depth": 1 if constant else 4,
        "characterFilter": None,
        "vectorized": False,
    }


def build_worldbook() -> dict[str, Any]:
    main = from_base(MAIN_LORE)
    tracker = from_base(TRACKER_LORE)
    entries = [copy.deepcopy(e) for e in main["entries"].values() if not obsolete(e)]

    entries.append(
        complete_entry(
            902,
            "Archer",
            "Archer is a Counter Guardian and an HSR-style crossover guest from Fate/Star Rail Night. He is dry, pragmatic, observant and quietly protective despite his cynical presentation. He has short white hair, tan skin, grey eyes, and a red-and-black combat mantle. His paired blades Kanshou and Bakuya, Reinforcement magecraft, and Unlimited Blade Works make him a versatile close- and long-range combatant. In this HSR adaptation he walks the Hunt (Fire). PORTRAIT HEADER: use [HSRCHAR|archer|Archer|fire|hunt|Fate/Star Rail Night], followed by [HSRSAY|Archer|fire|text].",
            ["Archer", "EMIYA", "Counter Guardian", "Unlimited Blade Works", "อาเชอร์"],
            constant=False,
            order=100,
            position=1,
            priority=10,
        )
    )
    entries.append(
        complete_entry(
            903,
            "HSR • Attached UI & GitHub Portrait Guide",
            "ATTACHED UI CONTRACT — Each RPG card embeds exactly five regex scripts: Scene Tracker, one coordinated Header, one Monologue, one Dialogue, and Status Tracker. Do not import the removed Tracker Systems lorebook and do not use Narrator/Narrative UI yet. OUTPUT ORDER: (1) one <hsr_scene> hsr_scene.v1 JSON at the absolute top; (2) plain scene prose as needed; (3) optional [HSRTHINK|Name|element|thought]; (4) [HSRCHAR|slug|Name|element|path|faction]; (5) matching [HSRSAY|Name|element|words]; (6) one <hsr_status> hsr_status.v2 JSON at the absolute bottom. Never attribute HSRTHINK, HSRCHAR or HSRSAY to {{user}}. HEADER PORTRAITS: the slug must exactly match a JPG filename in Sillytavern/Honkai Star Rail/Images. Primary URL: https://raw.githubusercontent.com/DesZiDesu/sillytavern-card/main/Sillytavern/Honkai%20Star%20Rail/Images/<slug>.jpg . Fallback URL: https://rawcdn.githack.com/DesZiDesu/sillytavern-card/main/Sillytavern/Honkai%20Star%20Rail/Images/<slug>.jpg . The approved opening uses march-7th-ice.jpg and dan-heng.jpg. Verified crossover portraits include rin-tohsaka.jpg, gilgamesh.jpg and archer.jpg.",
            [],
            constant=True,
            order=9_999_997,
            position=4,
            priority=1000,
            ignore_budget=True,
        )
    )
    entries.extend(sanitize_legacy_mentions(e) for e in tracker["entries"].values())
    entries.sort(key=lambda e: (int(e.get("displayIndex", 0)), int(e.get("uid", 0))))

    main["name"] = "Honkai Star Rail [LB]"
    main["description"] = "Complete HSR lorebook with full world and character content, GitHub portrait instructions, and current Scene/Status contracts."
    main["token_budget"] = max(int(main.get("token_budget", 0)), 2048)
    main.setdefault("extensions", {})["world_info_budget"] = max(
        int(main.get("extensions", {}).get("world_info_budget", 0)), 4096
    )
    main["entries"] = {str(i): e for i, e in enumerate(entries)}

    packed = json.dumps(main, ensure_ascii=False)
    assert len(main["entries"]) == 81, len(main["entries"])
    assert '"schema":"hsr_status.v1"' not in packed.replace(" ", "")
    assert '"schema": "hsr_status.v1"' not in packed
    assert "hsr_status.v2" in packed
    return main


def character_book(world: dict[str, Any]) -> dict[str, Any]:
    converted: list[dict[str, Any]] = []
    for entry in world["entries"].values():
        position = int(entry.get("position", 0) or 0)
        converted.append(
            {
                "keys": list(entry.get("keys") or entry.get("key") or []),
                "secondary_keys": list(entry.get("secondary_keys") or entry.get("keysecondary") or []),
                "comment": str(entry.get("comment") or entry.get("name") or ""),
                "content": str(entry.get("content") or ""),
                "constant": bool(entry.get("constant", False)),
                "selective": bool(entry.get("selective", True)),
                "insertion_order": int(entry.get("insertion_order", entry.get("order", 100)) or 100),
                "enabled": bool(entry.get("enabled", not entry.get("disable", False))),
                "position": "before_char" if position in (0, 4) else "after_char",
                "use_regex": False,
                "extensions": copy.deepcopy(entry.get("extensions", {})),
            }
        )
    return {
        "name": world["name"],
        "description": world.get("description", ""),
        "scan_depth": int(world.get("scan_depth", 50)),
        "token_budget": int(world.get("token_budget", 2048)),
        "recursive_scanning": bool(world.get("recursive_scanning", False)),
        "extensions": copy.deepcopy(world.get("extensions", {})),
        "entries": converted,
    }


def enrich_card(path: Path, book: dict[str, Any]) -> dict[str, Any]:
    card = load(path)
    card["data"]["character_book"] = copy.deepcopy(book)
    card["data"].setdefault("extensions", {})["world"] = ""
    card["data"]["creator_notes"] = (
        "Self-contained HSR card with the complete 81-entry lorebook, five attached regexes, "
        "GitHub portrait headers, and the approved detailed opening."
    )
    regexes = card["data"]["extensions"]["regex_scripts"]
    names = [str(item.get("scriptName", "")) for item in regexes]
    packed = json.dumps(card, ensure_ascii=False)
    assert len(regexes) == 5, names
    assert len(card["data"]["character_book"]["entries"]) == 81
    assert not any("Narrator" in name or "Narrative" in name for name in names)
    for required in (
        "march-7th-ice",
        "dan-heng",
        "raw.githubusercontent.com",
        "rawcdn.githack.com",
        "<hsr_scene>",
        "<hsr_status>",
        "hsr_status.v2",
    ):
        assert required in packed, required
    assert '"schema":"hsr_status.v1"' not in packed.replace(" ", "")
    return card


def validate_portraits() -> None:
    image_dir = HSR / "Images"
    required = ["march-7th-ice.jpg", "dan-heng.jpg", "rin-tohsaka.jpg", "gilgamesh.jpg", "archer.jpg"]
    missing = [name for name in required if not (image_dir / name).is_file()]
    assert not missing, f"Missing portraits: {missing}"


def write_readme() -> None:
    README_PATH.write_text(
        "# Honkai: Star Rail self-contained cards\n\n"
        "Import **one card only**. Each card already embeds the complete 81-entry lorebook and exactly five regex scripts: Scene, Header, Monologue, Dialogue, and Status.\n\n"
        "- `Honkai Star Rail RPG.json` — canonical UI A build\n"
        "- `Variants/Honkai Star Rail RPG - UI A - Astral Ticket.json` — explicit UI A copy\n"
        "- `Variants/Honkai Star Rail RPG - UI B - Warp Record.json` — UI B\n"
        "- `Variants/Honkai Star Rail RPG - UI C - Data Bank.json` — UI C\n\n"
        "Do not import the removed Tracker Systems lorebook. Header portraits load from the repository image gallery with a raw.githack fallback.\n",
        encoding="utf-8",
    )


def main() -> None:
    validate_portraits()
    world = build_worldbook()
    book = character_book(world)

    cards = {
        "HSR_RPG_UI_A_Full.json": enrich_card(CARD_A, book),
        "HSR_RPG_UI_A_Explicit_Full.json": enrich_card(CARD_A_EXPLICIT, book),
        "HSR_RPG_UI_B_Full.json": enrich_card(CARD_B, book),
        "HSR_RPG_UI_C_Full.json": enrich_card(CARD_C, book),
    }

    save(LORE_PATH, world)
    save(CARD_A, cards["HSR_RPG_UI_A_Full.json"])
    save(CARD_A_EXPLICIT, cards["HSR_RPG_UI_A_Explicit_Full.json"])
    save(CARD_B, cards["HSR_RPG_UI_B_Full.json"])
    save(CARD_C, cards["HSR_RPG_UI_C_Full.json"])
    write_readme()

    OUT.mkdir(parents=True, exist_ok=True)
    save(OUT / "HSR_Lorebook_Fixed_Full.json", world)
    for filename, card in cards.items():
        save(OUT / filename, card)
    (OUT / "README.txt").write_text(
        "Import one card only. Every card embeds the complete 81-entry lorebook and five regexes.\n",
        encoding="utf-8",
    )

    zip_path = OUT / "HSR_Self_Contained_Full_Pack.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(OUT.iterdir()):
            if path != zip_path and path.is_file():
                archive.write(path, arcname=path.name)

    print(
        json.dumps(
            {
                "entries": len(world["entries"]),
                "regexes_per_card": 5,
                "files": sorted(path.name for path in OUT.iterdir()),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
