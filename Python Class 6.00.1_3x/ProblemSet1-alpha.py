#!/usr/bin/env python

string = 'akbabc'
for letter in string:
    b = ord(letter)
    c = ord(letter)+1
    print 'current' + str(b)
    print 'next' + str(c)
    nextchar = chr(b+1)
    if letter == nextchar:
        print yes
