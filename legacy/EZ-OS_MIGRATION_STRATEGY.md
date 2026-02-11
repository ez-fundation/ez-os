# EZ-OS: Migration Strategy (Manus → Structured Project)

> **Contexto**: O EZ-OS foi criado no Manus e está atualmente sem estrutura de projeto Python adequada.  
> **Ferramentas Aliadas**: ARKITECT (scaffolding) + DOCSYNC (documentação)  
> **Objetivo**: Transformar os módulos canônicos em um projeto Python profissional e sustentável.

---

## 🎯 Estado Atual vs. Estado Desejado

### **Estado Atual** (Manus Legacy)
```
ez-os/docs/Fundação_I/
├── tui.py
├── memory.py
├── companion.py
├── governance.py
├── launcher.py
├── indexer.py
├── gallery.py
├── symbiosis.py
└── memory_graph.json
```

**Problemas**:
- ❌ Sem `pyproject.toml` ou `requirements.txt`
- ❌ Módulos soltos sem estrutura de pacote
- ❌ Documentação fragmentada em 2 fundações
- ❌ Sem testes ou CI/CD
- ❌ Impossível instalar via `pip install -e .`

### **Estado Desejado** (Structured Project)
```
ez-os/
├── pyproject.toml          # Metadata + dependencies
├── requirements.txt        # Pinned versions
├── README.md               # Consolidated docs
├── src/
│   └── ez_os/
│       ├── __init__.py
│       ├── core/
│       │   ├── memory.py
│       │   ├── governance.py
│       │   └── companion.py
│       ├── ui/
│       │   └── tui.py
│       ├── launcher/
│       │   ├── launcher.py
│       │   └── indexer.py
│       └── extensions/
│           ├── gallery.py
│           └── symbiosis.py
├── data/
│   └── memory_graph.json
├── docs/
│   ├── architecture.md
│   ├── philosophy.md
│   └── api_reference.md
└── tests/
    └── test_core.py
```

---

## 🛠️ Estratégia de Migração (3 Fases)

### **Fase 1: Scaffolding com ARKITECT**

ARKITECT pode gerar a estrutura de projeto Python automaticamente.

#### **1.1 Criar Template de Projeto**

```bash
cd c:\Users\João\Desktop\PROJETOS\04_DEVELOPER_TOOLS\ARKITECT

# Usar ARKITECT para gerar estrutura Python
python -m arkitect.orchestrator.main create-project \
    --name "ez-os" \
    --type "python-package" \
    --template "minimal" \
    --output "../ez-os-structured"
```

#### **1.2 Configurar `pyproject.toml`**

ARKITECT pode gerar um `pyproject.toml` base. Você precisará ajustar:

```toml
[project]
name = "ez-os"
version = "1.0.0"
description = "Sistema Operacional de Memória Lúdica Offline"
authors = [{name = "João", email = "your@email.com"}]
license = {text = "MIT"}
requires-python = ">=3.9"
dependencies = [
    "rich>=13.0.0",      # Para TUI
    "pydantic>=2.0.0",   # Para validação
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
]

[build-system]
requires = ["setuptools>=68.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
```

#### **1.3 Migrar Módulos Canônicos**

```bash
# Copiar módulos para a nova estrutura
mkdir -p ez-os-structured/src/ez_os/{core,ui,launcher,extensions}

# Core
cp docs/Fundação_I/memory.py ez-os-structured/src/ez_os/core/
cp docs/Fundação_I/governance.py ez-os-structured/src/ez_os/core/
cp docs/Fundação_I/companion.py ez-os-structured/src/ez_os/core/

# UI
cp docs/Fundação_I/tui.py ez-os-structured/src/ez_os/ui/

# Launcher
cp docs/Fundação_I/launcher.py ez-os-structured/src/ez_os/launcher/
cp docs/Fundação_I/indexer.py ez-os-structured/src/ez_os/launcher/

# Extensions
cp docs/Fundação_I/gallery.py ez-os-structured/src/ez_os/extensions/
cp docs/Fundação_I/symbiosis.py ez-os-structured/src/ez_os/extensions/

# Data
mkdir -p ez-os-structured/data
cp docs/Fundação_I/memory_graph.json ez-os-structured/data/
```

---

### **Fase 2: Documentação com DOCSYNC**

DOCSYNC vai consolidar e validar toda a documentação fragmentada.

#### **2.1 Consolidar Documentação**

```bash
cd c:\Users\João\Desktop\PROJETOS\04_DEVELOPER_TOOLS\DOCSYNC

# Criar configuração de sincronização
cat > ez-os-sync.yaml << EOF
project_name: "EZ-OS"
source_dirs:
  - "../ez-os/docs/Fundação_I"
  - "../ez-os/docs/Fundação_II"
output_dir: "../ez-os-structured/docs"
rules:
  - consolidate_duplicates: true
  - validate_links: true
  - semantic_check: true
provider: "openai"  # ou "anthropic" se preferir Claude
EOF

# Executar sincronização
python run_sync.py --config ez-os-sync.yaml
```

#### **2.2 Gerar README Consolidado**

```bash
# DOCSYNC pode gerar um README profissional baseado nos docs existentes
docsync improve ../ez-os-structured/README.md \
    --instruction "Consolidate all EZ-OS documentation into a single, enterprise-ready README. Include: vision, architecture, installation, usage, and philosophy."
```

#### **2.3 Validação Semântica**

```bash
# Verificar se a documentação está consistente com o código
docsync validate ../ez-os-structured/docs \
    --code-path ../ez-os-structured/src \
    --provider openai
```

---

### **Fase 3: Finalização & Testes**

#### **3.1 Criar `__init__.py` Files**

```bash
# Tornar os diretórios em pacotes Python
touch ez-os-structured/src/ez_os/__init__.py
touch ez-os-structured/src/ez_os/core/__init__.py
touch ez-os-structured/src/ez_os/ui/__init__.py
touch ez-os-structured/src/ez_os/launcher/__init__.py
touch ez-os-structured/src/ez_os/extensions/__init__.py
```

#### **3.2 Instalar em Modo Desenvolvimento**

```bash
cd ez-os-structured
pip install -e .
```

#### **3.3 Testar Importações**

```python
# Verificar se os módulos estão acessíveis
from ez_os.core import memory, governance, companion
from ez_os.ui import tui
from ez_os.launcher import launcher, indexer
from ez_os.extensions import gallery, symbiosis

print("✅ Todos os módulos importados com sucesso!")
```

---

## 📋 Checklist de Migração

### **Pré-Migração**
- [x] Auditoria completa do estado atual (EZ-OS_PROJECT_STATE_REPORT.md)
- [ ] Backup do ZIP canônico (`ez-os-v1.0-final-agencia-integrada.zip`)
- [ ] Criar branch `migration/structured-project` no Git

### **Fase 1: ARKITECT Scaffolding**
- [ ] Gerar estrutura de projeto com ARKITECT
- [ ] Criar `pyproject.toml` e `requirements.txt`
- [ ] Migrar módulos canônicos para `src/ez_os/`
- [ ] Migrar `memory_graph.json` para `data/`

### **Fase 2: DOCSYNC Documentation**
- [ ] Consolidar documentação das duas Fundações
- [ ] Gerar README.md profissional
- [ ] Validar consistência semântica docs ↔ código
- [ ] Criar `docs/architecture.md` e `docs/philosophy.md`

### **Fase 3: Finalização**
- [ ] Criar todos os `__init__.py`
- [ ] Instalar em modo dev (`pip install -e .`)
- [ ] Testar importações
- [ ] Criar testes básicos em `tests/`
- [ ] Configurar CI/CD (GitHub Actions)

---

## 🎯 Próximos Passos Recomendados

1. **Executar Fase 1** usando ARKITECT para gerar a estrutura base
2. **Executar Fase 2** usando DOCSYNC para consolidar documentação
3. **Validar** que o projeto estruturado funciona (`pip install -e .`)
4. **Arquivar** o estado atual em `_archive/manus-legacy/`
5. **Publicar** no GitHub como `ez-os` v1.0 estruturado

---

## 🛡️ Princípios de Não-Modificação

Durante a migração, **NENHUM código será alterado**. Apenas:
- ✅ Reorganização de arquivos
- ✅ Criação de metadados (`pyproject.toml`, `__init__.py`)
- ✅ Consolidação de documentação

O **Core v1.0-FINAL** permanece imutável, conforme declarado no Documento Fundador.

---

**Criado por**: Antigravity (Migration Planning Mode)  
**Data**: 11 de Fevereiro de 2026
