import os
import json
from pathlib import Path
from datetime import datetime

# EZ-OS (Anima): External Memory Indexer
# "I remember what you play, even if I don't hold the cartridge."

def index_external_drive(target_path):
    """
    Scans an external path for ROMs and Saves.
    Returns a lightweight catalog of metadata.
    """
    print(f"[INDEX] Scanning external memory at: {target_path}")
    
    catalog = {
        "scan_date": datetime.now().isoformat(),
        "source_path": str(target_path),
        "systems": {},
        "total_roms": 0,
        "total_saves": 0
    }

    target = Path(target_path)
    
    if not target.exists():
        print(f"[ERR] Target path not found: {target_path}")
        return catalog

    # Walk through the directory
    for root, dirs, files in os.walk(target):
        for file in files:
            file_path = Path(root) / file
            
            # Simple heuristic for ROMs and Saves
            if file.endswith((".zip", ".7z", ".iso", ".smc", ".gba", ".nes")):
                system = file_path.parent.name
                if system not in catalog["systems"]:
                    catalog["systems"][system] = {"roms": [], "saves": []}
                
                catalog["systems"][system]["roms"].append(file)
                catalog["total_roms"] += 1
                
            elif file.endswith((".srm", ".state", ".sav")):
                system = file_path.parent.name
                # Try to map save folder to system (often different in R36S)
                if system not in catalog["systems"]:
                     # Fallback bucket
                     system = "unknown_saves"
                     if system not in catalog["systems"]:
                        catalog["systems"][system] = {"roms": [], "saves": []}

                catalog["systems"][system]["saves"].append(file)
                catalog["total_saves"] += 1

    print(f"[DONE] Found {catalog['total_roms']} ROMs and {catalog['total_saves']} Saves.")
    return catalog

def save_catalog(catalog):
    data_dir = Path(__file__).parent.parent.parent.parent / "data"
    output_file = data_dir / "external_memory_map.json"
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=4)
    
    print(f"[SAVE] Catalog saved to {output_file}")

if __name__ == "__main__":
    # In a real scenario, this path comes from the user config
    # For now, we point to the local hosepdeiro folder
    HOST_PATH = Path(__file__).parent.parent.parent.parent / "data" / "hospedeiro#1"
    
    catalog = index_external_drive(HOST_PATH)
    save_catalog(catalog)
