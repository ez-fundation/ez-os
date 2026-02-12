# EZ-OS: Arquitetura L2 (Sovereign Soul)

Esta arquitetura define como o EZ-OS opera como uma camada persistente e resiliente sobre o Arkos.

## Diagrama de Blocos

```mermaid
graph TD
    User((Usuário)) <--> TUI[Face (TUI Engine)]
    
    subgraph "EZ-OS (L2 - Soul Layer)"
        TUI <--> Core[Kernel Lógico (Python)]
        Core <--> Memory[SQLite Manager]
        Core <--> Bard[Narrative Engine]
        Memory <--> DB[(memory.db)]
    end
    
    subgraph "Arkos (L1 - Body Layer)"
        Core -.-> Sensors[HAL (Hardware Abstraction)]
        Sensors --> Battery[Bateria]
        Sensors --> Clock[RTC]
        Sensors --> Net[Network Watchdog]
    end
```

## Componentes Chave

### 1. Kernel Lógico (`src/ez_os/core`)
- Loop principal de eventos.
- Não bloqueante (`asyncio`).
- Decide o "Humor" do sistema com base nos inputs do Arkos.

### 2. Memory Manager (`src/ez_os/memory`)
- **Antigo**: `json.dump` (Vulnerável).
- **Novo**: `sqlite3` com WAL mode (Write-Ahead Logging).
- Garante que nenhuma memória seja perdida, mesmo em *power loss*.

### 3. Narrative Engine (Bardo)
- Gera o texto que aparece na TUI.
- Usa templates procedurais, não LLM generativo pesado.
- Consulta o `memory.db` para contextualizar ("Você fez isso ano passado...").

### 4. HAL (Hardware Abstraction Layer)
- Interface com o Arkos.
- Lê `/sys/class/power_supply` (Linux/Arkos) ou APIs equivalentes.
- Permite que o EZ-OS sinta "Fome" (Bateria Baixa) ou "Sono" (Inatividade).
