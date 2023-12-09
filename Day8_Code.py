import os
import numpy as np
full_path = os.path.join(os.getcwd(),'Input/Day8_Input.txt')
file = open(full_path,'r')
data = file.read()
data = data.split('\n')
moves = data[0]

i = 2
d={}
for i in range(2,len(data)):
    d[data[i][0:3]] = [data[i][7:10],data[i][12:15]]
### Part 1
current = 'AAA'
nr_moves = 0
pos_steps = 0

while current != 'ZZZ':
    if moves[pos_steps] == 'L':
        current = d[current][0]
    else:
        current = d[current][1]
    pos_steps += 1
    nr_moves +=1
    if pos_steps >= len(moves):
        pos_steps = 0
print(nr_moves)

### Part 2 -- need to find a smart solution, brute force to slow
current_nodes = [s for s in list(d.keys()) if s[2]=='A']
nr_moves = 0
pos_steps = 0
while not all([True if s[2]=='Z' else False for s in current_nodes]):
    current_nodes = list(dict.fromkeys(current_nodes))
    for i in range(0,len(current_nodes)):
        if moves[pos_steps] == 'L':
            current_nodes[i] = d[current_nodes[i]][0]
        else:
            current_nodes[i] = d[current_nodes[i]][1]
    pos_steps += 1
    nr_moves += 1
    if pos_steps >= len(moves):
        pos_steps = 0

