## Search Algorithms / Algoritmos de Busca

### 🇺🇸 Theory Overview
Search problems involve finding a path from an initial state to a goal state. Key components include:
- **Agent**: Entity that perceives and acts (e.g., navigation app)
- **States**: Configurations (e.g., puzzle arrangements)
- **Actions**: Possible moves in a state
- **Transition Model**: Results of actions
- **Goal Test**: Checks if state is the solution
- **Path Cost**: Metric to optimize (e.g., time/distance)

#### Common Algorithms:
1. **Depth-First Search (DFS)**
   - Explores one path fully before backtracking
   - Uses stack (LIFO)
   - Pros: Fast if lucky | Cons: May find suboptimal solutions

2. **Breadth-First Search (BFS)**
   - Explores all directions equally
   - Uses queue (FIFO)
   - Pros: Guaranteed optimal solution | Cons: Slower

3. **A* Search**
   - Combines actual cost (g(n)) + heuristic (h(n))
   - Optimal with admissible/consistent heuristics
   - Example heuristic: Manhattan distance

### 🇧🇷 Visão Teórica
Problemas de busca envolvem encontrar um caminho do estado inicial ao objetivo. Componentes:
- **Agente**: Entidade que percebe e age (ex: app de navegação)
- **Estados**: Configurações (ex: arranjos de quebra-cabeça)
- **Ações**: Movimentos possíveis
- **Modelo de Transição**: Resultado das ações
- **Teste de Objetivo**: Verifica se estado é solução
- **Custo do Caminho**: Métrica a otimizar

#### Algoritmos Principais:
1. **Busca em Profundidade (DFS)**
   - Explora um caminho completamente antes de voltar
   - Último a entrar, primeiro a sair
   - Vantagem: Rápido se tiver sorte | Desvantagem: Solução subótima

2. **Busca em Largura (BFS)**
   - Explora todas as direções igualmente
   - Usa fila -> primeiro a entrar, primeiro a sair
   - Vantagem: Solução ótima garantida | Desvantagem: Mais lento

3. **A* (A-estrela)**
   - Combina custo real (g(n)) + heurística (h(n))
   - Ótimo com heurísticas admissíveis/consistentes
   - Exemplo: Distância de Manhattan

### Applications / Aplicações
- Navigation systems / Sistemas de navegação
- Puzzle solving / Resolução de quebra-cabeças
- Pathfinding in games / Caminhos em jogos
- Robotics planning / Planejamento robótico
