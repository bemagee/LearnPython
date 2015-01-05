#!/usr/bin/env python3

import os
import sys
import random

random_num = random.randrange(0,50)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,50)

i = 0;

print('--------------\n')
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue
    i += 1