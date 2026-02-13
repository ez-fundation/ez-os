import os
import json
import time
from pathlib import Path

# EZ-OS (Anima): The Birth Protocol (ART-Lite Implementation)
# "I am born from what you choose to keep."

ROOT_DIR = Path(__file__).parent.parent.parent
SETUP_DIR = ROOT_DIR / "setup"
DATA_DIR = ROOT_DIR / "data"
IDENTITY_FILE = DATA_DIR / "identity.json"

def scan_setup():
    """Scans the setup directory to determine initial personality weights."""
    print("[BIRTH] EZ-OS Birth Protocol Initiated...")
    time.sleep(1)

    # 1. Detect Name
    name_dir = SETUP_DIR / "01_NOME_DO_SISTEMA"
    system_name = "Unknown"
    if name_dir.exists():
        for item in name_dir.iterdir():
            if item.is_dir() and "RENOMEIE" not in item.name:
                system_name = item.name
                break

    print(f"[SCAN] System Name Detected: {system_name}")

    # 2. Detect Archetypes (ART-Lite Weights)
    archetype_dir = SETUP_DIR / "02_ARQUETIPO"
    weights = {"The_Guardian": 0.1, "The_Jester": 0.1, "The_Scholar": 0.1}

    if archetype_dir.exists():
        for item in archetype_dir.iterdir():
            if item.is_dir():
                key = item.name
                if key in weights:
                    weights[key] += 0.5
                    print(f"[ART] Resonance Detected: {key} (+0.5)")

    # 3. Detect Focus
    focus_dir = SETUP_DIR / "03_FOCO_PRINCIPAL"
    focus = "Generalist"
    if focus_dir.exists():
        for item in focus_dir.iterdir():
            if item.is_dir():
                focus = item.name
                print(f"[FOCUS] Lock: {focus}")
                break

    return {
        "name": system_name,
        "archetypes": weights,
        "focus": focus,
        "birth_date": time.strftime("%Y-%m-%d"),
        "plasticity_rate": 0.1
    }

def save_identity(identity):
    """Saves the Identity Matrix to disk."""
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True)

    with open(IDENTITY_FILE, "w", encoding="utf-8") as f:
        json.dump(identity, f, indent=4, ensure_ascii=False)

    print(f"[SAVE] Identity Matrix Saved to {IDENTITY_FILE}")

def main():
    if IDENTITY_FILE.exists():
        print("[WARN] System already born. Delete data/identity.json to rebirth.")
        return

    if not SETUP_DIR.exists():
        print("[ERR] Setup directory not found. Please re-download EZ-OS.")
        return

    identity = scan_setup()
    save_identity(identity)

    print()
    print("=== BIRTH COMPLETE ===")
    print(f"Hello, {identity['name']}. I am ready.")
    print("Run 'python -m src.ez_os.launcher' to begin.")

if __name__ == "__main__":
    main()
