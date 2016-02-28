#!/usr/bin/env python3

# Write a function named test_for_anagrams that receives two strings as parameters,
# both of which consist of alphabetic characters and returns True if the two strings 
# are anagrams, False otherwise. Two strings are anagrams if one string can be constructed 
# by rearranging the characters in the other string using all the characters in the original 
# string exactly once. For example, the strings "Orchestra" and "Carthorse" are anagrams 
# because each one can be constructed by rearranging the characters in the other one using all 
# the characters in one of them exactly once. Note that capitalization does not matter here i.e.
# a lower case character can be considered the same as an upper case character


def test_for_anagrams(my_string1, my_string2):
    test_str = ''
    lower_string1 = my_string1.lower()
    lower_string2 = my_string2.lower()
    len_string1 = len(lower_string1)
    len_string2 = len(lower_string2)
    if len_string1 == len_string2 :
        for i in lower_string1 :
            if lower_string2.find(i) > -1 :
                test_str = True
            else :
                test_str = False
                break
        for j in lower_string2 :
            if lower_string1.find(j) > -1 :
                test_str = True
            else :
                test_str = False
                break
        if test_str == True :
            return True
        else :
            return False
    else:
        return False    


answer = test_for_anagrams('doodle', 'poodle')
print(answer)