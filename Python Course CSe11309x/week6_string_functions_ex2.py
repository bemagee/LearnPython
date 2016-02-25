#!/usr/bin/env python3

# Write a function that accepts an input string consisting of alphabetic characters and removes
# all the trailing whitespace of the string and returns it without using any .strip() method.
# For example if:
# input_string = "  Hello       "
# then your function should return an output string such as:
# output_string = "  Hello"

def _remove_trailing_whitespace_sample_(string):
    my_index = None
    x = len(string)
    while x:
        if string[x-1] != " ":
            my_index = x
            break
        x -= 1
    # slice the string from that index to the end
    new_string = string[:my_index]
    return new_string


input_string = "    Hello  "
output_string = _remove_trailing_whitespace_sample_(input_string)
print (output_string)