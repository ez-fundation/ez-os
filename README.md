# EZ-OS: Ludic Memory Operating System

<div align="center">

[![Português](https://img.shields.io/badge/Lang-Português-green)](README_pt.md)

![EZ-OS Mascot](assets/01_mascot_base.png)

**A factual memory system for retro games that records real events and expresses history through a deterministic procedural mascot.**

`#python` `#retro-gaming` `#memory-system` `#procedural-generation` `#ez-fundation` `#digital-sovereignty`

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![EZ-Fundation](https://img.shields.io/badge/Part%20of-EZ--Fundation-purple)](https://github.com/ez-fundation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 🎯 What is EZ-OS?

**EZ-OS** (Easy Operating System) is a Ludic Memory Operating System. Its primordial function is the **factual recording of usage events** and the **symbolic expression of this history**, operating in a lightweight, offline, and hardware-agnostic manner.

### Non-Negotiable Principles

- **Memory Factuality**: Records only real events.
- **Default Silence State**: Communicates only when relevant.
- **Deterministic Procedural Identity**: Evolution based on real data and unique seeds.
- **Degradation Resilience**: Functionality in ASCII/2-bit environments.
- **AI Isolation**: Heavy processing is external and optional.

---

## 🏛️ EZ-Fundation Context

EZ-OS is the **Ludic Memory Kernel** of [EZ-Fundation](https://github.com/ez-fundation).

- **Identity**: Consumes identities from `EZ-Character`.
- **Memory**: Generates and preserves the user's memory graph.
- **Sovereignty**: Ensures "Proof of Play" data belongs to the user.

---

## 🚀 Installation

### Requirements

- Python 3.9+
- pip

### Installation via pip (Development Mode)

```bash
# Clone the repository
git clone https://github.com/ez-fundation/ez-os.git
cd ez-os

# Install in editable mode
pip install -e .
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📖 Usage

### Start EZ-OS

```bash
ez-os
```

### Programmatic Usage

```python
from ez_os.core import memory, companion, governance
from ez_os.ui import tui
from ez_os.launcher import launcher

# Load memory graph
graph = memory.load_graph("data/memory_graph.json")

# Update mascot state
mascot = companion.update_state(graph)

# Render TUI
tui.render(mascot, graph)
```

---

## 🏗️ Architecture

EZ-OS is composed of isolated domains:

### **Core**
- `memory.py`: Factual JSON Graph (CRUD)
- `governance.py`: Validation and strict limits
- `companion.py`: Deterministic procedural mascot

### **UI**
- `tui.py`: Symbolic terminal rendering (via `rich`)

### **Launcher**
- `launcher.py`: Minimal launcher for RetroArch integration
- `indexer.py`: ROM indexing

### **Extensions**
- `gallery.py`: Game gallery
- `symbiosis.py`: Symbiotic integration with external systems

---

## 🎨 Mascot & Variations

<div align="center">

![Mascot Variations](assets/02_mascot_variations.png)

*The mascot evolves deterministically based on usage history*

</div>

### **Design Evolution**

> **Architect's Note**: The v2 iteration serves as the definitive multi-angle study for 3D modeling.

<div align="center">
  <img src="assets/11_concept_feb07_v2.png" width="400" alt="Mascot Design Study (Multi-Angle)">
  <p><em>Fig 2. Design Study: Volume & Angles Reference</em></p>
</div>

---

## 📚 Documentation

- [Technical Architecture](docs/architecture.md)
- [Philosophy & Principles](docs/philosophy.md)
- [EZ-Fundation Context](docs/ez-fundation_context.md)
- [Asset Catalog Guide](docs/asset_catalog_guide.md)
- [3D Character Design](docs/character_design.md)
- [🎨 Visual Gallery & Artbook](docs/gallery.md)

---

## 🤝 Contributing

Contributions are welcome! Please read our contributing guide before submitting a PR.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**João** - [ez-fundation](https://github.com/ez-fundation)

---

<div align="center">

*EZ-OS does not try to trap the player. It only remembers when they return.*

![EZ-OS Logo](assets/04_brand_logo_character.png)

</div>
