#!/usr/bin/env python3

# Strings Functions Exercise 1 (Leading White Space)
# Write a function that accepts an input string consisting of alphabetic characters
# and removes all the leading whitespace of the string and returns it without using
# .strip(). For example if:
# input_string = "    Hello  "
# then your function should return a string such as:
# output_string = "Hello  "

def _remove_leading_whitespace_sample_(string):
    my_index = None
    for x in range(0, len(string)):
        if string[x] != " ":
            my_index = x
            break
    # slice the string from that index to the end
    new_string = string[my_index::]
    return new_string


input_string = "    Hello  "
output_string = _remove_leading_whitespace_sample_(input_string)
print (output_string)
