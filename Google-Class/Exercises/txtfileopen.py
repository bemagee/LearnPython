#!/usr/bin/python2.6
for line in open("LICENSE.txt"):
    col = line.strip().split(' ')
    print col[0],col[1],col[2]
