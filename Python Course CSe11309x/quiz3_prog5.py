#!/usr/bin/env python3

# Write a function that receives a positive integer as function parameter and returns True if the integer is a perfect number,
# False otherwise. A perfect number is a number whose sum of the all the divisors (excluding itself) is equal to itself.
# For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6. Therefore, 6 is a perfect number. 


def perf_num(my_int) :
    perf_tot = 0
    for i in range(1, my_int):
        if my_int % i == 0 :
            perf_tot = perf_tot + i
    if perf_tot == my_int :
        return True
    else :
        return False
  
tot = 0          
tot = perf_num(7)
str(tot)
print(tot)
        
    
