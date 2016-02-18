#!/usr/bin/env python3

# Write a function called find_integer_with_most_divisors that accepts a list of integers
# and returns the integer from the list that has the most divisors. In case of a tie,
# return the first item that has the most divisors. For example:
# if the list is:
# [8, 12, 18, 6]
# In this list, 8 has four divisors which are: [1,2,4,8] ; 12 has six divisors which
# are: [1,2,3,4,6,12]; 18 has six divisors which are: [1,2,3,6,9,18] ; and 6 has four
# divisors which are: [1,2,3,6]. Notice that both 12 and 18 are tied for maximum number
# of divisors (both have 6 divisors). Your function should return the first item with
# maximum number of divisors; so it should return:
# 12

def find_integer_with_most_divisors(int_list):
    highest_div_cnt = 0
    for i in int_list:
        div_cnt = 0
        for cnt in range(1,i+1):
            if i % cnt == 0 :
                div_cnt += 1
        if div_cnt > highest_div_cnt :
           best_num = i
           highest_div_cnt = div_cnt
    return best_num

my_list = [8, 12, 18, 6]
highest = find_integer_with_most_divisors(my_list)
print(highest)