#!/usr/bin/env python3

# Write a function which accepts an input string consisting of alphabetic characters and returns the string with all the spaces removed.
# Do NOT use any string methods for this problem.

def _remove_spaces_(string):
    out_string = ""
    for x in range(0, len(string)):
        if string[x] != " ":
            out_string = out_string + string[x]
    return out_string

input_string = "    Hello this is my string  "
output_string = _remove_spaces_(input_string)
print (output_string)