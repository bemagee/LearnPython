#!/usr/bin/env python3

# Write a function that accepts two positive integers a and b (a is smaller
# than b)and returns a list that contains all the odd numbers between a and b
# (including a and including b if applicable) in descending order.

def odd_nums(a,b):
    odd_nums_list = []
    for all_nums in range(a,b+1):
        if all_nums % 2:
            odd_nums_list.append(all_nums)
    odd_nums_list.reverse()
    return(odd_nums_list)


x = odd_nums(11,31)
print(x)
