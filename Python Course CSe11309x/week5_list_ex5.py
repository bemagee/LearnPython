#!/usr/bin/env python3

# Write a function that accepts a list and a value of an element and returns the count
# of how many times that element appears in the list. The behavior of this function
# should be exactly like the list.count() method. You may NOT use any built in list
# methods for this problem.

def list_cntr(list, item):
    item_cntr = 0
    for i in range(len(list)) :
        if list[i] == item :
            item_cntr += 1
    return item_cntr

list = [1, 20, 33, 6, 99, 33, 33]
item = 33
how_many = list_cntr(list, item)
print("for item", item, "found", how_many, "times")
