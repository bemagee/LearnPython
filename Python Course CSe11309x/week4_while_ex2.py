# Write a program using while loop, which asks the user to type a positive integer, n,
# and then prints the factorial of n. A factorial is defined as the product of all the numbers from 1 to n
# (1 and n inclusive)


ask_int = input("enter a positive integer: ")
num = int(ask_int)
fact = 1

while num > 0 :
    fact = fact * num
    num -= 1

print("factor = ", fact)
