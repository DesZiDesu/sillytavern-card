#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HSR = ROOT / "Sillytavern" / "Honkai Star Rail"
OUT = ROOT / "generated-hsr-pack"

MAIN_LORE = "Sillytavern/Honkai Star Rail/Lorebook/Honkai Star Rail [LB].json"
TRACKER_LORE = "Sillytavern/Honkai Star Rail/Lorebook/Honkai Star Rail Tracker Systems [LB].json"
CARD_A = HSR / "Bot" / "Honkai Star Rail RPG.json"
CARD_A_EXPLICIT = HSR / "Bot" / "Variants" / "Honkai Star Rail RPG - UI A - Astral Ticket.json"
CARD_B = HSR / "Bot" / "Variants" / "Honkai Star Rail RPG - UI B - Warp Record.json"
CARD_C = HSR / "Bot" / "Variants" / "Honkai Star Rail RPG - UI C - Data Bank.json"


def from_main(path: str) -> dict[str, Any]:
    raw = subprocess.check_output(["git", "show", f"origin/main:{path}"], cwd=ROOT)
    return json.loads(raw.decode("utf-8"))


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def obsolete(entry: dict[str, Any]) -> bool:
    text = "\n".join(str(entry.get(k, "")) for k in ("name", "comment", "content")).casefold()
    return "hsr_status.v1" in text or "scene & status tracker output contract" in text


def complete_entry(uid: int, name: str, content: str, keys: list[str], *, constant: bool, order: int, position: int, priority: int, ignore_budget: bool = False) -> dict[str, Any]:
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
        "extensions": {
            "depth": 1 if constant else 4,
            "weight": priority,
            "addMemo": True,
            "displayIndex": uid,
            "useProbability": True,
            "characterFilter": None,
            "excludeRecursion": True,
            "vectorized": False,
            **({"ignoreBudget": True} if ignore_budget else {}),
        },
        "case_sensitive": False,
        "depth": 1 if constant else 4,
        "characterFilter": None,
        "vectorized": False,
    }


def build_worldbook() -> dict[str, Any]:
    main = from_main(MAIN_LORE)
    tracker = from_main(TRACKER_LORE)
    entries = [copy.deepcopy(e) for e in main["entries"].values() if not obsolete(e)]

    archer = complete_entry(
        902,
        "Archer",
        "Archer is a Counter Guardian and an HSR-style crossover guest from Fate/Star Rail Night. He is dry, pragmatic, observant and quietly protective despite his cynical presentation. He has short white hair, tan skin, grey eyes, and a red-and-black combat mantle. His paired blades Kanshou and Bakuya, Reinforcement magecraft, and Unlimited Blade Works make him a versatile close- and long-range combatant. In this HSR adaptation he walks the Hunt (Fire). PORTRAIT HEADER: use [HSRCHAR|archer|Archer|fire|hunt|Fate/Star Rail Night], followed by [HSRSAY|Archer|fire|text].",
        ["Archer", "EMIYA", "Counter Guardian", "Unlimited Blade Works", "อาเชอร์"],
        constant=False,
        order=100,
        position=1,
        priority=10,
    )
    guide = complete_entry(
        903,
        "HSR • Attached UI & GitHub Portrait Guide",
        "ATTACHED UI CONTRACT — The RPG cards embed exactly five regex scripts: Scene Tracker, one coordinated Header, one Monologue, one Dialogue, and Status Tracker. Do not import the removed Tracker Systems lorebook and do not use Narrator/Narrative UI yet. OUTPUT ORDER: (1) one <hsr_scene> hsr_scene.v1 JSON at the absolute top; (2) plain scene prose as needed; (3) optional [HSRTHINK|Name|element|thought]; (4) [HSRCHAR|slug|Name|element|path|faction]; (5) matching [HSRSAY|Name|element|words]; (6) one <hsr_status> hsr_status.v2 JSON at the absolute bottom. Never attribute HSRTHINK, HSRCHAR or HSRSAY to {{user}}. HEADER PORTRAITS: slug must exactly match a JPG filename in Sillytavern/Honkai Star Rail/Images. Primary URL: https://raw.githubusercontent.com/DesZiDesu/sillytavern-card/main/Sillytavern/Honkai%20Star%20Rail/Images/<slug>.jpg . Fallback URL: https://rawcdn.githack.com/DesZiDesu/sillytavern-card/main/Sillytavern/Honkai%20Star%20Rail/Images/<slug>.jpg . The approved opening uses march-7th-ice.jpg and dan-heng.jpg. Other verified examples are rin-tohsaka.jpg, gilgamesh.jpg and archer.jpg.",
        [],
        constant=True,
        order=9_999_997,
        position=4,
        priority=1000,
        ignore_budget=True,
    )
    entries.extend([archer, guide])
    entries.extend(copy.deepcopy(e) for e in tracker["entries"].values())
    entries.sort(key=lambda e: (int(e.get("displayIndex", 0)), int(e.get("uid", 0))))

    main["name"] = "Honkai Star Rail [LB]"
    main["description"] = "Complete HSR lorebook with full world and character content, GitHub portrait instructions, and current Scene/Status v2 contracts."
    main["token_budget"] = max(int(main.get("token_budget", 0)), 2048)
    main.setdefault("extensions", {})["world_info_budget"] = max(int(main.get("extensions", {}).get("world_info_budget", 0)), 4096)
    main["entries"] = {str(i): e for i, e in enumerate(entries)}
    assert len(main["entries"]) == 81, len(main["entries"])
    assert "hsr_status.v1" not in json.dumps(main, ensure_ascii=False).casefold()
    return main


def character_book(world: dict[str, Any]) -> dict[str, Any]:
    converted = []
    for e in world["entries"].values():
        position = int(e.get("position", 0) or 0)
        converted.append({
            "keys": list(e.get("keys") or e.get("key") or []),
            "secondary_keys": list(e.get("secondary_keys") or e.get("keysecondary") or []),
            "comment": str(e.get("comment") or e.get("name") or ""),
            "content": str(e.get("content") or ""),
            "constant": bool(e.get("constant", False)),
            "selective": bool(e.get("selective", True)),
            "insertion_order": int(e.get("insertion_order", e.get("order", 100)) or 100),
            "enabled": bool(e.get("enabled", not e.get("disable", False))),
            "position": "before_char" if position in (0, 4) else "after_char",
            "use_regex": False,
            "extensions": copy.deepcopy(e.get("extensions", {})),
        })
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
    card["data"]["creator_notes"] = "Self-contained HSR card with the complete 81-entry lorebook, five attached regexes, GitHub portrait headers, and the approved detailed opening."
    assert len(card["data"]["extensions"]["regex_scripts"]) == 5
    assert len(card["data"]["character_book"]["entries"]) == 81
    packed = json.dumps(card, ensure_ascii=False)
    for required in ("march-7th-ice", "dan-heng", "raw.githubusercontent.com", "rawcdn.githack.com", "<hsr_scene>", "<hsr_status>"):
        assert required in packed, required
    assert "hsr_status.v1" not in packed.casefold()
    return card


def main() -> None:
    world = build_worldbook()
    book = character_book(world)
    OUT.mkdir(parents=True, exist_ok=True)
    save(OUT / "HSR_Lorebook_Fixed_Full.json", world)
    save(OUT / "HSR_RPG_UI_A_Full.json", enrich_card(CARD_A, book))
    save(OUT / "HSR_RPG_UI_A_Explicit_Full.json", enrich_card(CARD_A_EXPLICIT, book))
    save(OUT / "HSR_RPG_UI_B_Full.json", enrich_card(CARD_B, book))
    save(OUT / "HSR_RPG_UI_C_Full.json", enrich_card(CARD_C, book))
    (OUT / "README.txt").write_text(
        "Import one card only. Each card embeds the complete 81-entry lorebook and five regexes. UI A is canonical; B and C are selectable variants. Header portraits load from the GitHub HSR gallery.\n",
        encoding="utf-8",
    )
    print(json.dumps({"entries": len(world["entries"]), "files": sorted(p.name for p in OUT.iterdir())}, indent=2))


if __name__ == "__main__":
    main()
