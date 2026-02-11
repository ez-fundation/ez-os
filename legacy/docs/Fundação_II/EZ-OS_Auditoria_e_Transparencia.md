# 🔍 Auditoria e Transparência no EZ-OS

A confiança no EZ-OS é estabelecida através da **Auditoria por Inspeção**, eliminando a necessidade de explicações verbais complexas ou algoritmos opacos.

## 1. Rastreabilidade Factual
Todo estado visual do mascote ou da interface pode ser traçado diretamente a uma entrada no `memory_graph.json`.
- Se o mascote evoluiu para "Jovem", existe um registro de pelo menos 1 evento `START`.
- Se o sistema está em modo "Silêncio", é porque o grafo não registra atividade recente.

## 2. O Grafo como Fonte Única
O arquivo `memory_graph.json` é a única fonte de verdade. Ele é:
- **Append-only**: Eventos são apenas adicionados, nunca alterados ou removidos.
- **Humano-legível**: Estrutura JSON simples que permite inspeção manual rápida.

## 3. Ausência de Inferência
O EZ-OS não "acha" nada. Ele não tenta prever o que o usuário quer jogar nem sugere comportamentos. A transparência reside na **previsibilidade determinística**.

---
*Confiança não se constrói com palavras, mas com a capacidade de verificar o histórico.*
