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
    # implemented a Bubble sort
    # http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python
    for i in range(len(merged_list)) :
        for j in range(len(merged_list)-1-i) :
            if merged_list[j] > merged_list[j+1] :
                merged_list[j], merged_list[j+1] = merged_list[j+1], merged_list[j]
    return merged_list

a_list = [1, 20, 33, 6, 99]
b_list = [8, 10]
my_list = list_merger(a_list, b_list)

print(my_list)