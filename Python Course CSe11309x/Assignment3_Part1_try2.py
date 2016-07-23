#!/usr/bin/env python3

# Write a function named find_word_horizontal that accepts a 2-dimensional list of
# characters (like a crossword puzzle) and a string (word) as input arguments. This
# function searches the rows of the 2d list to find a match for the word. If a match
# is found, this functions returns a list containing row index and column index of the
# start of the match, otherwise it returns the value None (no quotations).

# For example if the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
# word='cat'
# find_word_horizontal(crosswords,word)
# then your function should return
# [2,1]
# Notice that the 2d input list represents a 2d crossword and the starting index of the
# horizontal word 'cat' is [2,1]

# s d o g
# c	u c	m
# a	c a	t
# t	e t	k

# Note: In case of multiple matches only return the match with lower row index. If you
# find two matches in the same row then return the match with lower column index.

def find_word_horizontal(crosswords,word):
    number_of_rows = len(crosswords)
    number_of_columns = len(crosswords[0])
    for item in crosswords:
        string_rows = ''
        match_found = 0
        for i in range(0, number_of_rows):
            print (item[i])
            string_rows = string_rows+item[i]
            for letter in word :
                print ('letter in word: ', letter)
                if item[i] == letter :
                    match_found += 1
                if match_found == 1 :
                    possible_first_index = i
                if match_found == 3 :
                    print('we got it')
                    return (i, possible_first_index)
                    break
    return None

crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
my_index = find_word_horizontal(crosswords,word)
print(my_index)