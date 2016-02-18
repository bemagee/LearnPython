#!/usr/bin/env python3

# Write a function that accepts two lists both of which consists of integers and
# returns the total sum of all the odd integers from both lists.

def add_odd(list_a, list_b) :
    odd_cnt = 0
    merged_list = []
    merged_list = list_a
    merged_list.extend(list_b)
    for i in range(len(merged_list)):
        if merged_list[i] % 2:
            odd_cnt += merged_list[i]
    return odd_cnt

a_list = [6, 7, 2, 1]
b_list = [8, 10]
odd_nums = add_odd(a_list, b_list)

print(odd_nums)
