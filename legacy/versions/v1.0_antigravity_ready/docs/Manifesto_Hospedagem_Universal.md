# 🌐 Manifesto de Hospedagem Universal (SMP-Host)

Este manifesto define os requisitos e a API mínima para que qualquer dispositivo (Edge, Handheld, Server) possa hospedar o protocolo SMP e o EZ-OS.

## 1. O Contrato do Hospedeiro
Para ser um hospedeiro SMP, o dispositivo deve garantir:
1. **Acesso ao Grafo**: Capacidade de ler e anexar a um arquivo JSON local.
2. **Registro Temporal**: Um relógio de sistema confiável (mesmo que offline).
3. **Superfície de Renderização**: Um meio de expressar o estado (Terminal, E-Ink, Framebuffer ou Serial).

## 2. API Mínima de Integração (SMP-API)

### Entrada (Input Context)
O hospedeiro envia para o Core:
```json
{
  "device": {
    "type": "pi | kindle | console | server",
    "display": "ascii | bit2 | ink",
    "input": "buttons | keyboard | none"
  },
  "event_trigger": {
    "action": "START | STOP",
    "target": "id_do_processo_ou_tarefa"
  }
}
```

### Saída (Symbolic Output)
O Core responde com o estado a ser renderizado:
```json
{
  "symbolic_state": "observer | archivist | hacker | ghost",
  "render_payload": {
    "ascii": "(O)---(O)",
    "meta": { "deterministic": true, "version": "1.0" }
  }
}
```

## 3. Filosofia de Implantação
- **Não-Invasivo**: O SMP roda como uma camada de observação. Ele não deve interromper os processos nativos do hospedeiro.
- **Resiliência**: Se o hospedeiro falhar, o grafo deve permanecer íntegro. Se o Core falhar, o hospedeiro deve continuar operando normalmente (Fail-Silent).

---
*Qualquer dispositivo capaz de registrar um fato pode hospedar uma alma simbólica.*
