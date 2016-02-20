#!/usr/bin/env python3

# Write a function called pattern_sum that receives two single digit positive integers,
# (k and m) as parameters and calculates and returns the total sum as:
# k + kk + kkk + .... (the last number in the sequence should have m digits)
# For example, if the two integers are:
# (4, 5)
# Your function should return the total sum of:
# 4 + 44 + 444 + 4444 + 44444
# Notice the last number in this sequence has 5 digits. The return value should be:
# 49380
# if the two integers are:
# (5, 3)
# Your function should return the total sum of:
# 5 + 55 + 555
# Notice the last number in this sequence has 3 digits. The return value should be:
# 615


def pattern_sum(a, b):
    sum_total = 0
    string_hold = '' 
    string_list = []
    for i in range(1, b+1) :
        string_hold = str(a) * i
        string_list.append(string_hold)
    for item in string_list :
        sum_total += int(item)
    return(sum_total)

tot = pattern_sum(5,3)
print(tot)