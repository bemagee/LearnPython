#!/usr/bin/python2.6
for line in open("LICENSE.txt"):
    col = line.strip().split(' ')
    if col[2] == 'errors':
        print "ERROR"
    else:
        print col[0...4]
