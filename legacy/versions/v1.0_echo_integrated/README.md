# 🔒 EZ-OS v1.0-CANONICAL

Este repositório contém a versão definitiva e consolidada do **EZ-OS**, o Sistema Operacional de Memória Lúdica.

## 🧠 Estrutura do Projeto

### 1. EZ-OS Core (v1.0-FINAL)
Localizado em `/core`, este núcleo é **imutável**.
- `memory.py`: Gestão de grafo factual (Append-only).
- `companion.py`: Mascote lógico (Determinístico).
- `governance.py`: Regras de silêncio e limites técnicos.
- `tui.py`: Interface canônica em terminal.
- `launcher.py`: Interface mínima de registro de eventos.

### 2. EZ-OS Layer (v1.0-LAYER)
Localizado em `/layer`, preparado para **ArkOS / R35S**.
- `integration/`: Scripts de hook para interceptar o ciclo de jogo.
- `data/`: Persistência do `memory_graph.json`.

## 🚀 Instalação em R35S (ArkOS)
1. Copie a pasta `ez-os` para `/home/ubuntu/`.
2. Configure o ArkOS para executar `python3 /home/ubuntu/ez-os/core/tui.py` no boot.
3. Aponte os scripts de lançamento do sistema para o `layer/integration/ezos_launch.sh`.

## 📜 Princípio Canônico
> **O EZ-OS não evolui por adição de funcionalidades. Ele permanece para ser confiável.**

---
*Factualidade | Silêncio | Memória*
