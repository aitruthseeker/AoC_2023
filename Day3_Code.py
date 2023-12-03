import os
import re
import numpy as np
full_path = os.path.join(os.getcwd(),'Input/Day3_Input.txt')
file = open(full_path,'r')
data = file.read()
data_list= data.split('\n')

### Part One
row = 0
sum = 0
for input_str in data_list:
    all_int_numbers = re.findall(r'\b\d+\b',input_str)
    prior_index = 0
    for number_to_check in all_int_numbers:
        left_index = re.search(number_to_check, input_str[prior_index:]).start()-1+prior_index
        prior_index = left_index + 1 + len(number_to_check)
        right_index = left_index + len(number_to_check) + 1
        row_above = 1 if row == 0 else row - 1
        row_below = row - 1 if row == len(data_list)-1 else row + 1
        if right_index >= len(input_str):
            elements_to_check = (input_str[left_index] + data_list[row_above][left_index:right_index] +
                                 data_list[row_below][left_index:right_index])
        elif left_index == -1:
            elements_to_check = (input_str[right_index] + data_list[row_above][left_index+1:right_index + 1] +
                                 data_list[row_below][left_index+1:right_index + 1])
        else:
            elements_to_check = (input_str[left_index] + input_str[right_index] +
                                 data_list[row_above][left_index:right_index+1] +
                                 data_list[row_below][left_index:right_index+1])
        if any([True if len(s) > 0 else False for s in elements_to_check.split('.')]):
            sum += int(number_to_check)
    row += 1
print(sum)

### Part Two
def add_to_dict(d, k, value):
    if k in d.keys():
        d[k].append(value)
    else:
        d[k] = list([value])
    return d

star_dict = {}
row = 0
for input_str in data_list:
    all_int_numbers = re.findall(r'\b\d+\b',input_str)
    prior_index = 0
    for number_to_check in all_int_numbers:
        left_index = re.search(number_to_check, input_str[prior_index:]).start()-1+prior_index
        prior_index = left_index + 1 + len(number_to_check)
        right_index = left_index + len(number_to_check) + 1
        row_above = 1 if row == 0 else row - 1
        row_below = row - 1 if row == len(data_list)-1 else row + 1
        if right_index >= len(input_str):
            right_comp = ''
            above_comp = data_list[row_above][left_index:right_index]
            down_comp = data_list[row_below][left_index:right_index]
            left_comp = input_str[left_index]
        elif left_index == -1:
            left_index = 0
            right_comp = input_str[right_index]
            above_comp = data_list[row_above][left_index:right_index + 1]
            down_comp = data_list[row_below][left_index:right_index + 1]
            left_comp = ''
        else:
            right_comp = input_str[right_index]
            above_comp = data_list[row_above][left_index:right_index+1]
            down_comp = data_list[row_below][left_index:right_index+1]
            left_comp = input_str[left_index]
        star_index = None
        if '*' in right_comp:
            star_index = 'row' + str(row) + 'col' + str(right_index)
            star_dict = add_to_dict(star_dict, star_index, number_to_check)
        elif '*' in left_comp:
            star_index = 'row' + str(row) + 'col' + str(left_index)
            star_dict = add_to_dict(star_dict, star_index, number_to_check)
        elif '*' in down_comp:
            star_index = 'row' + str(row_below) + 'col' + str(left_index + down_comp.find('*'))
            star_dict = add_to_dict(star_dict, star_index, number_to_check)
        elif '*' in above_comp:
            star_index = 'row' + str(row_above) + 'col' + str(left_index + above_comp.find('*'))
            star_dict = add_to_dict(star_dict, star_index, number_to_check)
    row += 1
sum = 0
for key in star_dict.keys():
    if star_dict[key].__len__() == 2:
        sum += (int(star_dict[key][0]) * int(star_dict[key][1]))
print(sum)
