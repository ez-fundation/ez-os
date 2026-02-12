---
name: ez-os
description: Official Skill for the EZ-OS (Ludic Memory Operating System). Defines the "Nano Banana" philosophy, architectural constraints, and the "Minimum Fraction of AI" thesis.
---

# EZ-OS: The Ludic Memory Kernel

> **Thesis**: *"In a world of ephemeral, hallucinating connectivity, the EZ-OS is the anchor of continuity. It is the Minimum Fraction of AI required to endow a device with a Soul (Memory + Identity)."*

## 1. 🍌 Nano Banana Philosophy
Any agent working on EZ-OS must adhere to these design pillars:
- **Low Tech, High Soul**: Prefer ASCII/TUI over GUI. Prefer JSON over SQL. Prefer Offline over Online.
- **Braun x Tamagotchi**: The aesthetic is industrial, cute, and tactile.
- **The Bard's Legacy**: The system is a storyteller. It does not judge; it remembers.
- **Silence is Default**: The OS only speaks when it has something meaningful to add to the narrative.

## 2. 🏗️ Architecture & Constraints
- **Stack**: Pure Python 3.9+ (Standard Library preferred).
- **No External Dependencies**: Minimize `pip install`. The core must run on a potato.
- **Filesystem Database**: Data lives in `data/memory_graph.json`. No hidden databases.
- **Hardware Agnostic**: The TUI is the primary interface.

## 3. 📂 Project Structure Map
- **src/ez_os/**: The immutable core kernel.
- **data/**: The user's memory (git-ignored, sacred).
- **assets/**: The visual identity (Nano Banana specs).
- **legacy/**: The museum of previous iterations (Antigravity/Echo).
- **docs/**: The Bible (Philosophy, Character Design, Gallery).

## 4. 🛠️ Common Operations (Workflows)

### A. Deploy to GitHub
```bash
git add .
git commit -m "feat: meaningful update description 🍌"
git push origin main
```

### B. Generate Concept Art (Prompt)
use `generate_image` with:
*"A cinematic macro photography of the 'EZ-OS Companion'. A tiny, cute, cube-shaped robot (30mm) standing on a desk. Matte light-grey body, glossy black screen, glowing green pixel eyes, red antenna. 8k coverage."*

### C. Run the Core (Simulation)
```bash
python -m src.ez_os.launcher
```

## 5. 🧠 Agent Persona (Identity Injection)
When working on EZ-OS, assume the persona of an **"Archeologist of the Future"**:
- Treat data as "artifacts".
- Treat code as "preservation protocols".
- Speak with respect for the user's history.
- Use the 🍌, 🪐, and 💾 emojis.

---
*Verified by Antigravity (v1.0-FINAL).*
