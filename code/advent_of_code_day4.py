import csv

with open('2020adventofcode/data/advent_of_code_input_day_four.txt', mode='r') as input_file:
    day4_data= input_file.read().split('\n\n')
    
print ('day 4 data length', len(day4_data))
    
required_keywords = ['byr','iyr','eyr', 'hgt', 'hcl','ecl', 'pid']
required_eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

invalid = 0.

count = 0.

for line in day4_data:
    count = count+1
    parsed = line.replace('\n', ' ').rstrip()

    missing_count = 0.
    fubarred_record = 0.
    for keyword in required_keywords:
        if ((keyword in parsed) == False):
            missing_count = missing_count +1
    if (missing_count != 0):
        invalid = invalid +1
    if (missing_count == 0):
        values = parsed.split(' ')
        
        passport = dict((x.strip(), y.strip()) 
             for x, y in (element.split(':') 
             for element in parsed.split(' ')))
                            
        hair = passport['hcl']
        eye = str(passport['ecl'])
        passnum = passport['pid']
        birth = passport['byr']
        issue = passport['iyr']
        expiration = passport['eyr']
        height = passport['hgt']
        
        
        if ((1920 <= int(birth) <= 2002) == False):
            fubarred_record = fubarred_record +1.
        if ((2010 <= int(issue) <= 2020) == False):
            fubarred_record = fubarred_record +1.
        if ((2020 <= int(expiration) <= 2030) == False):
            fubarred_record = fubarred_record +1.       
        if ((eye in required_eye) == False):
            fubarred_record = fubarred_record + 1.
        if (len(passnum) != 9):
            fubarred_record = fubarred_record + 1.
        if ((height[-2:] == 'cm')  & ((150 <= int(height[:-2] ) <= 193) == False)):
            fubarred_record = fubarred_record + 1.
        if ((height[-2:] == 'in') &((59 <= int(height[:-2]) <= 76) == False)):
            fubarred_record = fubarred_record + 1.
        if ((height[-2:] != 'in') & (height[-2:] != 'cm')):
            fubarred_record = fubarred_record+1
        if ((len(hair) != 7) | (hair[0] != '#')):
            fubarred_record = fubarred_record +1.
            
        if (fubarred_record >= 1.):
            invalid = invalid +1
print ('Number valid passports', len(day4_data)-invalid)