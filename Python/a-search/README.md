# A* search

## 💡 Overview & Approach
A* search is an informed search algorithm that finds the shortest path between nodes in a weighted graph. It improves upon Dijkstra's algorithm by using a heuristic function $h(n)$ to guide the search towards the goal, effectively prioritizing nodes that appear closer to the target.

The algorithm maintains two primary structures: a priority queue (`open_set`) to explore the most promising nodes first based on $f(n) = g(n) + h(n)$, and a dictionary (`g_score`) to track the minimum cost to reach each node. By continuously expanding the node with the lowest $f(n)$, A* balances the cost already incurred ($g$) with the estimated remaining cost ($h$), ensuring optimality provided the heuristic is admissible (never overestimates the true cost).

## 📊 Complexity Analysis
- **Time Complexity**: $O(E \log V)$, where $E$ is the number of edges and $V$ is the number of vertices. Each edge is processed at most once, and heap operations take logarithmic time relative to the number of nodes in the priority queue.
- **Space Complexity**: $O(V)$, as we store the `g_score` and `came_from` mappings for each vertex, and the priority queue can hold up to $V$ vertices in the worst case.

## 🏢 Top Companies Asking This Problem
- Google (Maps/Navigation)
- Uber (Routing/ETA)
- Meta (Social Graph traversal)
- Amazon (Logistics/Warehouse robotics)
- Microsoft (Pathfinding in gaming/AI)

## 🚀 Key Features & Edge Cases Handled
- **Optimality**: Guarantees the shortest path if the heuristic is admissible.
- **Efficiency**: Uses `heapq` for $O(\log N)$ insertion and extraction, ensuring high performance.
- **Disconnected Graphs**: Returns `None` gracefully if the goal node is unreachable from the start.
- **Dynamic Weights**: Handles varying edge weights correctly, unlike Breadth-First Search.
- **Memory Efficiency**: Only stores necessary path information, avoiding redundant state exploration.