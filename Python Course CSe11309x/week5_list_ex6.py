#!/usr/bin/env python3



# Write a function that accepts a list and return a new list which contains all but
# the first and last elements of the original list.

def list_chopper(my_list) :
    list_size = 0
    list_size = len(my_list)
    return my_list[1:list_size-1]

list_a = [1,2,3,4,5]
this_list = list_chopper(list_a)
print(this_list)

