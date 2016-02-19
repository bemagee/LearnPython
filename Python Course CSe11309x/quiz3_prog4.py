#!/usr/bin/env python3

# Write a function that accepts a list of integers as parameter. Your function should return the sum of all the odd numbers in the list.
# If there are no odd numbers in the list, your function should return 0 as the sum. 

# Remember that you are not asked to print anything. So, your function should just return the sum of all the odd numbers in the list.
# You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide.
# You only need to write one function and we will test your program with the first function that appears in your code. So, if you want
# to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.

def odd_sum(num_list) :
    cnt = 0
    odd_cnt = 0
    sumit = len(num_list)
    for cnt in range (0, sumit) :
        print("this num: ",num_list[cnt])
        if num_list[cnt] % 2 == 1 :
            odd_cnt += num_list[cnt]
    return odd_cnt

my_odds = odd_sum([3, 5, 110, 2, 10, 11])
str(my_odds)
print(my_odds)
