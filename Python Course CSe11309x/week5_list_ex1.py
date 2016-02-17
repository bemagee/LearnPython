#!/usr/bin/env python3

# Write a function that accepts a list (which has a length of 4 or more) and a
# string and returns the list such that the second through the fourth element
# (index 1 through 3 both inclusive) in the input list are replaced by the input
# string. For example:

# input_list = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
# input_string = "Brahman"
# Then, your function should return a list such as:
# ['Isha', 'Brahman', 'Brahman', 'Brahman', 'Sri']

def list_replacer(new_list, new_string):
    new_list[1] = new_string
    new_list[2] = new_string
    new_list[3] = new_string
    return new_list

input_list = ['TOM', 2, 'Jerry', 'Peace', 12, 'Draw', 'Attention', 'Stand up', 'Namaste']
input_string = "Brahman"
my_list = list_replacer(input_list, input_string)

print(my_list)