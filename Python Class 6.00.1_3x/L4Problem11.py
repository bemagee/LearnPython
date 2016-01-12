#!/usr/bin/env python

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    char = char.lower()
    vowel = 'aeiou'
    for char in vowel:
        print(True)
        return(True)
    else:
        print(False)
        return(False)


char = "t"
isVowel2(char)