# EZ-OS 3D Printing Guide

> **Character**: EZ-OS Companion  
> **Style**: Voxel / Low-Poly  
> **File**: `data/3d_specs/character_design_print.json`

---

## 🏗️ Design Concept

The EZ-OS Companion is designed as a physical "**Desktop Totem**" — a tangible representation of the user's digital memory.

### Physical Characteristics
- **Shape**: Technical but friendly. Think "GameBoy meets Tamagotchi".
- **Aesthetics**: Retro-futuristic, clean lines, tactile.
- **Size**: Approximately 35mm x 35mm (Keychain/Desk Toy size).

---

## 🖨️ Printing Instructions

### **Recommended Settings (FDM)**
- **Nozzle**: 0.4mm (Standard) or 0.2mm (High Precision)
- **Layer Height**: 0.12mm recommended for smooth curves
- **Material**: Matte PLA looks best for the "retro plastic" vibe
- **Infill**: 15% is sufficient

### **Color Strategy**
1. **Multi-color Print**: If you have a Bambu Lab AMS or Prusa MMU.
   - Body: Light Grey
   - Screen: Dark Green/Black
   - Antenna: Red
2. **Single Color + Paint**: Print in Grey PLA, paint details with acrylics.
3. **Multi-part Assembly**: Print screen insert separately and glue.

---

## 🧩 Procedural Accessories

The design includes a **magnetic mount point** on top. You can print accessories to match the procedural evolution:

- 🎩 **Top Hat** (Veteran Status)
- 🌸 **Flower** (Spring Theme)
- 🕶️ **Sunglasses** (Summer Theme - Glue on front)
- 🧣 **Scarf** (Winter Theme - Ring shape for body)

---

## 📦 File Export

This JSON specification is intended to be parsed by a script (e.g., Blender Python API or OpenSCAD) to generate the actual `.stl` or `.obj` files.

**Comming Soon**: `generate_stl.py` script.
