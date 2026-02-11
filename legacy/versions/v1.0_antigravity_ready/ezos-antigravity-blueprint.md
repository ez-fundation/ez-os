# 🛸 Antigravity Skill: EZ-OS Reconstructor

Esta skill permite que o **Antigravity** entenda, orquestre e reconstrua o ecossistema **EZ-OS v1.0** em qualquer ambiente compatível.

## 1. Identidade do Sistema
- **Nome**: EZ-OS (Symbiotic Memory System)
- **Versão**: 1.0-CANONICAL
- **Protocolo**: SMP v1.0
- **Núcleo**: Imutável / Congelado

## 2. Mapa de Reconstrução (Blueprint)

### A. Estrutura de Diretórios (Target)
O Antigravity deve garantir a seguinte árvore:
- `/core`: Módulos lógicos (`memory`, `companion`, `governance`, `launcher`, `tui`)
- `/layer`: Integração e Inteligência Echo (`echo_engine`, `integration/`)
- `/data`: Persistência do Grafo (`memory_graph.json`)
- `/docs`: Documentação Filosófica e Protocolos

### B. Dependências de Runtime
- **Linguagem**: Python 3.10+
- **Bibliotecas**: `rich` (TUI), `json`, `hashlib`, `datetime`
- **Ambiente**: Linux/Unix (para scripts de integração `.sh`)

## 3. Lógica de Orquestração
Para reconstruir a experiência, o Antigravity deve seguir esta sequência:
1. **Validation**: Verificar integridade do Core v1.0.
2. **Identity**: Gerar ou carregar a `seed.key` no `companion.py`.
3. **Echo**: Iniciar o `echo_engine.py` para análise de ressonância.
4. **TUI**: Lançar `tui.py` ou `ezos_echo_demo.py` como shell primário.

## 4. Invariantes para o Antigravity
- **NUNCA** alterar arquivos dentro de `/core`.
- **SEMPRE** usar a Layer para extensões de funcionalidade.
- **GARANTIR** que o Grafo de Memória seja append-only.

---
*Blueprint gerado por Manus para integração Antigravity.*
