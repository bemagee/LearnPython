#!/usr/bin/env python3

# Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)
# (1 + 4 + 7 + 10 + ....)

num = 1001
loop_cnt = -2
third_cnt = 0
total_cnt = 0

while loop_cnt <= num :
    loop_cnt += 1
    third_cnt += 1
    if third_cnt == 3 :
        total_cnt += loop_cnt
        third_cnt = 0

print("total", total_cnt)
