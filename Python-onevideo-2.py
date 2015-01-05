#!/usr/bin/env python3

import os
import sys
import random

grocery_list = ['juice', 'tomatoes', 'potatoes',
                'bananas']
print('First item', grocery_list[0])

grocery_list[0] = 'green juice'
print('First item', grocery_list[0])

print(grocery_list[1:3])

other_events = ['wash car', 'pick up kids', 'cash check']

todo_list = [other_events, grocery_list]
print(todo_list)

print((todo_list[1][1]))

grocery_list.append('onions')
print(todo_list)

grocery_list.insert(1, 'pickle')
print(todo_list)
print('\n')

grocery_list.sort()
print('\n')
print(grocery_list)
grocery_list.reverse()
print(grocery_list)

print('\n')
print("before delete", todo_list)
del grocery_list[4]
print('\n')
print("after delete", todo_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))