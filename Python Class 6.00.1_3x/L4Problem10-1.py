#!/usr/bin/env python

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    char = char.lower()
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    else:
        return False