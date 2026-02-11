# Arquitetura Simbiótica Canônica

A arquitetura de um Sistema de Memória Simbiótica deve seguir a separação rigorosa entre o que é imutável (Core) e o que é adaptativo (Layer).

## 1. O Core Congelado (Imutável)
O Core deve conter apenas o essencial para a existência do sistema:
- **Grafo de Memória**: Estrutura de dados factual e append-only.
- **Governança**: Regras de silêncio e limites de segurança.
- **Companheiro Lógico**: Renderizador de estado determinístico.
- **Launcher Mínimo**: Registro de eventos START/STOP.

## 2. A Layer de Adaptação (Hospedeiro)
A Layer é responsável por "hospedar" o Core em um hardware específico:
- **Tradução de Eventos**: Mapeia ações do hardware para o Core.
- **Persistência Local**: Gere o armazenamento físico do grafo.
- **Interface Contextual**: Renderiza o estado do Core de acordo com as capacidades do display (ASCII, E-Ink, Framebuffer).

## 3. Fluxo de Simbiose
1. O Hardware gera um evento.
2. A Layer intercepta e notifica o Core via Launcher.
3. O Core valida via Governança e anexa ao Grafo.
4. O Companheiro atualiza seu estado simbólico.
5. A Layer renderiza o novo estado para o humano.
