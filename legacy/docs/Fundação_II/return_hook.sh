#!/bin/bash
# EZ-OS v1.0-LAYER: Return Hook
# Usage: ./return_hook.sh <rom_path>

ROM_PATH=$1

# 1. Register STOP event in EZ-OS
python3 /home/ubuntu/ez-os-layer/core/launcher.py --action STOP --game "$ROM_PATH"

# 2. Re-open EZ-OS TUI
python3 /home/ubuntu/ez-os-layer/core/tui.py
