# EZ-OS — Sistema Operacional de Memória Lúdica Offline

## Documento Canônico de Consolidação v1.0

**Autor:** Manus AI

--- 

### 1. Introdução

Este documento tem como objetivo consolidar e apresentar o **EZ-OS (Easy Operating System)**, um sistema operacional experimental projetado para organizar a memória lúdica de jogos. O EZ-OS é um sistema leve, offline e agnóstico de hardware, desenvolvido inicialmente para consoles retro Linux, como o R35S, mas com compatibilidade estendida a dispositivos similares. Diferente de um *launcher* tradicional, o EZ-OS não foca em performance gráfica, mas sim na criação de um grafo factual de memória a partir de eventos reais de jogo, expressos por meio de um mascote simbólico e uma interface de terminal minimalista.

O propósito deste documento não é propor novas funcionalidades ou redefinir a filosofia do projeto, mas sim organizar, explicar e validar o que já foi implementado, garantindo clareza, coerência e viabilidade técnica e institucional. A linguagem utilizada é técnica, objetiva e auditável, refletindo a natureza do sistema.

### 2. Visão Geral do Sistema

O EZ-OS opera como um Sistema Operacional de Memória Lúdica, fundamentado nos seguintes princípios:

*   **Registro de Eventos Reais**: Apenas eventos genuínos de jogo são registrados, sem invenção ou inferência de memória.
*   **Grafo Factual de Memória**: Manutenção de uma estrutura de dados que representa o histórico de jogo de forma imutável e verificável.
*   **Expressão Simbólica e Não Invasiva**: O histórico é comunicado através de um mascote e uma interface que não pressiona o usuário, valorizando pausas e retornos voluntários.
*   **Operação 100% Offline**: Independência total de conectividade com a internet para seu funcionamento principal.
*   **Ausência de IA Pesada no Dispositivo**: A inteligência artificial, quando presente, opera fora do console, mantendo o sistema leve e focado em registro e expressão.
*   **Sustentabilidade e Manutenibilidade**: Projetado para ser mantido por uma única pessoa, garantindo a longevidade do projeto.

O sistema foi concebido para aceitar paases e lembrar quando o jogador retorna, sem criar dependência artificial ou pressionar por engajamento contínuo.

### 3. Principais Entregas Implementadas

As seguintes funcionalidades e estruturas foram implementadas no EZ-OS:

#### 3.1. Arquitetura Canônica

O sistema foi estruturado em domínios isolados, que se comunicam exclusivamente através de arquivos JSON validados. Essa separação promove auditabilidade, clareza e uma evolução segura do projeto.

| Domínio       | Descrição                                                              | Módulo Principal        |
| :------------ | :--------------------------------------------------------------------- | :---------------------- |
| **UI**        | Leitura simbólica e interação com o usuário via TUI.                   | `ui/tui.py`             |
| **Memória**   | Grafo factual de eventos e jogos.                                      | `system/memory.py`      |
| **Governança**| Regras de negócio e validação de dados.                                | `system/governance.py`  |
| **Execução**  | Integração com jogos e emuladores (e.g., RetroArch).                  | `scripts/launcher.py`   |

#### 3.2. Grafo de Memória Factual

O grafo de memória é o componente central do EZ-OS, armazenado em `data/memory_graph.json`. Ele é composto por:

*   **Nós (Nodes)**:
    *   **User**: Representa a identidade local do usuário e sua `seed` procedural.
    *   **Game**: Contém metadados do jogo (título, plataforma, ano, etc.).
    *   **Event**: Registra eventos reais como `START`, `STOP`, `ACHIEVEMENT`, entre outros.

*   **Relações (Edges)**:
    *   `PLAYED_IN`: Conecta um `Event` a um `Game`.
    *   `CHRONOLOGY`: Estabelece a ordem temporal entre os `Event`s.

O grafo é imutável por padrão, garantindo que as narrativas sejam derivadas dos dados existentes, e nunca inventadas.

#### 3.3. Mascote Simbólico (Companion)

O mascote do EZ-OS atua como um leitor do grafo de memória, sem ser um decisor. Sua representação prioritária é em ASCII Art, gerada de forma procedural determinística a partir da `seed` do usuário. O mascote evolui por fases claras (e.g., Ovo → Jovem → Adulto → Sábio), refletindo o tempo de vida do sistema e a quantidade de eventos registrados. Ele não simula emoções humanas nem se engaja em falas longas, expressando o tempo vivido de forma simbólica.

#### 3.4. Interface TUI (Terminal User Interface)

A interface foi desenvolvida em Python, utilizando a biblioteca `rich`, com foco nos seguintes aspectos:

*   **Silêncio como Estado Padrão**: A UI não força interação, respondendo apenas quando há informações relevantes a serem exibidas.
*   **Estética Retro-futurista**: Alto contraste e cores planas, sem fotorealismo ou excesso de brilho.
*   **Legibilidade em Ambientes Degradados**: Totalmente funcional em ASCII puro e ambientes de 2-bit.
*   **Layout Simples**: Composto por um menu lateral minimalista, uma área central para estados/memória e o mascote sempre visível.

#### 3.5. Launcher de Integração

Um script de *launcher* foi implementado para simular o início e o fim de sessões de jogo, registrando automaticamente eventos `START` e `STOP` e atualizando o grafo de memória. Isso permite testar o sistema em ambiente local sem a necessidade de emuladores externos, facilitando o desenvolvimento e a validação.

### 4. Estrutura do Projeto

A organização do projeto segue uma árvore de diretórios clara e canônica:

```
ez-os/
├── ui/             # Interface TUI
├── data/           # Grafo de memória e estados persistentes
├── games/          # Metadados de jogos
├── packs/          # Pacotes futuros de conteúdo (e.g., temas, variações do mascote)
├── challenges/     # Definições de desafios e conquistas
├── system/         # Módulos centrais (memória, governança, mascote, indexador)
└── scripts/        # Launcher e utilitários
```

O arquivo `ez-os_v1.0.zip` contém a implementação completa, funcional e organizada do projeto.

### 5. Fontes de Jogos e Bases de Dados (Camada de Indexação e Metadados)

O EZ-OS não hospeda, distribui ou baixa jogos automaticamente. Ele funciona como um sistema de indexação, organização e memória, operando sobre arquivos fornecidos pelo próprio usuário. Para isso, o sistema utiliza bases de dados públicas e abertas exclusivamente para metadados, identificação e enriquecimento semântico dos jogos, sempre com uma abordagem juridicamente neutra e tecnicamente precisa.

#### 5.1. Tipos de Bases Utilizadas

O EZ-OS distingue claramente três camadas de dados:

*   **Camada A — Arquivos Locais (Usuário)**:
    *   ROMs e ISOs fornecidos manualmente pelo usuário.
    *   Dumps pessoais de cartuchos/discos.
    *   Backups legítimos.
    *   **Princípio**: O EZ-OS nunca assume a origem dos arquivos nem executa downloads automáticos.

*   **Camada B — Bases Públicas de Metadados**:
    *   Utilizadas apenas para informações como nome oficial, plataforma, ano, gênero, *publisher* e identificação por *hash*.
    *   **Princípio**: Nenhum conteúdo jogável é obtido dessas fontes.

*   **Camada C — Bases Comunitárias (Opcional)**:
    *   Usadas para enriquecimento visual (capas, quando permitido) e descrições curtas ou dados históricos.
    *   **Princípio**: Sempre com *fallback* para o modo offline e dependente da permissão do usuário.

#### 5.2. Bases de Dados Canônicas (Aprovadas)

O EZ-OS integra-se com as seguintes bases de dados para metadados:

| Base de Dados         | Uso Principal                                  | Formato      | Status                                   | Observações                                     |
| :-------------------- | :--------------------------------------------- | :----------- | :--------------------------------------- | :---------------------------------------------- |
| **Libretro Database** | Metadados oficiais e compatibilidade           | JSON / DAT   | Open-source, amplamente adotada          | Base padrão do ecossistema RetroArch.           |
| **No-Intro Database** | Identificação por *hash* (ROMs de cartucho)    | DAT          | Comunitária, amplamente reconhecida      | Usada como referência técnica, não para distribuição. |
| **Redump Database**   | Identificação de mídias ópticas (CD/DVD)       | DAT          | Comunitária                              | Para sistemas baseados em disco (PlayStation, Sega CD, etc.). |
| **IGDB / OpenGameArt**| Enriquecimento semântico (opcional)            | API / JSON   | Opcional, nunca obrigatória              | Utilizada apenas com conectividade e permissão do usuário. |

#### 5.3. Pipeline de Indexação no EZ-OS

O processo de indexação é determinístico e auditável:

1.  **ROM fornecida pelo usuário**
2.  **Cálculo de *hash*** (CRC / SHA1)
3.  **Consulta a bases de metadados** (locais ou online, se permitido)
4.  **Criação do nó "Game" no grafo**
5.  **Associação futura com eventos reais**

É crucial ressaltar que nenhuma ROM é copiada, enviada ou modificada pelo sistema.

#### 5.4. Integração com o Grafo de Memória

As bases de dados não escrevem memória; elas apenas definem a identidade do jogo. A memória só é criada quando eventos reais de jogo ocorrem. Um exemplo de nó `Game` no grafo seria:

```json
{
  "id": "game_smw_snes",
  "name": "Super Mario World",
  "platform": "SNES",
  "year": 1990,
  "source": "No-Intro",
  "hash": "A1B2C3...",
  "memory_bound": false
}
```

### 6. Governança e Conformidade

O EZ-OS adota um conjunto rigoroso de regras para garantir a conformidade e a ética:

*   ❌ Não hospeda ROMs.
*   ❌ Não aponta para downloads ilegais.
*   ❌ Não faz *scraping* agressivo.
*   ✅ Usa apenas metadados públicos.
*   ✅ Respeita o modo offline.
*   ✅ Dá controle total ao usuário sobre suas fontes de dados.

Essas decisões são estruturais e não opcionais, refletindo o compromisso do projeto com a legalidade e a privacidade do usuário.

### 7. Benefícios da Abordagem

A arquitetura e os princípios do EZ-OS oferecem diversos benefícios:

*   **Portabilidade Internacional**: Facilita a adoção em diferentes regiões sem barreiras legais.
*   **Segurança Jurídica**: Minimiza riscos relacionados a direitos autorais e distribuição de conteúdo.
*   **Sustentabilidade de Longo Prazo**: A independência de serviços online e a leveza do sistema garantem sua viabilidade futura.
*   **Facilidade de Manutenção**: A modularidade e a comunicação via JSON simplificam atualizações e correções.
*   **Compatibilidade com RetroArch e Forks**: Integração facilitada com o ecossistema de emulação existente.

### 8. Filosofia Implementada

O EZ-OS foi construído seguindo princípios não negociáveis, que já estão refletidos no código e na documentação:

*   **Nada inventa memória**.
*   **Silêncio é o padrão**.
*   **Procedural é identidade, não mutação**.
*   **Tudo deve sobreviver à degradação** (ASCII, 2-bit).
*   **IA nunca executa no console**.

### 9. Estado Atual do Projeto

O EZ-OS encontra-se em um estado de maturidade considerável:

*   ✅ Implementado.
*   ✅ Executável em ambiente local.
*   ✅ Pronto para testes contínuos.
*   ✅ Preparado para portabilidade futura (R35S ou similares).
*   ✅ Conceitualmente estável.

Não se trata de um protótipo de ideia, mas sim de um sistema funcional em evolução controlada.

### 10. Frase-Âncora do Sistema

"O EZ-OS não tenta prender o jogador. Ele apenas lembra quando ele volta."

### 11. Frase-Âncora (Bases de Dados)

"O EZ-OS não coleciona jogos. Ele reconhece o que o jogador já possui."
