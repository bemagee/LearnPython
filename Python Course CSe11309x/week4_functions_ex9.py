#!/usr/bin/env python3

# Write a function that accepts a number x and evaluates the following expression:
# y=x4-12x3+13x2+11

def _find_min_sample_(x):
    y = ((x**4) - 12 * (x**3) + (13 * (x**2)) + 11)
    return y


y = _find_min_sample_(3)
print("y  = ", y)
