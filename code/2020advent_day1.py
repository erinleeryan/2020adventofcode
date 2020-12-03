import itertools

f = open("../data/advent_of_code_input_day_one.txt", "r")
inputlist = list([(int(x.strip())) for x in f.readlines()])

def make_combos(listofvalues, combolength):
    combo = list(itertools.combinations(listofvalues,combolength))
    return combo

def add_elements_makes_2020(pair):
    return sum(pair) == 2020



# make a list where the two values combine to make 2020
two_part_matches = list(filter(add_elements_makes_2020, make_combos(inputlist,2)))
#make another list where three values combine to make 2020
three_part_matches = list(filter(add_elements_makes_2020, make_combos(inputlist,3)))


# just in case there's more than one match that adds up to 2020 use enumerate
for index,t2 in enumerate(two_part_matches):
    product = t2[0]*t2[1]
    print ('{} {}'.format('Two element solution: ', product))

for index,t3 in enumerate(three_part_matches):
    product = t3[0]* t3[1]* t3[2]
    print ('{} {}'.format('Three element solution: ', product))

