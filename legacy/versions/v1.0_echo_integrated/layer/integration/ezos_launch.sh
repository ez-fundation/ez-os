#!/bin/bash
# EZ-OS v1.0-LAYER: ArkOS Integration
# Este script deve ser chamado pelo ArkOS para lançar jogos

ROM_PATH=$1
CORE_PATH=$2

# 1. Registro Canônico de START
python3 /home/ubuntu/ez-os/core/launcher.py START "$ROM_PATH"

# 2. Execução (Mock do RetroArch para o ambiente de teste)
# Em hardware real: retroarch -L "$CORE_PATH" "$ROM_PATH"
echo "Launching $ROM_PATH..."

# 3. Registro Canônico de STOP (após fechar o jogo)
python3 /home/ubuntu/ez-os/core/launcher.py STOP "$ROM_PATH"

# 4. Retorno à TUI
python3 /home/ubuntu/ez-os/core/tui.py
