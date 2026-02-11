# EZ-OS: Arquitetura Técnica

## 1. Visão Geral
O EZ-OS é um sistema de "Memória Lúdica" que organiza o histórico de jogos de forma simbólica e factual.

## 2. Estrutura de Dados (Grafo de Memória)
O grafo será armazenado em `data/memory_graph.json`.

### Nós (Nodes)
- **Game**: ID, Título, Plataforma, Data de Adição.
- **Event**: ID, GameID, Timestamp, Tipo (Start, Stop, Achievement, Milestone), Dados Adicionais.
- **User**: ID, Seed (para procedural).

### Relações (Edges)
- `PLAYED_IN`: Event -> Game
- `CHRONOLOGY`: Event -> Event (Next)

## 3. Mascote (Companion)
- **Nome**: Definido por Seed.
- **Forma**: ASCII Art gerada deterministicamente.
- **Estados**:
  - `Fase`: Ovo -> Jovem -> Adulto -> Sábio (baseado no número de eventos).
  - `Energia`: Baseado na frequência de uso recente.
  - `Foco`: Baseado no jogo mais jogado recentemente.

## 4. Domínios de Implementação
1. **UI**: Python + `rich`.
2. **Memória**: Módulo `memory.py` para CRUD no JSON.
3. **Governança**: Módulo `governance.py` para regras de negócio e validação.
4. **Execução**: Mock/Script de integração com RetroArch.

## 5. Fluxo de Operação
1. Usuário abre EZ-OS.
2. Sistema lê Grafo e atualiza estado do Mascote.
3. Usuário seleciona jogo.
4. EZ-OS registra evento "Start" e chama RetroArch.
5. Ao retornar, EZ-OS registra evento "Stop" e calcula tempo/memória.
