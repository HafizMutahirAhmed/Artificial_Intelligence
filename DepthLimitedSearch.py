def DepthLimitedSearch(start, goal, graph, limit):
    if start == goal:
        return start
    
    frontier = [start]
    reached = [start]

    while frontier:
        current_node_path = frontier.pop()
        current_node = current_node_path[-1]
        depth = len(current_node_path) - 1
        if depth < limit:
            for successor in graph.get(current_node, []):
                if successor not in reached:
                    if successor == goal:
                        return current_node_path + successor
                    frontier.append(current_node_path + successor)
                    reached.append(successor)
    return None


graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['C'],
    'C': ['G'],
    'G': []
}


start = 'S'
goal = 'G'

result = DepthLimitedSearch(start, goal, graph,4)
if result is None:
    print('Goal not Reached!')
else:
    print(f'Goal {result} Reached!')
                



