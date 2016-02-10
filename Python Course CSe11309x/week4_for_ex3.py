# Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of the square
# of all numbers form 1 to n (including both 1 and n).

# For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14

total = 0

ask = input("enter an integer: ")
entered = int(ask)

for n in range(1, entered + 1):
    total += n**2

print(total)