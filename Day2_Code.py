import os
full_path = os.path.join(os.getcwd(),'Input/Day2_Input.txt')

file = open(full_path,'r')
data = file.read()
data_list= data.split('\n')

#### Part 1
colors = {'blue': 14, 'green': 13 , 'red': 12}
sum = 0
for input_str in data_list:
    draws = input_str.split(':')[1].replace(';', ',').split(',')
    possible = True
    for draw in draws:
        for col in colors.keys():
            if col in draw:
                realized_col = int(draw.replace(col,''))
                if realized_col > colors[col]:
                    print(col)
                    possible = False
    if possible:
        game_id = int(input_str.split(':')[0].replace('Game ', ''))
        print(game_id)
        sum += game_id

#### Part 2
sum = 0
for input_str in data_list:
    colors = {'blue': 0, 'green': 0, 'red': 0}
    draws = input_str.split(':')[1].replace(';', ',').split(',')
    possible = True
    for draw in draws:
        for col in colors.keys():
            if col in draw:
                realized_col = int(draw.replace(col,''))
                colors[col] = max(colors[col], realized_col)
    sum += (colors['blue'] * colors['red'] * colors['green'])