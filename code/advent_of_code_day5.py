import numpy as np

data = np.genfromtxt('2020adventofcode/data/advent_of_code_input_day_five.txt', dtype='str')
new_data = []

for line in data:
    new_data.append(int(line.replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1'),2))

print ('Highest seat num is ', max(new_data))

seats_sorted = np.sort(new_data)

seats_dummy = np.arange(min(new_data), max(new_data))

unassigned = set(seats_dummy) - set(seats_sorted)
print ('This is your seat: ', unassigned)