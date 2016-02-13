#!/usr/bin/env python3

#  Write a program for loan calculations. Your program should ask the user for three pieces of information (with three seperate input() functions:)

# The total amount of loan. Assume that the user enters a floating point number.
# Annual interest rate. Assume that the user enters a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
# Total duration of loan in years. This is the number of years to pay the loan back. Assume that the user enters a positive integer. Also remember that the loan is paid back with monthly payments.
# Your Program should use the two functions that you implented in part 1 and part 2 of this assignment and display the follwoing information about the loan.

# In the first first line show the amount of loan and interest rate.
# In the second line show duration of the loan and monthly payment.
# In each of the following lines show the Loan balance and total amount paid for each year.
# Example 1: assuming that user inputs the following numbers in response to your questions:

# Enter loan amount: 1000.0
# Enter annual interest rate (percent): 4.5
# Enter loan duration in years: 5

# The output of your program should be:
# LOAN AMOUNT: 1000.0 INTEREST RATE (PERCENT): 4.5
# DURATION (YEARS): 5 MONTHLY PAYMENT: 18
# YEAR: 1 BALANCE: 817 TOTAL PAYMENT 223
# YEAR: 2 BALANCE: 626 TOTAL PAYMENT 447
# YEAR: 3 BALANCE: 427 TOTAL PAYMENT 671
# YEAR: 4 BALANCE: 218 TOTAL PAYMENT 894
# YEAR: 5 BALANCE: 0 TOTAL PAYMENT 1118

# Important notes:
# Print LOAN AMOUNT and INTEREST RATE as floating point numbers.
# Convert all the calculated numbers (MONTHLY PAYMENT, BALANCE, TOTAL PAYMENT) to int only for printing them. This means that you should use floating point numbers for all of your calculations and only convert them to int for printing.
# Pay attention to capitalization and spaces.


def my_loan (principal, annual_interest_rate, duration) :
    print("principal = ", principal)
    print("annual_interest rate = ", annual_interest_rate)
    monthly_rate = ((annual_interest_rate / 100) / 12)
    duration_in_months = (duration *  12)
    print("monthly_interest rate = ", monthly_rate)
    print("duration in years = ", duration)
    print("duration in months = ", duration_in_months)
    monthly_payments = (principal * (monthly_rate * (1 + monthly_rate) ** duration_in_months) / ((1 + monthly_rate)** duration_in_months - 1))
    return (monthly_payments)

# Your main program goes here
principle=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
duration_in_months = (duration *  12)
remaining_balance = principle


print("")
print("LOAN AMOUNT:" ,principle, "INTEREST RATE (PERCENT):", annual_interest_rate)
print("DURATION (YEARS):", duration ,"MONTHLY PAYMENT: ", int(duration_in_months))
years = 0
for years in range(0, duration) :
    monthly_payments = my_loan(principle,annual_interest_rate,duration)
    years += 1
    payments_this_year = 12 * monthly_payments
    print("YEAR:", years, "BALANCE: ", int(remaining_balance), "TOTAL PAYMENT " , int(payments_this_year))
    remaining_balance = remaining_balance - payments_this_year
    balance = remaining_balance
    duration = duration - 12

