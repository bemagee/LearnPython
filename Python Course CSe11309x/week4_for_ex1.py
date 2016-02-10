# Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.

tot_nums = 0

for cntr in range(1, 102):
    if cntr % 2 == 0:
        tot_nums += cntr

print(tot_nums)
