import random
def HillClimbing(start, problem_type = 'maxima', step_size=1):
    current_state = start
    while True:
        neighbours = [current_state - step_size, current_state + step_size] #left neighbour and right neighbour -> neighbour state space values(x)
        
        if problem_type == 'maxima':
            #bigger neighbour between the two
            if f(neighbours[0]) > f(neighbours[1]):
                next_state = neighbours[0]
            else:
                next_state = neighbours[1]

            if f(current_state) >= f(next_state): #if neighbours (next state) is smaller than current state
                return current_state, f(current_state)
            else: 
                current_state = next_state #climb up

        elif problem_type == 'minima': 
            #smaller neighbour between the two
            if f(neighbours[0]) < f(neighbours[1]):
                next_state = neighbours[0]
            else:
                next_state = neighbours[1]     

            if f(current_state) <= f(next_state): #if neighbours (next state) is bigger than current state
                return current_state, f(current_state)
            else: 
                current_state = next_state #climb down       

#can implement any objective function
def f(x):
    return -(x - 3) ** 2 + 9




start = random.randint(-10,10)
maxima, maxima_value = HillClimbing(start)

print(f"Start value taken is: {start}")
print(f"Maxima({maxima_value}) is found at: {maxima}")