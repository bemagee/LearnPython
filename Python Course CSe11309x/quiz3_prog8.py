#!/usr/bin/env python3

# Write a function that accepts two positive integers as parameters. The first integer is the number of heads and the second integer is
# the number of legs of all the creatures in a farm which consists of chickens and dogs. Your function should calculate and return the
# number of chickens and number of dogs in the farm in a list as specified below. If it is impossible to determine the correct number
# of chickens and dogs with the given information then your function should return None. Example 1, if your function received the following numbers:

# 5, 12 
# This means that someone has counted a total of 5 heads and total of 12 legs in the farm. Now, your function should calculate how many chickens and
# how many dogs are in the farm and return that information in a list exactly as shown below.
# [4, 1] 
# this means that there were 4 chickens and 1 dog in the farm. 

# Example 2, if your function received the following numbers:
# 7, 12 
# Then it should return:
# None


def animal_cnt(heads, legs) :
    print("number of heads:", heads)
    print("number of legs:", legs)
    if heads * 2 <= legs :
        print("num of chickens: ", legs/heads)
        print("num of dogs: ", legs%heads)
    else :
        print("None")
    return(number_of_chickens, number_of_dogs)

animals[chicks,dogs] = animal_cnt(4, 1)
print animals
