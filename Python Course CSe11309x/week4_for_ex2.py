# Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of all
# numbers from 1 to n (including both 1 and n).
total = 0

ask = input("enter an integer: ")
entered = int(ask)

for n in range(1, entered + 1):
    total += n

print(total)