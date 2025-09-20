import DepthLimitedSearch as DLS
def IterativeDeepeningSearch(start, goal, graph):
    limit = 0

    while True:
        result = DLS.DepthLimitedSearch(start, goal, graph, limit)
        if result is not None:
            return result
        limit +=1
    
    
graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['C'],
    'C': ['G'],
    'G': []
}


start = 'S'
goal = 'G'