#!/usr/bin/env python3

# Write a function that accepts a list of integers and returns a new list which is the
# sorted version (ascending order) of the original list (Original list should not be modified).
# You may NOT use the built in sort() or sorted() functions. Notice that the original list
# should not be modified



def list_merger(list_a, list_b):
    merged_list = []
    list_a.extend(list_b)
    merged_list = list_a
    merged_len = len(merged_list)
    sorted = 0
    low_num = 0
    high_num = 0
    while sorted == 0 :
        for i in range(0,merged_len-1) :
            if merged_list[i] > merged_list[i+1] :
                low_num = merged_list[i+1]
                high_num = merged_list[i]
                mv_item = merged_list.pop(i)
                merged_list.insert(i+1, mv_item)
            if low_num > high_num :
                sorted = 0
            else :
                sorted = 1
    return merged_list

a_list = [1, 20, 33, 6, 99]
b_list = [8, 10]
my_list = list_merger(a_list, b_list)

print(my_list)