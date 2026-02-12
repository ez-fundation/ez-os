# EZ-OS: Estrutura Analítica do Projeto (EAP/WBS)

> **Fase Atual**: Ato IV - A Soberania
> **Objetivo**: Transformar o Protótipo v1.0 em um Sistema L2 Robusto.

## 1. Engenharia de Dados (A Memória Eterna)
- [ ] **1.1 Migração SQLite**
    - [ ] 1.1.1 Modelagem do Schema (Memórias, Fatos, Tags).
    - [ ] 1.1.2 Script de migração JSON -> SQL.
    - [ ] 1.1.3 Implementação de ACID Transactions.
- [ ] **1.2 Camada de "Facts"**
    - [ ] 1.2.1 Deduping de memórias repetidas.
    - [ ] 1.2.2 Indexação Semântica (Embeddings locais leves ou Keywords).

## 2. Engenharia de Sistemas (O Corpo)
- [ ] **2.1 Daemonização**
    - [ ] 2.1.1 Criar `ez-os.service` (Systemd/Arkos unit).
    - [ ] 2.1.2 Implementar Bootloader Hook.
- [ ] **2.2 Sensores (Arkos Bindings)**
    - [ ] 2.2.1 API de Bateria (PowerState).
    - [ ] 2.2.2 API de Relógio (Ciclo Circadiano).
    - [ ] 2.2.3 API de Rede (Detecção de "Silence").

## 3. Interface Lúdica (O Rosto)
- [ ] **3.1 TUI Engine v2**
    - [ ] 3.1.1 Buffer de renderização assíncrono (evitar flicker).
    - [ ] 3.1.2 Animações ASCII processuais (piscar, dormir).
- [ ] **3.2 Input Handling**
    - [ ] 3.2.1 Captura de teclas físicas (GPIO/Keyboard).

## 4. Hardware (O Berço)
- [ ] **4.1 Prototipagem Física**
    - [ ] 4.1.1 Impressão do Case (STL).
    - [ ] 4.1.2 Montagem do Kit Dev (Raspberry/Orange Pi/Arkos Board).

## 5. Legado & Governança
- [ ] **5.1 Manutenção do Canon**
- [ ] **5.2 Auditoria de "Anti-Joi"** (Garantir que não estamos inflando o ego da IA).
