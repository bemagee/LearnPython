#!/usr/bin/env python3

# Write a function which accepts an input string and returns a string where the case
# of the characters are changed, i.e. all the uppercase characters are changed to lower
# case and all the lower case characters are changed to upper case. The non-alphabetic
# characters should not be changed. Do NOT use the string methods upper(), lower(), or swap().

def _my_Swap(s):
    output_string=""
    for char in s:
        if (ord(char)<= 90) and (ord(char)>=65) :
            x=chr(ord(char)+32)
            output_string=output_string+x
        elif (ord(char)<= 122) and (ord(char)>=97):
            x=chr(ord(char)-32)
            output_string=output_string+x
        else:
            output_string=output_string+char
    return output_string

input_string = "    Hello  "
output_string = _my_Swap(input_string)
print (output_string)
