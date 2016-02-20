#!/usr/bin/env python3

# Write a function named find_gcd that accepts a list of positive integers and returns their greatest common divisor (GCD).
# Your function should return 1 as the GCD if there are no common factors between the integers. Here are some examples: 

# if the list was

# [12, 24, 6, 18]
# then your function should return the GCD:
# 6
# if the list was
# [3, 5, 9, 11, 13]
# then your function should return their GCD:
# 1

import fractions

def find_gcd(some_list):
    greatest_div = 0
    lowest_element = min(some_list)
    for i in some_list :
        if i%lowest_element == 0 :
            if lowest_element == greatest_div :
                greatest_div = 1
            else :
                greatest_div = lowest_element
    return(greatest_div)

# my_list_a = [12, 24, 6, 18]
my_list_a = [3, 5, 9, 11, 13]
my_gcd = find_gcd(my_list_a)

print(my_gcd)