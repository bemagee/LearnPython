#!/usr/bin/env python3

# Write a program that asks the user to enter an integer between 1 and 9999 (both inclusive) and then prints the input integer using words. For example if the user enters:

# 3421
# Then your program should print
# three thousand four hundred twenty one
# more examples:
# Input	Printed Output
# 15	fifteen
# 7000	seven thousand
# 501	five hundred one
# 1008	one thousand eight
# 7	seven
# Notes:
# the words in the printed output should all be lower cased and separated by only one space
# There is no "and" between the printed words.
# Notice that when you use a print() statement, Python by default adds a new line after each printed output. If you do not want each new print statment to be printed in a new line then you should add end="" at the end of your print arguments as shown below:
# print("seven ", end = "")
# print("thousand")
# This will print
# seven thousand
# Also when you use two arguments in a print statement, Python adds a space between them by default. For example:
# print("x",5)
# will print
# x 5
# If you do not want a space to be inserted between your arguments then you should add sep="" at the end of your print arguments as shown below:
# print("x",5,sep="")
# will print
# x5
# Make sure your words match the following spellings:
# one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
# sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
# ninety, hundred, thousand

n=int(input('please enter an integer between 1 and 9999: '))

string_num = str(n)
len_of_num = len(string_num)

single_list = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]
tens_list =  [ '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]

for i in string_num :
#    print(i , 'of size ', len_of_num)

print_string = 0
print_string2 = 0
print_string3 = 0
print_string4 = 0
print_string5 = 0

    if len_of_num >= 4 :
        pos = int(i)
        if pos > 0 :
            print (single_list[pos], 'thousand ', end = "a")
            print_string = "single_list[pos] thousand"
        len_of_num -= 1
    elif len_of_num >= 3 :
        pos = int(i)
        if pos > 0 :
            print (single_list[pos], 'hundred ', end = "b")
            print_string2 =  "single_list[pos] hundred"
        len_of_num -= 1
    elif len_of_num >= 2 :
        test = int(string_num)
        if test  <= 19 :
            print (single_list[test])
            print_string3 = "single_list[test]"
            len_of_num -= 1
            break
        pos = int(i)
        pos_next = (int(i)-1)
        if pos > 0 and (test == 20 or test == 30 or test == 40 or test == 50 or test == 60 or test == 70 or test == 80 or test == 90) :
            print (tens_list[pos], end = "")
            print_string4 = "tens_list[pos]"
            len_of_num -= 2
        else:
            print (tens_list[pos], end = " ")
            print_string4 = "tens_list[pos]"
        len_of_num -= 1
    else:
        pos = int(i)
        if pos > 0 :
            print (single_list[pos]) 
            print_string5 = "single_list[pos]"
   
# construct the print statement
if print_string:
    print_all = print_string
if print_string2:
    print_all += print_string2
if print_string3:
    print_all += print_string3
if print_string4:
    print_all += print_string4
if print_string5:
    print_all += print_string5
    
print (print_all)
