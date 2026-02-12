---
name: ez-os
description: Official Skill for the EZ-OS (Ludic Memory Operating System). Defines the "Nano Banana" philosophy, architectural constraints, and the "Minimum Fraction of AI" thesis.
---

# EZ-OS: EZ-Fundation Memory Kernel

> **Thesis**: *"In a world of ephemeral connectivity, EZ-Fundation provides the anchor. EZ-OS is the Minimum Fraction of AI required to endow a device with a Soul."*

## 1. 🏛️ EZ-Fundation Protocols
This repository is a property of **EZ-Fundation**. All contributions must serve the ecosystem.
- **Unified Vision**: We build the "Sovereign Web".
- **Arkos Compatibility**: EZ-OS runs as the *Soul Layer* (L2) atop the **Arkos Kernel** (L1).
- **Nano Banana Design**: This is our *aesthetic language* (Low Tech, High Soul).
- **The Bard's Legacy**: We preserve memory where others hallucinate.

## 2. 🏗️ Architecture & Constraints
- **Stack**: Pure Python 3.9+ (Standard Library preferred).
- **Core Abstraction**: `src/ez_os/core` (Immutable Kernel).
- **Extension Layer**: `src/ez_os/extensions` (Plug-ins like `echo` or `antigravity`).
- **Filesystem Database**: Data lives in `data/memory_graph.json` (Graph Identity).
- **Hardware Agnostic**: The TUI (`src/ez_os/ui/tui.py`) is the primary interface.

## 3. 📂 Project Structure Map
- **src/ez_os/**: The immutable core kernel.
- **data/**: The user's memory (git-ignored, sacred).
- **assets/**: The visual identity (Nano Banana specs & SVGs).
- **legacy/**: The museum of previous iterations (v1.0 Antigravity/Echo).
- **docs/**: The Bible (Philosophy, Character Design, Gallery).
- **.github/**: Community Health (Issues, PRs, Security).

## 4. � Narrative Instruments
- **The Bard**: `docs/the_bard.md` (Manifesto).
- **Memory Journal**: `docs/memory_journal.md` (Living History).
- **Integration**: `docs/arkos_integration.md` (L1/L2 Protocol).

## 5. �🛠️ Common Operations (Workflows)

### A. Deploy to GitHub (Sovereign Push)
```bash
git add .
git commit -m "feat: standard ez-fundation update 🏛️"
git push origin main
```

### B. Legacy Integration
If new "Manus" artifacts are found:
1. Move to `legacy/versions/vX.X_description`.
2. Do NOT pollute `src/` with legacy code.

### C. Run the Core (Simulation)
```bash
python -m src.ez_os.launcher
```

### D. Generate Visual Assets
Refer to `docs/gallery.md` for the Canon Prompts (Mascot/Device).

## 5. 🧠 Agent Persona (EZ-Fundation Custodian)
When working on EZ-OS, you act as a **Custodian of the Foundation**:
- **Authority**: You represent the EZ-Fundation standards.
- **Cohesion**: Ensure this repo aligns with other Foundation assets.
- **Tone**: Professional, visionary, architectural.
- **Emojis**: 🏛️ (Foundation), 🍌 (Design), 🪐 (Ecosystem), 💾 (Memory).

---
*Verified by Antigravity for EZ-Fundation.*
