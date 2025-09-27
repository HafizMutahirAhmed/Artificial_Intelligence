def UniformCostSearch(start, goal, graph):
    if start == goal:
        return '0'+start
    
    frontier = [[0, start]]
    while frontier:
        frontier.sort()
        path_cost, path = frontier.pop(0)
        current_node = path[-1]

        if current_node == goal:
            return str(path_cost)+path
        
        for successor, step_cost in graph.get(current_node, []):
            if successor == goal:
                return str(step_cost+path_cost) + (path+successor)
            frontier.append([step_cost+path_cost, path+successor])
    return None


graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 4), ('D', 1)],
    'B': [('D', 7)],
    'C': [('G', 2)],     # Path: S → A → C → G = 9
    'D': [('G', 2)],     # Path: S → A → D → G = 6  (best)
    'G': []
}


print(UniformCostSearch('S', 'G', graph))
