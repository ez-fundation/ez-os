# 🔒 Symbiotic Memory Protocol (SMP v1.0)

O **Symbiotic Memory Protocol (SMP)** define o padrão de comunicação e comportamento para sistemas de memória lúdica reflexiva. Ele garante que a identidade e a história do usuário sejam preservadas de forma imutável e agnóstica de hardware.

## 1. Princípios de Conformidade
- **P1: Primazia do Grafo**: Toda verdade do sistema reside no `memory_graph.json`.
- **P2: Determinismo**: O estado simbólico é uma função pura do histórico factual.
- **P3: Silêncio Operacional**: O protocolo proíbe ações autônomas, metas próprias ou busca de engajamento.
- **P4: Imutabilidade do Core**: O núcleo que processa o protocolo é inalterável.

## 2. Estrutura do Grafo (SMP-JSON)
O grafo deve seguir a estrutura `append-only`:
```json
{
  "protocol_version": "1.0",
  "seed": "string-determinística",
  "events": [
    {
      "id": "uuid",
      "type": "START | STOP",
      "context": "string",
      "timestamp": "ISO-8601"
    }
  ]
}
```

## 3. Mapeamento de Estados (Reflexão)
O protocolo define 4 estados canônicos baseados na densidade de eventos:
- **Observer**: Estado padrão (silêncio/inatividade).
- **Archivist**: Atividade recente detectada (registro ativo).
- **Hacker**: Pico de atividade (simbiose profunda com o hardware).
- **Ghost**: Sessões abandonadas ou longos hiatos (memória latente).

## 4. Invariantes de Segurança
- Proibição de I/O de rede no processamento do Core.
- Proibição de auto-modificação de código.
- Proibição de geração de objetivos (Goal Generation).

---
*SMP v1.0: Identidade através da Memória Factual.*
