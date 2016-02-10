#!/usr/bin/env python3

# Write a function that accepts a list of integers and returns the average.
# Assume that the input list contains only numbers. Do NOT use the built-in sum() function.

def _find_avg_sample_(sample_list):
    # At first initialize total_sum to 0
    my_sum = 0
    total_items = 0
    # Iterate through the list
    for item in sample_list:
        # Add each element to my_sum
        my_sum = my_sum + item
        total_items += 1
    my_avg = my_sum/total_items
    return my_avg

s_list = [10, 20, 30]
big_avg = _find_avg_sample_(s_list)
print("final average = ", big_avg)
