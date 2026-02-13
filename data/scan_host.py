"""EZ-OS: Host Scanner - Scans EASYROMS drive for memory indexing."""
import os
import json
from pathlib import Path
from datetime import datetime

TARGET = Path("E:/")
OUTPUT = Path("c:/Users/João/Desktop/PROJETOS/04_DEVELOPER_TOOLS/ez-os/data/external_memory_map.json")

ROM_EXTS = {
    ".zip", ".7z", ".iso", ".bin", ".cue", ".smc", ".sfc",
    ".gba", ".gbc", ".gb", ".nes", ".nds", ".n64", ".z64",
    ".v64", ".pbp", ".cso", ".chd", ".img", ".gen", ".smd",
    ".gg", ".sms", ".pce", ".ngp", ".ws", ".wsc", ".vb",
    ".a26", ".a78", ".lnx", ".col", ".sg", ".fds", ".mgw",
}
SAVE_EXTS = {".srm", ".state", ".sav", ".state1", ".state2", ".state3"}
SKIP = {
    "System Volume Information", "backup", "bios", "bgmusic",
    "launchimages", "movies", "themes", "tools",
}

def main():
    catalog = {
        "scan_date": datetime.now().isoformat(),
        "source": "R36S EASYROMS (E:)",
        "systems": {},
        "total_roms": 0,
        "total_saves": 0,
    }

    for sd in sorted(TARGET.iterdir()):
        if not sd.is_dir() or sd.name in SKIP:
            continue
        roms = []
        saves = []
        try:
            for f in sd.rglob("*"):
                if f.is_file():
                    ext = f.suffix.lower()
                    if ext in ROM_EXTS:
                        roms.append(f.name)
                    elif ext in SAVE_EXTS:
                        saves.append(f.name)
        except PermissionError:
            pass

        if roms or saves:
            catalog["systems"][sd.name] = {
                "rom_count": len(roms),
                "save_count": len(saves),
                "sample_roms": roms[:5],
            }
            catalog["total_roms"] += len(roms)
            catalog["total_saves"] += len(saves)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    total_sys = len(catalog["systems"])
    total_r = catalog["total_roms"]
    total_s = catalog["total_saves"]
    print(f"[DONE] {total_sys} systems | {total_r} ROMs | {total_s} Saves")
    print(f"[SAVE] {OUTPUT}")

if __name__ == "__main__":
    main()
