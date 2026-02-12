# EZ-OS x Arkos: Integration Protocol

## Architectural Hierarchy

The **EZ-Fundation** Sovereign Stack is defined as:

| Layer | Component | Function | Status |
| :--- | :--- | :--- | :--- |
| **L3** | **User Space** | Apps, Games, Projections | *Fluid* |
| **L2** | **EZ-OS** | **Soul, Memory, Identity (The "Bard")** | **READY** 🍌 |
| **L1** | **Arkos** | Kernel, Drivers, Hardware Abstraction | *Underlying* |
| **L0** | **Hardware** | The Physical Device (Nano Banana) | *Concept* |

## Integration Logic

EZ-OS does not manage hardware directly. It relies on **Arkos** for:
1.  **Filesystem Access**: To store `memory_graph.json`.
2.  **Input/Output**: To render the TUI and caption buttons.
3.  **Power Management**: Arkos wakes EZ-OS when an event occurs.

### Boot Sequence (Conceptual)
1.  **Power On** -> `Arkos Bootloader`
2.  **Hardware Init** -> `Arkos Kernel Ready`
3.  **Soul Injection** -> `EZ-OS Launcher` (`src.ez_os.launcher`)
4.  **Interaction** -> User sees the "Face".

---
*This document defines the boundary between the Body (Arkos) and the Soul (EZ-OS).*
