import os
import numpy as np
full_path = os.path.join(os.getcwd(),'Input/Day6_Input.txt')
file = open(full_path,'r')
data = file.read()
data = data.split('\n')
### Part 1
t = [int(s) for s in data[0].split(' ') if s.isdigit()]
d = [int(s) for s in data[1].split(' ') if s.isdigit()]
prod = 1
for i in range(0,len(t)):
    t_lb = int(np.ceil((-t[i] + ((t[i] ** 2 - (4 * d[i])) ** (1 / 2))) / (-2)))
    t_ub = int(np.floor((-t[i] - ((t[i] ** 2 - (4 * d[i])) ** (1 / 2))) / (-2)))
    prod *= (t_ub-t_lb+1)
print(prod)
### Part 2
t = int(''.join([s for s in data[0].split(' ') if s.isdigit()]))
d = int(''.join([s for s in data[1].split(' ') if s.isdigit()]))
t_lb = int(np.ceil((-t + ((t** 2 - (4 * d)) ** (1 / 2))) / (-2)))
t_ub = int(np.floor((-t- ((t** 2 - (4 * d)) ** (1 / 2))) / (-2)))
print(t_ub-t_lb+1)