# Síntese Estratégica e Perfil de Hardware Hospedeiro

## 1. Top 3 Alvos de Adaptação (Além de Consoles)

| Alvo | Motivação Técnica | Coerência Filosófica | Potencial Estratégico |
| :--- | :--- | :--- | :--- |
| **1. Dispositivos E-Ink (reMarkable/Kindle)** | Baixo consumo, persistência visual sem brilho. | O "Estado de Silêncio" absoluto. O mascote vive na tinta estática. | Transforma o leitor em um repositório de memória de leitura. |
| **2. Micro-Servidores Headless (OpenWRT/Pi Zero)** | Operação 24/7, sem interface gráfica obrigatória. | "Existência Invisível". O EZ-OS como guardião da rede. | Torna-se o primitivo de memória da infraestrutura doméstica. |
| **3. Terminais de Escrita (Alphasmart/Pomera)** | Foco em input único, distração zero. | "Anti-dependência por design". Respeito ao tempo de criação. | Camada de simbiose para ferramentas de produtividade "burras". |

## 2. Perfil de Hardware Hospedeiro Ideal

O EZ-OS Core v1.0-FINAL é propositalmente leve para garantir essa portabilidade.

### Requisitos Mínimos
- **CPU**: ARM v7 ou superior (mínimo 300MHz). Deve suportar interpretador Python 3.
- **RAM**: 64MB (O Core ocupa < 10MB em runtime).
- **Armazenamento**: 1MB livre para o Core + Espaço para o Grafo (JSON).

### Requisitos de Interface (Simbiose)
- **Display**: Suporte a modo texto (TTY) ou Framebuffer. Ideal para E-Ink ou LCDs monocromáticos.
- **Input**: Mínimo de 3 botões (Cima, Baixo, Seleção) ou entrada serial.
- **Conectividade**: Nenhuma necessária (Offline por design).

### Dependências de Sistema
- Kernel Linux (preferencial) ou RTOS que suporte Python.
- Bibliotecas: `json`, `hashlib`, `uuid`, `datetime` (Standard Lib).
- Opcional: `rich` para a TUI canônica (pode ser substituído por print simples se necessário).
