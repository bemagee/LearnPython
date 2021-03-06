#!/usr/bin/env python3

# Write a function which accepts a 2D list of numbers and returns the sum of all the
# number in the list You can assume that the number of columns in each row is the same.
# (Do not use python's built-in sum() function).

def _sum_of_a_2d_list_sample_(sample_2d_list):
    # Initialize total sum to be 0
    total_SUM = 0
    # Get the length of rows and columns
    number_of_rows = len(sample_2d_list)
    number_of_columns = len(sample_2d_list[0])
    # Initialize row index to 0
    rows = 0
    # Produce row indices 0, 1, 2, ...number_of_rows
    while rows < number_of_rows:
        # for each row, initialize the column index to 0
        columns = 0
        # Produce column indices 0, 1, 2, ... number_of_columns
        while columns < number_of_columns:
            # Added the element i.e. list[row][column] to total sum
            total_SUM = total_SUM + sample_2d_list[rows][columns]
            # Increment to the next column index
            columns = columns + 1
        # increment to the next row index
        rows = rows + 1
    # Finally return the total sum
    return total_SUM


my_list = [[1,2,3], [4,5,6]]
my_sum = _sum_of_a_2d_list_sample_(my_list)
print(my_sum)