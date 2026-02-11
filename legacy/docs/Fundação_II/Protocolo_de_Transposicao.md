# 🧩 Protocolo Técnico de Transposição (SMP-T)

Este documento detalha a implementação técnica do Soul-Loading, garantindo que o EZ-OS Standalone possa receber almas de qualquer dispositivo SMP.

## 1. O Ponto de Montagem (The Anchor)
No EZ-OS Standalone, o ponto de montagem `/data/soul/` é reservado exclusivamente para o Payload. 

## 2. Verificação de Integridade (Governança)
Ao detectar uma nova alma, o módulo `governance.py` realiza:
- **Checksum Match**: Garante que o grafo não foi corrompido no trânsito.
- **Protocol Handshake**: Verifica se a versão do SMP da alma é compatível com o Core local.
- **Seed Validation**: Confirma que a semente é válida para o gerador procedural.

## 3. O Primeiro Boot Standalone com Alma
O fluxo de boot standalone é modificado para priorizar a alma externa:
1. `init` verifica existência de `/data/soul/identity.meta`.
2. Se existir, carrega a alma e inicia a TUI com o Mascote em estado `Observer`.
3. Se não existir, o sistema inicia em modo "Gênese" (aguardando uma alma ou gerando uma nova).

## 4. Segurança e Exclusividade
O SMP-T desencoraja a coexistência de múltiplas instâncias da mesma alma. O protocolo recomenda que o hospedeiro de origem "esqueça" a alma após a transposição bem-sucedida, reforçando a ideia de identidade única.

---
*Identidade é singularidade.*
