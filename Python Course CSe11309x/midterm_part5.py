#!/usr/bin/env python3

# Write a function named items_price that accepts two lists as parameters. The
# first list contains the quantities of n different items, the second list contains
# the prices that correspond to those n items respectively. Now, calculate the total
# amount of money required to purchase those items. Assume that both the lists will
# have equal lengths. For example if the input lists are:
# a = [2, 3, 5, 7, 9]
# This list (list a) gives you the quantity of each item.
# b = [5, 8, 4, 1, 11]
# This list (list b) gives you the per item price for each item corresponding to the first
# list (list a). This means that if you want to purchase 2 units of the first item, each unit
# costs $5 per item, to purchase the 3 units of second item it costs $8 per item ...
# Now, your function should calculate and return the total price required to purchase all the
# quantities of all the items given to you.
# The correct output for the lists above would be:
# 160

def items_price(list_a, list_b) :
    total_amt = 0
    for i in range(len(list_a)) :
        amount = list_a[i] * list_b[i]
        total_amt += amount
    return(total_amt)

a = [2, 3, 5, 7, 9]
b = [5, 8, 4, 1, 11]
tot_price = items_price(a, b)
print(tot_price)