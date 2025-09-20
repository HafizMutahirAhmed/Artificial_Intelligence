from collections import deque as queue

def BreadthFirstSearch(start, goal, graph):
    if start == goal:
        return start
    
    frontier = queue([start]) #initial F <- S
    reached = [start] #mark S as reached
    while frontier:
        N = frontier.popleft() #pops from the top cuz FIFO
        for successor in graph.get(N, []):
            if successor not in reached:
                if successor == goal:
                    return successor
                frontier.append(successor)
                reached.append(successor)
    
    return None


graph = {
    'S':['A','B','D'],
    'A':['C'],
    'B':['D'],    
    'C':['D','G'],
    'D':['G'],
    'G':[]
}

start = 'S'
goal = 'G'

result = BreadthFirstSearch(start, goal, graph)
if result is None:
    print('Goal not Reached!')
else:
    print(f'Goal {result} Reached!')

