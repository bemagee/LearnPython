#!/usr/bin/env python3

# Write a function that takes a two-dimensional list (list of lists) of numbers as
# argument and returns a list which includes the sum of each row. You can assume
# that the number of columns in each row is the same.

def _sum_of_rows_sample_(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(sum(item))
    return mylist

my_list = [[1,2,3], [4,5,6]]
my_avg = _sum_of_rows_sample_(my_list)
print(my_avg)

