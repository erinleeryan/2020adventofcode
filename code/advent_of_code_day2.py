import pandas as pd

input = pd.read_csv('../data/advent_of_code_input_day_two.txt', delimiter=' ', names =['min-max', 'requirement', 'password'])  
input.requirement = input.requirement.str.replace(':','')
input[['min', 'max']]= input['min-max'].str.split('-', expand=True) 

input['Count'] = ""
for index, row in input.iterrows():
     substring = row.requirement
     password = row.password
     row['Count'] = password.count(substring)
input['okay_password'] = input['Count'].between(input['min'].astype('int'),input['max'].astype('int'), inclusive=True)
print('Passwords that have specified substring appear btwn min and max value, inclusive', input.okay_password.value_counts())


input['pos_one'] = ""
input['pos_two'] = ""
input['combined_pos'] = ""

input['pos_one'] = ""
input['pos_two'] = ""
input['combined_pos'] = ""

for index, row in input.iterrows():
     substring = row.requirement
     password = row.password
     position_one = int(row['min'])
     position_two = int(row['max'])

     if (password[position_one-1] == substring):
         row['pos_one'] = True
     else:
         row['pos_one'] = False

     if (password[position_two -1] == substring):
         row.pos_two = True
     else:
         row.pos_two = False

input['pos_one'] = ""
input['pos_two'] = ""
input['combined_pos'] = ""
for index, row in input.iterrows():
    substring = row.requirement
    password = row.password
    position_one = int(row['min'])
    position_two = int(row['max'])

    input.loc[index, 'pos_one'] = (password[position_one-1] == substring)
    input.loc[index,'pos_two'] = (password[position_two-1] == substring)
    input.loc[index, 'combined_pos'] = ((password[position_one-1] == substring) == (password[position_two-1] == substring))
 



print ('False value counts are where the first position != second position, which is what passwords require now')
print(input.combined_pos.value_counts())
