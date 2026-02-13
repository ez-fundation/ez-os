# EZ-OS: Estrutura Analítica do Projeto (EAP/WBS)

> **Fase Atual**: Ato IV - A Soberania (Construção do Anima)
> **Objetivo**: Transformar o Protótipo v1.0 em um Sistema L2 Robusto e Simbiótico.

## 1. Fundação L2 (Robustez)
- [ ] **1.1 Migração de Memória (JSON -> SQLite)**
    - [ ] Criar schema `memory.db` (Tabelas: `facts`, `logs`, `affinity_weights`).
    - [ ] Implementar `src/ez_os/core/memory_sql.py` com ACID.
    - [ ] Migrar `identity.json` para tabela de configs.
- [ ] **1.2 Daemonização (Heartbeat)**
    - [ ] Criar `ez-os.service` para Linux/Arkos.
    - [ ] Implementar loop de background (sem TUI) para coleta de dados.

## 2. Sistema de Identidade (Soul)
- [ ] **2.1 Birth Protocol (Refinamento)**
    - [ ] Integrar `birth.py` com o novo SQLite.
    - [ ] Criar testes unitários para o `ART-Lite` (pesos dinâmicos).
- [ ] **2.2 Narrative Engine (`src/ez_os/narrative/`)**
    - [ ] Implementar sistema de templates dinâmicos baseados no Arquétipo escolhido.
    - [ ] Criar "Trigger Events" (ex: aniversário do user, lua cheia).

## 3. Interface & Instalação
- [ ] **3.1 Flash & Play Installer**
    - [ ] Criar script `bootstrap.sh` (Linux) e `install.bat` (Windows).
    - [ ] Empacotar release `.zip` com a estrutura `setup/` limpa.
- [ ] **3.2 TUI v2 (Imersão)**
    - [ ] Adicionar suporte a cores reais (Ansi).
    - [ ] Implementar "Idle Animations" (olhos piscando em ASCII).

## 4. Hardware Integration (Corpo)
- [ ] **4.1 Sensores Arkos**
    - [ ] Mapear leitura de bateria (`/sys/class/power_supply`).
    - [ ] Mapear RTC (Relógio de Tempo Real).

## 5. Legado & Governança
- [ ] **5.1 Manutenção do Canon**
    - [ ] Garantir que novos códigos respeitem o "Anti-Joi".
