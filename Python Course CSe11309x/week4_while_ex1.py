#!/usr/bin/env python3

# Write a program which prints the sum of numbers from 1 to 101 ( 1 and 101 are included) that are divisible by 5

nums = 1
sum_nums = 0
while nums < 101:
    nums += 1
    if nums % 5 == 0:
        sum_nums = sum_nums + nums
        print("yes, divisible by five", nums)
        print("sum_nums total", sum_nums)

print("the sum of all nums divisible by 5 is", sum_nums)


