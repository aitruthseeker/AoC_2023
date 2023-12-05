import os
import numpy as np
full_path = os.path.join(os.getcwd(),'Input/Day5_Input.txt')
file = open(full_path,'r')
data = file.read()
d= data.split('\n')
### Part 1
s = [int(s) for s in d[0].split(' ') if s.isdigit()]
m = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
     'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
m_dict = {}
current_m_id = 0
current_map_loc = 2

for i in range(current_map_loc, len(d)):
    if current_m_id == len(m)-1:
        m_dict[m[current_m_id]] = d[current_map_loc+1:]
        break
    elif current_m_id < len(m)-1:
        if d[i] == m[current_m_id+1]:
            m_dict[m[current_m_id]] = d[current_map_loc+1:i-1]
            current_m_id += 1
            current_map_loc = i
min_loc = 10**10
for current_pos in s:
    for key in m_dict.keys():
        m_line = 0
        flag_found = False
        flag_standard = False
        while not flag_found:
            loc_start = int(m_dict[key][m_line].split(' ')[1])
            loc_range = int(m_dict[key][m_line].split(' ')[2])
            if loc_start <= current_pos < loc_start + loc_range:
                flag_found = True
            else:
                m_line += 1
                if m_line == len(m_dict[key]):
                    flag_found = True
                    flag_standard = True
        if not flag_standard:
            loc_start = int(m_dict[key][m_line].split(' ')[1])
            dest_start = int(m_dict[key][m_line].split(' ')[0])
            current_pos = (current_pos - loc_start) + dest_start
    min_loc = min(min_loc,current_pos)
print(min_loc)

#### Part 2 -
interval_loc = []
for seed in range(0,len(s[::2])):
    interval_loc.append([s[::2][seed],s[::2][seed] + s[1::2][seed]-1])

intervals_to_check = interval_loc
for key in list(m_dict.keys()):
    mapped_intervals = []
    while len(intervals_to_check) >=1:
        current_int = intervals_to_check[0]
        current_int_not_found = True
        for current_map in m_dict[key]:
            #current_map = m_dict[key][0]
            # Mapping interval
            loc_start = int(current_map.split(' ')[1])
            loc_end = int(current_map.split(' ')[2]) + loc_start - 1
            dest_start = int(current_map.split(' ')[0])

            # Mapping interval larger than current interval:
            if current_int[0] >= loc_start and current_int[1] <= loc_end:
                intervals_to_check.pop(0)
                mapped_intervals.append([current_int[0]-loc_start+dest_start, current_int[1]-loc_start+dest_start])
                current_int_not_found = False
            else:
                flag_in_interval = False
                # Mapping interval - mapping range in interval
                if current_int[0] < loc_start and current_int[1] > loc_end:
                    intervals_to_check.pop(0)
                    intervals_to_check.append([current_int[0],loc_start-1])
                    intervals_to_check.append([loc_end+1,current_int[1]])
                    mapped_intervals.append([dest_start,dest_start+loc_end-loc_start])
                    flag_in_interval = True
                    current_int_not_found = False
                # Mapping interval - mapping range 'left' of interval
                elif (not flag_in_interval) and current_int[0] >= loc_start and current_int[0] <= loc_end:
                    intervals_to_check.pop(0)
                    intervals_to_check.append([loc_end+1,current_int[1]])
                    mapped_intervals.append([current_int[0]-loc_start+dest_start,loc_end-loc_start+dest_start])
                    current_int_not_found = False
                # Mapping interval - mapping range 'right' of interval
                elif (not flag_in_interval) and current_int[1] >= loc_start and current_int[1]<=loc_end:
                    intervals_to_check.pop(0)
                    intervals_to_check.append([current_int[0],loc_start-1])
                    mapped_intervals.append([dest_start, current_int[1]-loc_start+dest_start])
                    current_int_not_found = False

        if current_int_not_found:
            intervals_to_check.pop(0)
            mapped_intervals.append([current_int[0], current_int[1]])

    intervals_to_check = mapped_intervals

min_help = 10**1000
for interval in intervals_to_check:
    min_help = min(min_help,interval[0])
print(min_help)

