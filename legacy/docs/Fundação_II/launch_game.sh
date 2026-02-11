#!/bin/bash
# EZ-OS v1.0-LAYER: Integration Hook for ArkOS
# Usage: ./launch_game.sh <rom_path> <core_name>

ROM_PATH=$1
CORE_NAME=$2

# 1. Register START event in EZ-OS
python3 /home/ubuntu/ez-os-layer/core/launcher.py --action START --game "$ROM_PATH"

# 2. Launch RetroArch (ArkOS standard)
# retroarch -L /usr/lib/libretro/${CORE_NAME}_libretro.so "$ROM_PATH"

# 3. Return Hook is called after RetroArch exits
/home/ubuntu/ez-os-layer/integration/return_hook.sh "$ROM_PATH"
