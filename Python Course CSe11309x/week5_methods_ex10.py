#!/usr/bin/env python3

# Write a function that accepts a positive integer k and returns the list of
# cube root values of all the numbers from 1 to k (including 1 and not including
# k). [if k is 1, your program should return an empty list]

def cube_root(k):
    croot_list = []
    for i in range(1,k):
        croot = i**(1.0/3.0)
        croot_list.append(croot)
    croot_list.sort()
    return(croot_list)

x = cube_root(5)
print(x)
