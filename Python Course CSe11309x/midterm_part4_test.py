#!/usr/bin/env python3

import math
def is_prime(n):
    my_list = []
    if n % 2 == 0 and n > 2:
        print(False)
    for i in range(1, n):
        if not n % i == 0:
            my_list.append(i)
        for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    print(False)
    return(my_list)

my_nums = is_prime(7)
print(my_nums)