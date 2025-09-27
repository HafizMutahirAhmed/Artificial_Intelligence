from math import exp
from random import randint

#ALGO used in VLSI Layout Design

def SimulatedAnnealing(initial_state, intial_temp, step_size = 1, cooling_factor=0.9, probability=0.5):
    current_state = initial_state
    current_temp = intial_temp

    while current_temp > 0.0000000000001:
        neighbours = [current_state - step_size, current_state + step_size]
         
        next_state = neighbours[randint(0, 1)] #randomly selected neighbour(successor) of current
        
        deltaE = f(next_state) - f(current_state) #if +ve -> graph going upwards, if -ve -> graph going downwards

        if deltaE > 0: #if deltaE = +ve
            current_state = next_state
        
        elif exp(deltaE/current_temp) > probability: #if deltaE = -ve and within the probability range set
                current_state = next_state
        
        #reduce the temperate by amount cooling_factor
        current_temp *= cooling_factor
    return current_state, f(current_state)
            

def f(x):
    return -(x - 3) ** 2 + 9  # peak at x=3, value=9

initial_state = randint(-10,10)
maxima, maxima_value = SimulatedAnnealing(initial_state, 50)
print(f"Initial Value selected is {initial_state}")
print(f"Maxima ({maxima}) is found at {maxima_value}")
