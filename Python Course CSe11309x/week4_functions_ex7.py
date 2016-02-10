#!/usr/bin/env python3

# Write a function which accepts an input list of numbers and returns the
# largest number in the list (Do not use python's built-in max() function).

def _find_max_sample_(sample_list):
    # At first initialize total_sum to 0
    my_max = 0
    # Iterate through the list
    for item in sample_list:
        # Add each element to my_sum
        if my_max <= item :
            my_max = item
    return my_max

s_list = [10, 20, 30]
big_max = _find_max_sample_(s_list)
print("max item  = ", big_max)