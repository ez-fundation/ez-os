# Matriz Comparativa de Dispositivos Edge (Referência EZ-OS)

Esta matriz avalia a viabilidade de hospedar o EZ-OS Core v1.0-FINAL como camada de memória simbiótica em diferentes ecossistemas.

| Dispositivo | Categoria | O que ensina (Arquitetura) | O que NÃO herdar | Compatibilidade |
| :--- | :--- | :--- | :--- | :--- |
| **Raspberry Pi (Zero/4/5)** | Laboratório / Geral | Versatilidade total e GPIO como sensor de simbiose. | Complexidade de SO desktop e overhead de boot. | **Alta** |
| **Playdate** | Handheld (Lúdico) | Foco em restrição física (manivela) e 1-bit display. | SDK proprietário fechado e falta de multi-tasking. | **Média** |
| **Analogue Pocket** | Handheld (FPGA) | Fidelidade absoluta ao hardware original (Factualidade). | Opacidade do hardware (FPGA é difícil de interceptar). | **Baixa** |
| **reMarkable / Kindle** | Leitura (E-Ink) | Silêncio visual radical e foco em estado, não ação. | Taxa de atualização lenta (Ghosting) e DRM. | **Alta** |
| **Steam Deck** | Handheld (PC) | Shell como camada de abstração sobre SO complexo. | Bloatware, telemetria e excesso de performance. | **Média** |
| **OpenWRT Devices** | Infraestrutura | Existência invisível, 24/7, resiliente e headless. | Foco em throughput e conectividade constante. | **Alta** |

## Análise de Compatibilidade
- **Alta**: Dispositivos que permitem interceptação de eventos via shell e possuem displays de baixo consumo ou terminais.
- **Média**: Dispositivos com barreiras de software (SDKs fechados) ou excesso de funcionalidades que competem com o silêncio.
- **Baixa**: Sistemas fechados ou baseados em hardware que não expõe eventos factuais de uso ao software.
