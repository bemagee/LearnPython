#!/usr/bin/env python3

import os
import sys
import random

#if else elif == != > >= <=


age = 30
if age > 16 :
    print('You are old enough to drive')
else :
    print('You are NOT old enough to drive')

if age >= 21 :
    print('You are old enough to drive a tractor trailer ')
elif age >= 16 :
    print('you are olde enought to drive a car')
else :
    print('You are NOT old enough to drive')

# logical operators "and, or, not"

if ((age >= 1) and (age <=18)) :
    print('You get a birthday')
elif (age == 21) or (age >= 65) :
    print ('You get a birthday')
elif not(age == 30) :
    print('You DO NOT get a birthday')
else:
    print ('You get a birthday yeah')
