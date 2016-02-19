#!/usr/bin/env python3

# Write a program that asks the user for a positive number 'n' as input. Assume that the user
# enters a number greater than or equal to 3 and print a triangle as described below.
# For example if the user enters 6 then the output should be:

#*
#**
#***
#****
#*****
#******
#*****
#****
#***
#**
#*

my_int = int(input("enter a positive int: "))

for going_up in range(0, my_int) :
    print(going_up * "*")
    
while my_int > 0 :
    print(my_int * "*")
    my_int -= 1
