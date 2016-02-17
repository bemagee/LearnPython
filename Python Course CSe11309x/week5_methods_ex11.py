#!/usr/bin/env python3

# Write a function that accepts a positive integer k and returns the list of all
# the divisors of k. Your list should include both 1 and k.

import math

def FindAllDivisors(x):
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
            my_count = divList.count(y)
            if my_count == 2 :
                divList.remove(y)
        y += 1
    divList.sort()
    return divList

x = FindAllDivisors(20)
print (x)