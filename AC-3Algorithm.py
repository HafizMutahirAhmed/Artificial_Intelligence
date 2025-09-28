def AC3(domain, neighbours, constraints_satisfied):
    set_of_states = set()
    
    for Xi, all_neighbours in neighbours.items():
        for Xj in all_neighbours:
            set_of_states.add((Xi, Xj))
    
    while len(set_of_states) != 0:
        examined_arc = set_of_states.pop()
        Xi, Xj = examined_arc
        
        to_remove = []

        for domain_value_of_state in domain[Xi]:
            constraint_not_satisfied = True
            for domain_value_of_neighbour in domain[Xj]:
                if constraints_satisfied(domain_value_of_state, domain_value_of_neighbour):
                    constraint_not_satisfied = False
                    break

            if constraint_not_satisfied:
                to_remove.append(domain_value_of_state)

        for removed_domain in to_remove:    
            domain[Xi].remove(removed_domain)
            for Xk in neighbours[Xi]:
                    set_of_states.add((Xk, Xi))

        if len(domain[Xi]) == 0:
            return "No solution!"
        
    return "CSP is arch-consistent"
            


                




def constraints_satisfied(x, y):
    return x != y   # constraint: Xi > Xj

neighbours = {
    'A': ['B','C','E'],
    'B': ['A','E','F'],
    'C': ['A','E','F'],
    'D': ['F'],
    'E': ['A','B','C','F'],
    'F': ['E','D','C','B']    
}
domains = {
    'A': ['G'],
    'B': ['R'],
    'C': ['R','G','B','Y'],
    'D': ['R','G','B','Y'],
    'E': ['R','G','B','Y'],
    'F': ['R','G','B','Y'],
}

print(AC3(domains, neighbours, constraints_satisfied))
print(domains)
