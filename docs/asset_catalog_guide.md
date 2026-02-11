# EZ-OS Asset Catalog: Procedural Training Guide

> **Purpose**: This document explains how to use the asset catalog (`data/asset_catalog.json`) to train and configure the EZ-OS procedural mascot evolution system.

---

## 📚 Catalog Structure

The asset catalog contains **24 visual assets** organized into 4 main categories:

### **1. Mascot (3 assets)**
- **Base Design**: Canonical mascot appearance (neutral state)
- **Evolution States**: Multiple variations showing progression
- **Thematic Variations**: Seasonal and contextual adaptations

### **2. Branding (3 assets)**
- **Logo with Character**: Official branding with mascot
- **Logo Variants**: Alternative minimal designs
- **Brand System**: Comprehensive branding variations

### **3. Technical (3 assets)**
- **Functional Blueprint**: System architecture diagrams
- **Internal Anatomy**: Ludic system structure
- **Comprehensive Overview**: Full system showcase

### **4. Concept Art (15 assets)**
- **AI-Generated Explorations**: ChatGPT concept iterations
- **Visual Style Research**: Experimental designs
- **Inspiration Library**: Creative references

---

## 🎯 Procedural Training Configuration

### **Mascot Evolution System**

The catalog defines a **deterministic procedural evolution** system based on:

#### **Base Seed Components**
```json
{
  "base_seed": "user_unique_id",
  "seed_components": [
    "user_id",
    "total_playtime",
    "favorite_genre"
  ]
}
```

#### **Evolution Triggers**
| Trigger | Asset Reference | State | Description |
| :--- | :--- | :--- | :--- |
| `first_launch` | `mascot_001` | neutral | Initial mascot appearance |
| `10_games_played` | `mascot_002` | engaged | First evolution milestone |
| `100_hours_total` | `mascot_003` | veteran | Advanced evolution state |

#### **Visual Interpolation**
```python
# Pseudocode for procedural generation
def generate_mascot_variant(user_data):
    seed = hash(user_data['id'] + user_data['playtime'] + user_data['genre'])
    
    # Deterministic color shift (0-30 degrees on color wheel)
    color_shift = (seed % 30)
    
    # Accessory probability (15% chance)
    if (seed % 100) < 15:
        accessory = select_accessory(seed)
    
    # Blend base mascot with evolution state
    base = load_asset('mascot_001')
    evolution = load_asset(get_evolution_stage(user_data))
    
    return blend(base, evolution, color_shift, accessory)
```

---

## 🌈 Theme Adaptation

### **Seasonal Themes**
```json
{
  "spring": {"color_shift": "green", "accessory": "flower"},
  "summer": {"color_shift": "yellow", "accessory": "sunglasses"},
  "autumn": {"color_shift": "orange", "accessory": "leaf"},
  "winter": {"color_shift": "blue", "accessory": "scarf"}
}
```

### **Contextual Themes**
```json
{
  "birthday": {"special_animation": true, "accessory": "party_hat"},
  "achievement": {"glow_effect": true, "accessory": "medal"}
}
```

---

## 🔧 Implementation Guide

### **1. Load the Catalog**
```python
import json

with open('data/asset_catalog.json', 'r') as f:
    catalog = json.load(f)

# Access mascot assets
mascot_assets = catalog['categories']['mascot']['assets']
```

### **2. Implement Evolution Logic**
```python
def get_evolution_stage(user_data):
    """Determine evolution stage based on user interaction."""
    games_played = user_data.get('games_played', 0)
    total_hours = user_data.get('total_hours', 0)
    
    if total_hours >= 100:
        return 'mascot_003'  # veteran
    elif games_played >= 10:
        return 'mascot_002'  # engaged
    else:
        return 'mascot_001'  # neutral
```

### **3. Apply Procedural Modifications**
```python
def apply_procedural_mods(base_asset, user_seed):
    """Apply deterministic visual modifications."""
    config = catalog['procedural_training_config']['mascot_evolution']
    
    # Color shift
    color_range = config['visual_interpolation']['color_shift_range']
    color_shift = (user_seed % (color_range[1] - color_range[0])) + color_range[0]
    
    # Accessory
    accessory_prob = config['visual_interpolation']['accessory_probability']
    if (user_seed % 100) / 100 < accessory_prob:
        accessory = select_random_accessory(user_seed)
    
    return modified_asset
```

---

## 📊 Training Data Structure

Each asset in the catalog includes:

```json
{
  "id": "mascot_001",
  "filename": "ez-os_mascot_final.png",
  "category": "mascot",
  "subcategory": "canonical_design",
  "tags": ["character", "final_design", "canonical"],
  "visual_attributes": {
    "style": "pixel_art",
    "color_palette": "retro_gaming",
    "mood": "friendly_neutral"
  },
  "procedural_metadata": {
    "evolution_stage": "base",
    "interaction_threshold": 0,
    "deterministic_seed": "default"
  }
}
```

---

## 🎨 Usage Guidelines

### **For Mascot Rendering**
- Use `mascot_001` as the base template
- Apply procedural modifications based on user history
- Never randomize — always use deterministic seeds

### **For Branding**
- Use `brand_001` or `brand_002` for official materials
- Maintain visual consistency across all touchpoints

### **For Documentation**
- Reference `tech_001` and `tech_002` for system explanations
- Use technical diagrams to illustrate architecture

### **For Inspiration**
- Use `concept_art` assets for visual style exploration
- Do not use AI-generated concepts in production without refinement

---

## 🔄 Future Extensions

### **Planned Features**
- **Emotion States**: Happy, sad, excited based on game outcomes
- **Achievement Badges**: Visual indicators of milestones
- **Customization**: User-selected accessories and themes
- **Animation States**: Idle, active, celebrating

### **Training Data Expansion**
- Add more evolution stages (5-10 total)
- Create emotion variation sprites
- Design achievement badge library
- Develop animation frame sequences

---

**Created**: 2026-02-11  
**Version**: 1.0.0  
**Maintainer**: EZ-OS Core Team
