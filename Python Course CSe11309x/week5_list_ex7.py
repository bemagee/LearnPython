#!/usr/bin/env python3


# Write a function that accepts a list that contains positive integers and returns a new list
# which contains all the elements from original list but adds 1 to those elements which are odd.
# For example if :
# input_list = [12, 3, 4, 5, 6]
# Then your function should return a list such as:
# [12, 4, 4, 6, 6]

def list_evener(list_one):
    for i in range(len(list_one)) :
        if list_one[i] % 2 :
             list_one[i] += 1
    return list_one

a_list = [1, 20, 33, 6, 99]
new_list = list_evener(a_list)
print(new_list)