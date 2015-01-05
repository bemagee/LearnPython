#!/usr/bin/env python3

import os
import sys
import random


long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.5f" % ("X", 'favorite', 1, .14))

#various built in string functions
print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalpha())
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Floor","Ground"))
print(long_string.strip())
quote_list = long_string.split(" ")
