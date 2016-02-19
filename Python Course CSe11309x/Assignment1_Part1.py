#!/usr/bin/env python3

# Write a function that calculates and returns the monthly payments for a loan.
# This function accepts three parameters in the exact order
# (principal, annual_interest_rate, duration):

# *principal: The total amount of loan. Assume that the principal is a positive floating
# point number.

# *annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate
# is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)

# *duration: number of years to pay the loan back. Assume that duration is a positive integer.
# To calculate the amount of monthly payment for the loan you should use the following equation

# MonthlyPayment = Principal * r(1+r)**n/(1+r)**n-1
# Where:
# r is the monthly interest rate (should be calculated by first dividing the annual_interest_rate by
# 100 and then divide the result by 12 to make it monthly). Notice that if the interest rate is equal
# to zero then the above equation will give you a ZeroDivisionError. In that case you should use the
# following equation:MonthlyPayment=Principal/n

# n is the total number of monthly payments for the entire duration of the loan (Notice that n is equal
# to loan duration in years multiplied by 12).

# Your function should return the monthly payment as a floating point number.

# Example: if your function is called with the following parameters:

# (1000.0,4.5,5)
# Then it should return a floating point number:
# 18.643019241516996

# Remember that you are not asked to print anything. So, your function should just return the monthly
# payments. You do not need to call your function, it will automatically be called and tested for correctness
# with the test cases we provide. You only need to write one function and we will test your program with the
# first function that appears in your code. So, if you want to write more than one function to help you solve
# the problem remember to embed the helper functions inside the first function.


def my_loan (principal, annual_interest_rate, duration) :
    print("principal= ", principal)
    print("annual_interest rate= ", annual_interest_rate)
    monthly_rate = ((annual_interest_rate / 100) / 12)
    duration_in_months = (duration *  12)
    print("monthly_interest rate= ", monthly_rate)
    print("duration in years= ", duration)
    print("duration in months= ", duration_in_months)
    interest_paid = month_pay - monthly_rate
    principal_paid = month_pay - monthly_rate
    print("paid year 1:", month_pay * 12)
    print("principal paid year 1:", principal_paid)
    print("interest paid year 1:", interest_paid)
    return (principal * (monthly_rate * (1 + monthly_rate) ** duration_in_months) / ((1 + monthly_rate)** duration_in_months - 1))

month_pay = my_loan(1000.0,4.5,5)
print("loan amount is")
print (month_pay)
print("balance after year 1:", 1000 - month_pay * 12)
