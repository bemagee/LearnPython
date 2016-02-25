#!/usr/bin/env python3


# Write a program that asks the user for an input 'n' and prints a square of n
# by n asterisks "*". For example if the user enters 5 then the output should
# look like the following: Note that there should be no spaces between the asterisks
# *****
# *****
# *****
# *****
# *****

input_num = input('enter a positive integer: ')
integer_num = int(input_num)
counter = integer_num
str_print = "*"

for i in range(0, counter) :
    print (str_print * integer_num)
