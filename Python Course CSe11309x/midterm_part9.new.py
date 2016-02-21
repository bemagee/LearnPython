#!/usr/bin/env python3

def GCD(numbers):

    if numbers[-1] == 0:
        return numbers[0]

    numbers.sort()
    
    gcd = 0

    for i in range(len(numbers)):
        gcd = GCD([numbers[i+1], numbers[i] % numbers[i+1]])
        gcdtemp = GCD([gcd, numbers[i+2]])
        gcd = gcdtemp

    return gcd


my_list_a = [3, 5, 9, 11, 13]
my_gcd = GCD(my_list_a)

print(my_gcd)
