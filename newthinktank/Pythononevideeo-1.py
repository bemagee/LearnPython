#!c:/python33/python.exe
import os
import sys
import random

print ("Hello World")

# variables start with a letter and can contain numbers and underscores
name = "Derek"
print(name)

# Datatypes numbers, strings, lists, tuples, dictionaries

# arithmetic operations
print ("5 + 2 =", 5+2)
print ("5 - 2 =", 5-2)
print ("5 * 2 =", 5*2)
print ("5 / 2 =", 5/2)
print ("5 % 2 =", 5%2)
print ("5 ** 2 =", 5**2)
print ("5 // 2 =", 5//2)

quote = "\"Always remember you are unique"

multi_line_quote = '''just
list everyone else '''

new_string = quote + multi_line_quote

print ("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print ('\n' * 5)

print("i don't like ", end="")
print("newlines")