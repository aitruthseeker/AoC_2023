import os

full_path = os.path.join(os.getcwd(),'Day1/Day1_Input.txt')

file = open(full_path,'r')
data = file.read()
data_list= data.split('\n')
data_list = data_list[:-1]


#### Part 1
def first_int_in_str(input_str):
    for idx, char in enumerate(input_str):
        if char.isdigit():
            return char


def get_number_str(input_str):
    return int(first_int_in_str(input_str) + first_int_in_str(input_str[::-1]))


sum = 0
for puzzle_str in data_list:
    sum += get_number_str(puzzle_str)
print(sum)


#### Part 2
numbers_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                'eight': '8', 'nine': '9'}


def check_spelled_out_letter(input_str, letters_list):
    for letter in letters_list:
        if letter in input_str:
            return letter, True
    return None, False


def replace_str_by_digit(input_str, letters_dict, direction):
    str_len = len(input_str)
    replaced_flag = False
    i = 1
    while not replaced_flag and i <= str_len:
        if direction == 'front':
            letter, flag = check_spelled_out_letter(input_str[:i], letters_dict)
        elif direction == 'back':
            letter, flag = check_spelled_out_letter(input_str[str_len-i:], letters_dict)
        else:
            raise ValueError('Please insert valid direction')
        i += 1
        if flag:
            input_str = input_str.replace(letter, letters_dict[letter])
            replaced_flag = True

    return input_str

sum = 0
for puzzle_str in data_list:
    puzzle_str_front = replace_str_by_digit(puzzle_str, numbers_dict, direction='front')
    puzzle_str_back = replace_str_by_digit(puzzle_str, numbers_dict, direction='back')
    sum += int(first_int_in_str(puzzle_str_front) + first_int_in_str(puzzle_str_back[::-1]))
print(sum)

