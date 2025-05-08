# Degrees of Separation / Graus de Separação

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![CS50AI](https://img.shields.io/badge/CS50-AI-green)

## 🇺🇸 Implementation Overview
**My contribution** was exclusively implementing the `shortest_path()` function in `degrees.py` using Breadth-First Search (BFS). The remaining codebase was provided by CS50.

### Algorithm Choice: BFS
- **Optimal Solution**: Guarantees shortest path
- **Frontier**: Uses queue (FIFO) structure
- **Explored Set**: Prevents cycles and redundant checks
- **Path Reconstruction**: Backtracks through parent nodes

### Key Components
| Concept | Implementation |
|---------|----------------|
| States | Actor IDs |
| Actions | Movies connecting actors |
| Transition Model | `neighbors_for_person()` function |
| Goal Test | Matching target actor ID |
| Path Cost | Number of movies in path |

## 🇧🇷 Visão da Implementação
**Minha contribuição** foi exclusivamente a implementação da função `shortest_path()` em `degrees.py` usando Busca em Largura (BFS). O restante do código foi fornecido pelo CS50.

### Escolha do Algoritmo: BFS
- **Solução Ótima**: Garante o caminho mais curto
- **Fronteira**: Usa estrutura de fila (FIFO)
- **Conjunto Explorado**: Evita ciclos e verificações redundantes
- **Reconstrução do Caminho**: Retrocede através dos nós pais

### Componentes Principais
| Conceito | Implementação |
|---------|----------------|
| Estados | IDs de atores |
| Ações | Filmes conectando atores |
| Modelo de Transição | Função `neighbors_for_person()` |
| Teste de Objetivo | Correspondência de ID do ator alvo |
| Custo do Caminho | Número de filmes no caminho |
