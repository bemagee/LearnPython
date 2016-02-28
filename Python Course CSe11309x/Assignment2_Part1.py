#!/usr/bin/env python3

# Write a function named find_mismatch that accepts two strings as input arguments and returns:
# 0 if the two strings match exactly.
# 1 if the two strings have the same length and mismatch in only one character.
# 2 if the two strings do not have the same length or mismatch in two or more characters.
# Capital letters are considered the same as lower case letters. Here are some examples:
# First string	Second String	Function return
# Python	Java	2
# Hello There	helloothere	1
# sin	sink	2 (note not the same length)
# dog	Dog	0


def find_mismatch(s1,s2):
    test_str = ''
    match_type = 2
    lower_string1 = s1.lower()
    lower_string1 = lower_string1.replace(" ", "")
    lower_string2 = s2.lower()
    lower_string2 = lower_string2.replace(" ", "")
    len_string1 = len(lower_string1)
    len_string2 = len(lower_string2)
    if len_string1 == len_string2 :
        for i in lower_string1 :
            if lower_string2.find(i) > -1 :
                test_str = match_type
            else :
                test_str = match_type
                break
        for j in lower_string2 :
            if lower_string1.find(j) > -1 :
                test_str = 0
            else :
                test_str = 1
                break
        if test_str == 0 :
            return 0
        else :
            return 1
    else:
        for i in lower_string1 :
            if lower_string2.find(i) > -1 :
                test_str = match_type
            else :
                test_str = match_type
                break
        for j in lower_string2 :
            if lower_string1.find(j) > -1 :
                match_type = 0
            else :
                match_type = 1
                break
        if test_str == 0 :
            return 0
        else :
            return 1
        match_type -= 1
        return match_type


answer = find_mismatch('Python', 'Java')
#answer = find_mismatch('Hello There', 'hellothere')
print(answer)