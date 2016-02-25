#!/usr/bin/env python3

# Write a function that accepts an alphabetic string and returns an integer
# which is the sum of all the UTF-8 codes of the character in that string.
# For example if the input string is "hello" then your function should return 532

def convert(new_str) :
    tot_8code = 0
    str_len = len(new_str)
    for i in range(0, str_len):
        ord_code = ord(new_str[i])
        tot_8code += ord_code
    return tot_8code

my_tot = convert("hello")
print (my_tot)
