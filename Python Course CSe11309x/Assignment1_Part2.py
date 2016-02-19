#!/usr/bin/env python3

# Write a function that calculates and returns the remaining loan balance. This function accepts four parameters in the exact order shown below:
# (principal, annual_interest_rate, duration , number_of_payments)
# principal: The total amount of loan. Assume that the principal is positive floating point number.
# annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number.
# (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
# duration: number of years to pay the loan back. Assume that duration is a positive integer.
# number_of_payments: number of monthly payments that are already paid. Assume that number_of_payments is an integer.

# To calculate the remaining loan balance use the following equation:
# RemainingLoanBalance=Principal*(1+r)n-(1+r)p(1+r)n-1
# Where:
# r is the monthly interest rate. r should be calculated by first dividing the annual_interest_rate by 100 and then divide the result by 12 to make it monthly.
# Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the following
# equation: RemainingLoanBalance=Principal(1-pn)
# n is the total number of monthly payments for the entire duration of the loan. Notice that n is equal to loan duration in years multiplied by 12.
# p is the number of payments which are already made.

# Your function should return the remaining balance as a floating point number.
# Example: if your function is called with the following parameters:
# (1000.0,4.5,5,12)
# Then it should return a floating point number:
# 817.5512804582867

def my_loan (principal, annual_interest_rate, duration, payments_made) :
    print("principal = ", principal)
    print("annual_interest rate = ", annual_interest_rate)
    monthly_rate = ((annual_interest_rate / 100) / 12)
    duration_in_months = (duration *  12)
    print("monthly_interest rate = ", monthly_rate)
    print("duration in years = ", duration)
    print("duration in months = ", duration_in_months)
    print("payments already made = ", payments_made)
    monthly_payments = (principal * ((monthly_rate * (1 + monthly_rate) ** duration_in_months) / ((1 + monthly_rate)** duration_in_months - 1)))
    print("total amount already paid = ", payments_made * monthly_payments)
    print("monthly payments = ", monthly_payments)
    return (principal - (payments_made * monthly_payments))

#remaining_balance = my_loan(1000.0,4.5,5,12)
remaining_balance = my_loan(1000.0,4.5,8,3)
print("loan balance is")
print (remaining_balance)


