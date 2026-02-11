# Estrutura Conceitual de Adaptação (Protocolo Simbiótico)

Este documento define como o EZ-OS Core v1.0-FINAL deve ser integrado a novos hospedeiros sem sofrer alterações.

## 1. A Anatomia da Integração
A adaptação ocorre sempre através de uma **Layer** externa, nunca modificando o **Core**.

```text
[ Hardware Hospedeiro ]
       ↓
[ Sistema Operacional Nativo ]
       ↓
[ EZ-OS LAYER (Adaptação) ]  <-- Onde a tradução ocorre
       ↓
[ EZ-OS CORE (v1.0-FINAL) ]  <-- Imutável
```

## 2. O Protocolo de Eventos (Tradução)
Cada hospedeiro deve mapear suas ações nativas para os primitivos do EZ-OS:
- **Evento Nativo** (Ex: Abrir PDF no Kindle) → Traduzido para `START` no `launcher.py`.
- **Evento Nativo** (Ex: Fechar PDF / Sleep) → Traduzido para `STOP` no `launcher.py`.
- **Propriedades**: O hospedeiro deve fornecer metadados factuais (ID do arquivo, Timestamp).

## 3. Renderização Simbiótica
A Layer de adaptação é responsável por apresentar o estado do Core de acordo com as capacidades do hardware:
- **E-Ink**: Atualizações parciais do mascote para evitar ghosting.
- **Headless**: Envio do estado do mascote via Serial ou Log.
- **Terminal**: Uso da TUI canônica via SSH ou console local.

## 4. Garantias de Integridade
- **Isolamento**: O Core não deve ter permissão de escrita fora de seu diretório de dados.
- **Unidirecionalidade**: A Layer lê o estado do Core, mas o Core nunca solicita informações da Layer de forma ativa.
- **Persistência**: O `memory_graph.json` deve ser tratado como o bem mais precioso do sistema, com backups geridos pela Layer se necessário.
