#!/usr/bin/env python3

# Write a function named unique_common that accepts two lists both of which contain integers as
# parameters and returns a sorted list (ascending order) which contains unique common elements
# from both the lists. If there are no common elements between the two lists, then your function
# should return the keyword None
# For example, if two of the lists received by the function are:
# ([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7])
# You can see that elements 5, -7, and 8 are common in both the first list and the second list and
# that the element 8 occurs twice in both lists. Now you should return a sorted list (ascending order)
# of unique common elements like this:
# [-7, 5, 8]
# if the two lists received by the function are:
# ([5, 6, 7, 0], [3, 2, 3, 2])
# Since, there are no common elements between the two lists, your function should return the keyword
# None


def unique_common(a, b):
    findings= []
    my_index = 0
    len_a = len(a)
    len_b = len(b)
    if len_a >= len_b :
        master_len = len_a
    for i in range(0, master_len):
        if a[i] in b :
            my_index = b.index(a[i])
            found = 'yes'
        else :
            found = 'no'
        if found == 'yes' :
            if not a[i] in findings :
                findings.append(a[i])
            my_index = 0
    if len(findings) == 0 :
        return(None)
    else:
        findings.sort()
        return(findings)

my_a = [12, 12, 11, 14, 16, 18]
my_b = [11, 11, 12, -5]

common_list = unique_common(my_a, my_b)
print(common_list)

