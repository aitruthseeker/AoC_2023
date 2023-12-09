import os
import numpy as np
full_path = os.path.join(os.getcwd(),'Input/Day9_Input.txt')
file = open(full_path,'r')
data = file.read()
data = data.split('\n')
### Part 1
sum = 0
for i in range(0,len(data)):
    seq = np.array([int(s) for s in data[i].split(' ')])
    end_vals = list([seq[-1]])
    while abs(seq).sum() != 0:
        seq = seq[1:] - seq [0:-1]
        end_vals.append(seq[-1])
    sum += np.array(end_vals).sum()
print(sum)

### Part 2
sum = 0
for i in range(0,len(data)):
    seq = np.array([int(s) for s in data[i].split(' ')])
    start_vals = list([seq[0]])
    plus_minus_ind = -1
    while abs(seq).sum() != 0:
        seq = seq[1:] - seq [0:-1]
        start_vals.append(plus_minus_ind * seq[0])
        plus_minus_ind *= -1
    sum += np.array(start_vals).sum()
print(sum)