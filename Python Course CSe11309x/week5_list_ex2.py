#!/usr/bin/env python3

# Write a function that accepts two lists A and B and returns a new list which contains all the elements
# of list A followed by elements of list B. Notice that the behaviour of this function is different from
# list.extend() method because the list.extend() method extends the list in place, but here you are asked
# to create a new list and return it. Your function should not return the original lists. For example if
# the input lists are:
# A = ['p', 'q', 6, 'k']
# B = [8, 10]
# Then your function should return a list such as:
# ['p', 'q', 6, 'k', 8, 10]

def list_merger(list_a, list_b):
    merged_list = []
    b_len = len(list_b)
    a_len = len(list_a)
    for i in range(0,b_len) :
        a_len += 1
        list_a.insert(a_len, list_b[i])
    merged_list = list_a
    return merged_list

a_list = ['p', 'q', 6, 'k']
b_list = [8, 10]
my_list = list_merger(a_list, b_list)

print(my_list)