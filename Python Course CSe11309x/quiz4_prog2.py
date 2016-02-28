#!/usr/bin/env python3

# Write a function named count_consonants that receives a string as parameter and
# returns the total count of the consonants in the string. Consonants are all the
# characters in the english alphabet except for 'a', 'e', 'i', 'o', 'u'. If the same
# consonant repeats multiple times you should count all of them. Note that capitalization
# and punctuation does not matter here i.e. a lower case character should be considered the
# same as an upper case character.

def count_consonants(some_string):
    tot_consonants = 0
    lower_string = some_string.lower()
    for i in lower_string:
        if not i in ('a', 'e', 'i', 'o', 'u', ' ') :
            my_count = lower_string.count(i)
            tot_consonants += 1
            print("original string =", lower_string, "-> how many",i, "strings =", my_count)
    return tot_consonants
            
ccount = count_consonants('hi my Name is Brian')
print ("total consonants = ", ccount)
