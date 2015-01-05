#!/usr/bin/env python3

import os
import sys
import random

for x in range(0, 10):
    print(x, ' ', end="")

print ('\n')

grocery_list = ['juice', 'tomatoes', 'potatoes', 'bananas']

for y  in grocery_list:
    print(y)

print ('\n')
for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
         print(num_list[x][y])
