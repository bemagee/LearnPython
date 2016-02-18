#!/usr/bin/env python3

# Write a function that accepts an input list and returns a new list which contains
# only the unique elements(Elements should only appear one time in the list and the
# order of the elements must be preserved as the original list)

def unique(list_a) :
    copied_list_a = list_a.copy()
    for i in range(len(list_a)):
        list_item = list_a[i]
        my_count = copied_list_a.count(list_item)
        if my_count > 1:
            list_item = list_a[i]
            copied_list_a.remove(list_item)
    return copied_list_a

a_list = [6, 1, 7, 2, 6, 1]
new_list = unique(a_list)
print(new_list)