#!/usr/bin/env python3

# Write a function that accepts a number x and evaluates the following expression:
# y=abs(x3)+cos(sqrt(3*x))
# and returns the value of y. Hint: Use the math module!

import math
def _evaluate_expression_sample3_(x):
    y = abs(x**3) + math.cos(math.sqrt(3*x))
    return y

x = _evaluate_expression_sample3_(3)
print(x)
