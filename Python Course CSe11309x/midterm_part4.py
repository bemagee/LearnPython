#!/usr/bin/env python3

# Write a function named list_of_primes that accepts a positive integer n and returns
# a sorted list (ascending order) of all the prime numbers between 2 and n (including
# 2 but not including n)

def list_of_primes(n):
    my_list = []
    for i in range(1, n):
        if not n % i == 0:
            my_list.append(i)
    return(my_list)

prnt_list = list_of_primes(5)
print(prnt_list)
