# EZ-OS: Sistema Operacional de Memória Lúdica Offline

<div align="center">

[![English](https://img.shields.io/badge/Lang-English-blue)](README.md)

![EZ-OS Mascot](assets/01_mascot_base.png)

**Um sistema de memória factual para jogos retro que registra eventos reais e expressa o histórico através de um mascote procedural determinístico.**

`#python` `#retro-gaming` `#memory-system` `#procedural-generation` `#ez-fundation` `#digital-sovereignty`

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![EZ-Fundation](https://img.shields.io/badge/Part%20of-EZ--Fundation-purple)](https://github.com/ez-fundation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 🎯 O que é o EZ-OS?

O **EZ-OS** (Easy Operating System) é um Sistema Operacional de Memória Lúdica. Sua função primordial é o **registro factual de eventos de uso** e a **expressão simbólica desse histórico**, operando de forma leve, offline e agnóstica de hardware.

### Princípios Não Negociáveis

- **Factualidade da Memória**: Registra apenas eventos reais
- **Estado Padrão de Silêncio**: Comunicação apenas quando relevante
- **Identidade Procedural Determinística**: Evolução baseada em dados reais e sementes únicas
- **Resiliência à Degradação**: Funcionalidade em ASCII/2-bit
- **Isolamento de IA**: Processamento pesado é externo e opcional

---

## 🏛️ Contexto EZ-Fundation

O EZ-OS é o **Kernel de Memória Lúdica** da [EZ-Fundation](https://github.com/ez-fundation).

- **Identity**: Consome identidades do `EZ-Character`.
- **Memory**: Gera e preserva o grafo de memória do usuário.
- **Sovereignty**: Garante que os dados de "Proof of Play" pertençam ao usuário.

---

## 🚀 Instalação

### Requisitos

- Python 3.9+
- pip

### Instalação via pip (Modo Desenvolvimento)

```bash
# Clone o repositório
git clone https://github.com/ez-fundation/ez-os.git
cd ez-os

# Instale em modo desenvolvimento
pip install -e .
```

### Instalação de Dependências

```bash
pip install -r requirements.txt
```

---

## 📖 Uso

### Iniciar o EZ-OS

```bash
ez-os
```

### Uso Programático

```python
from ez_os.core import memory, companion, governance
from ez_os.ui import tui
from ez_os.launcher import launcher

# Carregar grafo de memória
graph = memory.load_graph("data/memory_graph.json")

# Atualizar estado do mascote
mascot = companion.update_state(graph)

# Renderizar TUI
tui.render(mascot, graph)
```

---

## 🏗️ Arquitetura

O EZ-OS é composto por domínios isolados:

### **Core**
- `memory.py`: Grafo factual em JSON (CRUD)
- `governance.py`: Validação e limites rígidos
- `companion.py`: Mascote procedural determinístico

### **UI**
- `tui.py`: Renderização simbólica em terminal (via `rich`)

### **Launcher**
- `launcher.py`: Launcher mínimo para integração com RetroArch
- `indexer.py`: Indexação de ROMs

### **Extensions**
- `gallery.py`: Galeria de jogos
- `symbiosis.py`: Integração simbiótica com sistemas externos

---

## 🎨 Mascote & Variações

<div align="center">

![Mascote Variations](assets/02_mascot_variations.png)

*O mascote evolui deterministicamente baseado no histórico de uso*

</div>

### **Evolução do Design**

> **Nota do Arquiteto**: A iteração v2 serve como o estudo definitivo de múltiplos ângulos para modelagem 3D.

<div align="center">
  <img src="assets/11_concept_feb07_v2.png" width="400" alt="Estudo de Design (Múltiplos Ângulos)">
  <p><em>Fig 2. Estudo de Design: Referência de Volume e Ângulos</em></p>
</div>

---

## 📚 Documentação

- [Arquitetura Técnica](docs/architecture.md)
- [Filosofia e Princípios](docs/philosophy.md)
- [Contexto EZ-Fundation](docs/ez-fundation_context.md)
- [Guia de Catalogação de Assets](docs/asset_catalog_guide.md)
- [Design de Personagem 3D](docs/character_design.md)
- [🎨 Galeria Visual & Artbook](docs/gallery.md)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia nosso guia de contribuição antes de enviar um PR.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👤 Autor

**João** - [ez-fundation](https://github.com/ez-fundation)

---

<div align="center">

*O EZ-OS não tenta prender o jogador. Ele apenas lembra quando ele volta.*

![EZ-OS Logo](assets/04_brand_logo_character.png)

</div>
