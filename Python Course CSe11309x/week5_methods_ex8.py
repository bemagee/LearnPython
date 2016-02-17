#!/usr/bin/env python3

# Write a function that accepts two positive integers a and b and returns a
# list of all the even numbers between a and b (including a and not including b).

def even_nums(a, b) :
    even_nums_list = []
    for all_nums in range(a,b):
        if not (all_nums % 2):
            even_nums_list.append(all_nums)
    return(even_nums_list)


x = even_nums(100,150)
print(x)
