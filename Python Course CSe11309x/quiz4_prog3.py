#!/usr/bin/env python3

# Write a function named find_longest_word that receives a string as parameter and returns
# the longest word in the string. Assume that the input to this function is a string of words 
# consisting of alphabetic characters that are separated by space(s). In case of a tie between 
# some words return the last one that occurs.

def find_longest_word(some_string):
    string_len = len(some_string)
    word_cnt = 0
    current_word = ''
    longest_word = ''
    longest_word_cnt = 0
    some_string = some_string + " "
    lower_string = some_string.lower()
    for i in some_string :
        if not i in (' ') :
            word_cnt += 1
            current_word = current_word + i
        else :
            if word_cnt >= longest_word_cnt :
                longest_word_cnt = word_cnt
                longest_word = current_word
            word_cnt = 0
            current_word = ''
    return longest_word 

long_word = find_longest_word('brahman the mysterious of the univERsity')
print ("total consonants = ", long_word)