#!/usr/bin/env python3

# Write a function that accepts a positive integer n as function parameter and returns True if n is a prime number,
# False otherwise. Note that zero and one are not prime numbers and two is the only prime number that is even.

def is_prime(n):
    if n < 2 :
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

answer = is_prime(1)
print(answer)
