#!/usr/bin/env python3

# Write a function that accepts a list as input and returns a new list which
# includes every other element in the original list. Keep the first element,
# i.e. input_list[0]. For example if:
# input_list = ["we", "love", "python", "so","much"]
# then your function should return a list such as:
# ['we', 'python', 'much']

def even_lister(x) :
    cnt = len(x)
    return x[0:cnt:2]

input_list = ["we", "love", "python", "so", "much", "too", "xer", "size"]
new_x = even_lister(input_list)
print(new_x)