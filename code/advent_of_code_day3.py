#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math


# In[2]:



fileObj = open('../data/advent_of_code_input_day_three.txt', "r") #opens the file in read mode.
items = fileObj. read(). splitlines() #puts the file into an array.


# In[3]:


#print (items)

def split(line): 
    return list(line)

holding = []
for i, line in enumerate(items):
    result = split(line)
    holding.append(result)

holding = np.array(holding)
holding[holding == '.'] = 0
holding[holding == '#'] = 1

holding = holding.astype(int)
print (holding)


# In[7]:



def dup_and_count(rightstep, downstep, basedata):
    needed_slope_elements = math.floor(basedata.shape[0]/downstep)
    replications_needed = (needed_slope_elements* rightstep)/basedata.shape[1]
    duplicated = np.tile(basedata, math.ceil(replications_needed))
    right = np.arange(0,(needed_slope_elements)*rightstep, rightstep).astype(int)
    down = np.arange(0,(needed_slope_elements)*downstep,downstep).astype(int)
    
    moves = []

    for ii in range(len(right)):
        moves.append(duplicated[down[ii], right[ii]])
    
    hits = np.sum(moves)
    return hits

down1_right3 = dup_and_count(3,1,holding)
down1_right1 = dup_and_count(1,1,holding)
down1_right5 = dup_and_count(5,1,holding)
down1_right7 = dup_and_count(7,1,holding)
down2_right1 = dup_and_count(1,2,holding)

results = np.array([down1_right3, down1_right1, down1_right5, down1_right7, down2_right1], dtype=np.int64)
print(results) 
product = np.prod(results)
print (product)


# In[ ]:




