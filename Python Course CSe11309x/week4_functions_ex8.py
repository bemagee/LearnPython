#!/usr/bin/env python3

# Write a function which accepts an input list of numbers and returns the smallest
# number in the list (Do not use python's built-in min() function).


def _find_min_sample_(sample_list):
    # At first initialize total_sum to 0
    my_min = sample_list[0]
    # Iterate through the list
    for item in sample_list:
        # Add each element to my_sum
        if item < my_min :
            my_min = item
    return my_min

s_list = [30, 20, 35, 1]
big_min = _find_min_sample_(s_list)
print("min item  = ", big_min)
