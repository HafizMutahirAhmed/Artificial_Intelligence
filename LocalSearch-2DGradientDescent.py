import matplotlib.pyplot as plt
import numpy as np
from math import log

def GradientDescent(derivative_func, learning_rate=0.02, initial_value=0.5, precision=0.001, max_iter=300):
    t = initial_value
    t_list = []

    for i in range(1, max_iter + 1):
        t_list.append(t)
        t = t  - learning_rate * derivative_func(t)
        if abs(learning_rate * derivative_func(t)) <= precision:
        # if derivative_func(t) == 0:
            return t, t_list, i
        
# #Implementing the function g(t)
# def g(t):
#     return t**4-4*t**2+5

# #Implementing the derivative of the function g(t)
# def dg(t):
#     return 4*t**3-8*t

# t_1=np.linspace(-2,2,1000)
# print(t_1)
# plt.figure(figsize=(8,5))
# plt.plot(t_1,g(t_1))
# plt.xlabel('t', fontsize=14)
# plt.ylabel('g(t)', fontsize=14)
# plt.title('Cost function')
# plt.show()

# local_minima, t_list, runs = GradientDescent(dg, initial_value=0.5, learning_rate=0.02, max_iter=1000, precision=0.0001)

# print('Local minima occurs at', local_minima)
# print('Cost at this point is', g(local_minima))
# print('Slope at this point is', dg(local_minima))
# print('Loop runs this many times:', runs)

# #Plotting search trace on cost function
# plt.figure(figsize=(8,5))
# plt.plot(t_1,g(t_1))
# plt.xlabel('t', fontsize=14)
# plt.ylabel('g(t)', fontsize=14)
# plt.title('Cost function')
# plt.scatter(t_list, g(np.array(t_list)), color='red',alpha=0.4)
# plt.show()

def h(t):
    return t**5-2*t**4+2

#Implementing the derivative of the function h(x)
def dh(t):
    return 5*t**4-8*t**3

#Making data
t_2=np.linspace(-2.5,2.5,1000)

#Visualizing the function
plt.figure(figsize=(8,5))
plt.xlim(-1.2, 2.5)
plt.ylim(-1, 4)
plt.plot(t_2,h(t_2))
plt.xlabel('t', fontsize=14)
plt.ylabel('h(t)', fontsize=14)
plt.title('Cost function')
plt.show()

#Running gradient descent and plotting the results
local_minima,t_list,runs = GradientDescent(dh,initial_value= -0.8, learning_rate= 0.02, precision= 0.001,max_iter= 9)
    
print('Local minima occures at ', local_minima)
print('Cost at this point is ', h(local_minima))
print('Slope at this point is ', dh(local_minima))
print('Loop runs this many times: ', runs)

plt.figure(figsize=(8,5))
plt.xlim(-1.2, 2.5)
plt.ylim(-1, 4)
plt.plot(t_2,h(t_2))
plt.xlabel('t', fontsize=14)
plt.ylabel('h(t)', fontsize=14)
plt.title('Cost function')
plt.scatter(t_list,h(np.array(t_list)), color='red',alpha=0.4)
plt.show()