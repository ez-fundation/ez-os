# EZ-OS: Sistema Operacional de Memória Lúdica Offline

O **EZ-OS** é um sistema operacional leve, offline e agnóstico de hardware, projetado para consoles retro Linux como o R35S, mas compatível com outros dispositivos semelhantes. Seu objetivo principal é organizar a memória de jogo, não apenas ROMs, registrando eventos reais de jogo e expressando esse histórico através de um mascote simbólico.

## ✨ Visão Geral do Projeto

O EZ-OS não é um *launcher* e não compete por performance gráfica. Ele existe para criar um grafo de memória factual dos eventos de jogo do usuário, oferecendo uma experiência única e pessoal sem depender de conectividade ou IA pesada no dispositivo. A filosofia central é que o sistema **não inventa memória**, apenas registra e expressa o que realmente aconteceu.

## 📁 Estrutura do Repositório

A estrutura de diretórios do EZ-OS é organizada para isolar domínios e facilitar a manutenção e expansão:

```
ez-os/
├── ui/             # Interface de Usuário (Terminal User Interface - TUI)
├── data/           # Armazenamento persistente de dados (e.g., grafo de memória JSON)
├── games/          # Metadados e configurações específicas de jogos
├── packs/          # Pacotes de conteúdo (e.g., temas, variações do mascote)
├── challenges/     # Definições de desafios e conquistas
├── system/         # Módulos centrais do sistema (memória, governança, mascote)
└── scripts/        # Scripts utilitários e de integração (e.g., launcher de jogos)
```

## 🚀 Como Executar

Para começar a usar o EZ-OS, siga os passos abaixo:

### 1. Instalação de Dependências

O EZ-OS utiliza a biblioteca `rich` para a construção da interface de terminal. Certifique-se de tê-la instalada:

```bash
pip install rich
```

### 2. Simulação de Eventos de Jogo

Para popular o grafo de memória com alguns eventos de exemplo, você pode usar o script `launcher.py`:

```bash
python3 scripts/launcher.py "Nome do Seu Jogo Favorito"
python3 scripts/launcher.py "Outro Jogo Clássico"
```

Este script simula o início e o fim de uma sessão de jogo, registrando os eventos no `data/memory_graph.json`.

### 3. Visualização da Interface

Após simular alguns eventos, você pode iniciar a interface do EZ-OS:

```bash
python3 ui/tui.py
```

Você verá a interface de terminal com o mascote e um log das últimas memórias registradas.

## 🧠 Princípios de Design

O desenvolvimento do EZ-OS é guiado por um conjunto de princípios não negociáveis:

1.  **Nada inventa memória**: Apenas eventos reais são registrados. A narrativa é derivada, nunca criada do zero.
2.  **Silêncio é estado padrão**: A interface fala pouco. Se não houver algo relevante, não exibe nada.
3.  **Procedural é assinatura, não mutação**: Cada jogador tem um mascote único, mas sua forma individual não afeta a lógica central do sistema.
4.  **Tudo deve sobreviver à degradação**: O sistema deve funcionar em ambientes de terminal puro, ASCII e 2-bit, sem depender de efeitos visuais complexos.
5.  **IA nunca executa no console**: O console registra e expressa; interpretações profundas acontecem fora do dispositivo (opcionalmente).

## 🛠️ Arquitetura Técnica

O sistema é dividido em quatro domínios isolados, comunicando-se exclusivamente via arquivos JSON validados:

| Domínio       | Descrição                                                              | Módulo Principal        |
| :------------ | :--------------------------------------------------------------------- | :---------------------- |
| **UI**        | Leitura simbólica e interação com o usuário via TUI.                   | `ui/tui.py`             |
| **Memória**   | Grafo factual de eventos e jogos.                                      | `system/memory.py`      |
| **Governança**| Regras de negócio e validação de dados.                                | `system/governance.py`  |
| **Execução**  | Integração com jogos e emuladores (e.g., RetroArch).                  | `scripts/launcher.py`   |

### Grafo de Memória

O grafo de memória é o coração do EZ-OS, armazenado em `data/memory_graph.json`. Ele é composto por:

-   **Nós (Nodes)**:
    -   **Game**: Representa um jogo, com ID, Título, Plataforma e Data de Adição.
    -   **Event**: Registra um evento específico (e.g., `START`, `STOP`, `ACHIEVEMENT`), com ID, GameID, Timestamp e Dados Adicionais.
    -   **User**: Contém informações do usuário, incluindo a `seed` para geração procedural do mascote.

-   **Relações (Edges)**:
    -   `PLAYED_IN`: Conecta um `Event` a um `Game`.
    -   `CHRONOLOGY`: Estabelece a ordem temporal entre `Event`s.

### Mascote (Companion)

O mascote é a representação visual do estado do grafo de memória. Seu nome e aparência (ASCII Art) são gerados deterministicamente a partir de uma `seed` do usuário. Seus estados (`Fase`, `Energia`, `Foco`) são derivados dos eventos registrados, sem simular emoções ou falas longas.

## 🎯 Critério de Sucesso

O EZ-OS será considerado bem-sucedido se:

-   Puder rodar no R35S sem esforço.
-   Continuar legível em ASCII puro.
-   Não depender de internet.
-   Não cansar o usuário.
-   Fizer sentido após meses de uso.
-   Puder ser mantido por uma pessoa só.

---

"O EZ-OS não tenta prender o jogador. Ele apenas lembra quando ele volta."
