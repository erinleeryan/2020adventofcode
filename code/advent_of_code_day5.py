import numpy as np

data = np.genfromtxt('2020adventofcode/data/advent_of_code_input_day_five.txt', dtype='str')
new_data = []

for line in data:
    new_data.append(int(line.replace('F', '0').replace('B','1').replace('L', '0').replace('R', '1'),2))

print ('Highest seat num is ', max(new_data))