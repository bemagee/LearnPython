#!/usr/bin/env python3

# Write a function that accepts a list of integers and returns the sum of all the numbers in the list.
# Assume that the input list contains only numbers. Do NOT use the built-in sum() function.

def _find_sum_sample_(sample_list):
    # At first initialize total_sum to 0
    my_sum = 0
    # Iterate through the list
    for item in sample_list:
        # Add each element to my_sum
        my_sum = my_sum + item
    return my_sum

s_list = [10, 20, 30]
big_sum = _find_sum_sample_(s_list)
print("final sum = ", big_sum)