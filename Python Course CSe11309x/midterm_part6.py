#!/usr/bin/env python3

# Write a function named crazy_list that accepts a list as parameter and returns a boolean
# (either True or False) based on whether or not the list is the same forward and backwards.
# You may NOT use list.reverse() method.
# For example, if the list received by the function is:
# [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]
# (Notice how the list is exactly the same whether you read it from left to right, or from
# right to left) Then your function should return the Boolean
# True
# however, if the list recieved by the function is something like this:
# [4, 5, 6, 7, 8, 4, 5, 2]
# (Notice how the list is NOT the same when reading from left to right vs right to left)
# In this case, your function should return the Boolean
# False


def crazy_list(some_list):
    list_len = 0
    list_len = len(some_list)
    for i in range(0,list_len):
        print(some_list[i])
        print(some_list[list_len-i-1])
        if not some_list[i] == some_list[list_len-i-1] :
            return False
            break
    else :
        return True

my_list = [4, 5, 6, 7, 8, 4, 5, 2]
torf = crazy_list(my_list)
print(torf)