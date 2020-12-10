import numpy

with open('../data/advent_of_code_input_day_six.txt', mode='r') as input_file:
    day6_data= input_file.read().split('\n\n')

running_count = 0
all_yes_count = 0
whole_group = 0
for index, line in enumerate(day6_data):
    subset = day6_data[index].split()
   
    day6_data[index] = day6_data[index].replace('\n','')
    running_count = running_count + len(np.unique(list(day6_data[index])))
    entry,counts = np.unique(list(''.join(subset)), return_counts = True)
    matches = np.where(counts == len(subset))  
    all_yes_count = all_yes_count + len(matches[0])
    
print ('The number of questions to which yes was answered', running_count)
print ('The number of times everyone in a group answers yes to a question', all_yes_count)