import matplotlib.pyplot as plt
import numpy as np
from math import log

def GradientDescent(partial_derivative1, partial_derivative2, initial_value1=1.8, initial_value2=1.5, learning_rate=0.1, max_iteration=20000):
    t1 = initial_value1
    t2 = initial_value2
    t1_list = []
    t2_list = []

    for i in range(1, max_iteration + 1):
        t1_list.append(initial_value1)
        t2_list.append(initial_value2)

        new_t1 = t1 - learning_rate * partial_derivative1(t1, t2)
        new_t2 = t2 - learning_rate * partial_derivative2(t1, t2)

        t1 = new_t1
        t2 = new_t2

    return t1_list, t2_list

def f(t1,t2):
    return 1/(3**(-t1**2-t2**2)+1)

def partial_derivative1(t1,t2):
    return 2*t1*log(3)*(3**(-t1**2-t2**2))/(3**(-t1**2-t2**2)+1)**2
def partial_derivative2(t1,t2):
    return 2*t2*log(3)*(3**(-t1**2-t2**2))/(3**(-t1**2-t2**2)+1)**2



#Making data for t1 and t2
t1=np.linspace(-2,2,200)
t2=np.linspace(-2,2,200)
t1,t2=np.meshgrid(t1,t2) 
#meshgrid converts t1 and t2 into 2D arrays, as required by the plotting function plot_surface.
#Plotting a 3D graph
fig=plt.figure(figsize=[16,12])
ax=plt.axes(projection='3d')
ax.set_xlabel('t1', fontsize=16)
ax.set_ylabel('t2', fontsize=16)
ax.set_zlabel('Cost - f(t1,t2)', fontsize=16)
ax.plot_surface(t1,t2,f(t1,t2), alpha=0.4, cmap='summer') 
#Explore other colormaps
#Website for color choices: materialpalette.com
plt.show()

#Plotting the 3D graph
fig=plt.figure(figsize=[16,12])
ax=plt.axes(projection='3d')
ax.set_xlabel('t1', fontsize=16)
ax.set_ylabel('t2', fontsize=16)
ax.set_zlabel('Cost - f(t1,t2)', fontsize=16)
ax.plot_surface(t1,t2,f(t1,t2), alpha=0.4, cmap='summer')

t1_list, t2_list = GradientDescent(partial_derivative1, partial_derivative2)

t1_list=np.array(t1_list)
t2_list=np.array(t2_list)
ax.scatter(t1_list,t2_list,f(t1_list,t2_list), alpha=0.4, s=50, color='red')
plt.show()