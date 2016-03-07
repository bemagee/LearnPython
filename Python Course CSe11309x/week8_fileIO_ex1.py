#!/usr/bin/env python3

# Write a function that accepts a filename as input argument and reads the file and saves
# each line of the file as an element in a list (without the new line ("\n")character) and
# returns the list. Each line of the file has comma separated values: For example if the
# content of the file looks like this:

# Lucas,Turing,22
# Alan,Williams,27
# Layla,Trinh,21
# Brayden,Huang,22
# Oliver,Greek,20
# then your function should return a list such as
# ['Lucas,Turing,22', 'Alan,Williams,27', 'Layla,Trinh,21', 'Brayden,Huang,22', 'Oliver,Greek,20']

def list_from_file(file_name):
    data = []
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    for item in file_pointer.readlines():
       stripped_line = item.strip('\n')
       data.append(stripped_line)
    file_pointer.close()
    return data

file_lst = list_from_file('week8_fileIO_ex1.txt')
print (file_lst)