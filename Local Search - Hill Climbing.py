import random
def HillClimbing(start, step_size=1):
    current_state = start
    while True:
        neighbours = [current_state - step_size, current_state + step_size] #left neighbour and right neighbour -> neighbour state space values(x)
        #bigger neighbour between the two
        if f(neighbours[0]) > f(neighbours[1]):
            next_state = neighbours[0]
        else:
            next_state = neighbours[1]


        if f(current_state) >= f(next_state): #if neighbours (next state) is worse than current state
            return current_state, f(current_state)
        else: 
            current_state = next_state #climb up
        
#can implement any function
def f(x):
    return -(x - 3) ** 2 + 9

start = random.randint(-10,10)
print(f"Start value taken is: {start}")
maxima, maxima_value = HillClimbing(start)
print(f"Maxima({maxima_value}) is found at: {maxima}")