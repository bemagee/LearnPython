#!/usr/bin/env python3

# Write a program using while loops that asks the user for a positive integer 'n'
# and prints a triangle using numbers from 1 to 'n'. For example if the user enters
# 6 then the output should be like this :
# (There should be no spaces between the numbers)
# 1
# 22
# 333
# 4444
# 55555
# 666666

input_num = input('enter a positive integer: ')
integer_num = int(input_num)
counter = 1
str_counter = "1"

while counter <= integer_num :
    print (str_counter * counter)
    counter += 1
    str_counter = str(counter)