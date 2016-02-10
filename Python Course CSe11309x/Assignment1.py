#!/usr/bin/env python3

# This assignment includes 3 parts. In the first two parts you are asked to write
# two functions to calculate the monthly payment and the remaining balance of a loan.

# In part 3 you are asked to write a program to use the two previous functions and
# display useful information about a loan.

# Part 1 - Write a function to calculate monthly payment for a loan.
# Part 2 - Write a function to calculate remaining balance for a loan
# Part 3 - Write a program to display information about a loan.
#          This program is using the functions in the last two parts.

def month_payments(loan_amount) :
    return loan_amount/12

def balance_amt(loan_amount, paid) :
    return loan_amount - paid

my_loan = 1200
month_amount = month_payments(my_loan)
my_bal = balance_amt(my_loan, month_amount)

print("my loan = ",my_loan)
print("my monthly payments are ", month_amount)
print("my balance is ", my_bal)