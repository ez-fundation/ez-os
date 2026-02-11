# Diagrama Arquitetural: EZ-OS v1.0

```mermaid
graph TD
    subgraph "EZ-OS LAYER (ArkOS/R35S)"
        H[Hardware R35S] --> B[ArkOS Boot]
        B --> T[EZ-OS TUI]
        
        subgraph "Integration Hooks"
            L[ezos_launch.sh]
        end
    end

    subgraph "EZ-OS CORE (Imutável)"
        T --> C[Companion]
        L --> LN[Launcher]
        LN --> G[Governance]
        LN --> M[Memory Graph]
        M --> C
    end

    subgraph "Data (Append-Only)"
        M --> DB[(memory_graph.json)]
    end
```

## Fluxo Canônico
1. **Boot**: ArkOS inicia e chama a `TUI`.
2. **Seleção**: Usuário escolhe um jogo.
3. **Hook**: `ezos_launch.sh` registra `START` via `Launcher`.
4. **Jogo**: O jogo roda via RetroArch.
5. **Retorno**: Ao fechar, o hook registra `STOP` e recarrega a `TUI`.
6. **Simbiose**: O `Companion` lê o novo estado da `Memory` e atualiza sua forma.
