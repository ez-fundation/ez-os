# 🥧 Implementação de Referência: Raspberry Pi (SMP-Edge)

O Raspberry Pi é o hospedeiro ideal para o EZ-OS como **Primitivo de Laboratório**. Esta implementação foca na simbiose entre eventos de sistema e a representação TUI.

## 1. Arquitetura da Layer (Raspberry Pi)
- **Hospedeiro**: Raspberry OS Lite (Headless).
- **Interface**: Display LCD 16x2 via I2C ou Terminal Serial via GPIO.
- **Interceptação**: `systemd` units e hooks no `.bashrc`.

## 2. Mapeamento de Eventos Simbióticos
No Raspberry Pi, o "jogo" é a própria computação:
- **START**: Início de um serviço, login via SSH, ou execução de script Python.
- **STOP**: Encerramento de processo, logout, ou shutdown.
- **Contexto**: O nome do script ou serviço torna-se o `game_id` no grafo.

## 3. Script de Adaptação (Exemplo Conceitual)
```bash
# /usr/local/bin/ezos-pi-hook
# Chamado por eventos do sistema

ACTION=$1
TARGET=$2

# Notifica o Core Congelado via API Mínima
python3 /home/pi/ezos/core/launcher.py "$ACTION" "$TARGET"

# Atualiza o display físico (LCD/OLED)
python3 /home/pi/ezos/layer/render_pi_display.py
```

## 4. O Mascote no Edge
No Raspberry Pi, o mascote atua como o **Espírito da Máquina**:
- **Observer**: O Pi está ocioso, apenas monitorando a rede.
- **Hacker**: O usuário está ativamente compilando código ou via SSH.
- **Archivist**: Logs de sistema estão sendo gerados em massa.

---
*Transformando um computador de placa única em um companheiro de memória persistente.*
