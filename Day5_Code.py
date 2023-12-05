import os
import numpy as np
full_path = os.path.join(os.getcwd(),'Input/Day4_Input.txt')
file = open(full_path,'r')
data = file.read()
data_list= data.split('\n')
### Part 1
sum = 0
for input_str in data_list:
    split_str = input_str.split('|')
    my_numbers = [int(s) for s in split_str[1].split() if s.isdigit()]
    win_numbers = [int(s) for s in split_str[0].split(':')[1].split() if s.isdigit()]
    nr_match = (set(my_numbers) & set(win_numbers)).__len__()
    if nr_match >= 1:
        value = 2**(nr_match-1)
    else:
        value = 0
    sum += value
print(sum)

### Part 2
nr_copies = np.ones([len(data_list),1])
card_id = 0
for input_str in data_list:
    split_str = input_str.split('|')
    my_numbers = [int(s) for s in split_str[1].split() if s.isdigit()]
    win_numbers = [int(s) for s in split_str[0].split(':')[1].split() if s.isdigit()]
    nr_match = (set(my_numbers) & set(win_numbers)).__len__()
    card_id += 1
    for i in range(0,nr_match):
        nr_copies[card_id+i] = nr_copies[card_id+i] + nr_copies[card_id-1]
print(int(nr_copies.sum()))