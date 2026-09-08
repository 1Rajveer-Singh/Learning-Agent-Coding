import heapq

def a_star_search(graph, start, goal, heuristic):
    """
    Performs A* search to find the shortest path from start to goal.
    
    :param graph: Dict where keys are nodes and values are dicts of neighbors {neighbor: cost}
    :param start: The starting node
    :param goal: The target node
    :param heuristic: A function that estimates the cost from a node to the goal
    :return: A list of nodes representing the shortest path, or None if no path exists
    """
    # Priority queue stores tuples: (f_score, current_node)
    # f_score = g_score (cost from start) + h_score (heuristic to goal)
    open_set = [(heuristic(start), start)]
    
    # Track the best path to reach a node
    came_from = {}
    
    # g_score[n] is the cost of the cheapest path from start to n currently known
    g_score = {start: 0}
    
    while open_set:
        # Get the node with the lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, weight in graph.get(current, {}).items():
            tentative_g_score = g_score[current] + weight
            
            # If this path to neighbor is better than any previous one
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))
                
    return None  # Path not found