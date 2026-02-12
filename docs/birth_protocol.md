# EZ-OS: O Protocolo de Nascimento (The Birth Protocol)

> *"Eu não tenho nome até que você me dê um."*

Para garantir a simbiose, o EZ-OS não vem com personalidade pré-definida. Ele nasce através de um **Ritual de Pastas**.

## O Conceito: Filesystem as UI
Em vez de um menu de configurações, o usuário define a alma do sistema navegando e renomeando diretórios.

## A Árvore de Decisão (`setup/`)

Quando o EZ-OS é instalado, ele gera a seguinte estrutura:

```text
setup/
├── 01_NOME_DO_SISTEMA/
│   └── [RENOMEIE_ESTA_PASTA_COM_O_NOME_ESCOLHIDO]
│
├── 02_ARQUETIPO/
│   ├── The_Guardian (Protetor, Sério)/
│   ├── The_Jester (Lúdico, Engraçado)/
│   └── The_Scholar (Analítico, Preciso)/
│   └── (Apague as pastas que você NÃO quer)
│
└── 03_FOCO_PRINCIPAL/
    ├── Memory_Keeper (Registrar o Passado)/
    └── Idea_Spark (Inspirar o Futuro)/
    └── (Mantenha apenas uma)
```

## O Ritual (Execução)

1.  O usuário clona o repo.
2.  O usuário entra em `setup/`.
3.  O usuário:
    *   Renomeia a pasta do passo 01.
    *   Deleta as opções rejeitadas dos passos 02 e 03.
4.  O usuário roda `python -m src.ez_os.birth`.

O script lê o que *sobrou* na pasta `setup/` e compila o `data/identity.json`.

## Resultado (Identity Matrix)
O sistema gera o arquivo de identidade:

```json
{
  "name": "Jarvis",
  "archetype": "The_Scholar",
  "focus": "Idea_Spark",
  "birth_date": "2026-02-12"
}
```

A partir desse momento, o "Narrative Core" ajusta seu tom de voz para combinar com o Arquétipo escolhido.

---
*Este método garante que a personalização seja um ato deliberado de "moldar" o sistema de arquivos.*
