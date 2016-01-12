#!/usr/bin/env python3

import os
import sys
import random

# Some examples of reading text files with different options
#
# The file sample.txt is a UTF-8 encoded text file with Windows
# line-endings (\r\n).

# (a) Reading a basic text file (UTF-8 default encoding)
file='sample.txt'
if os.path.exists(file):
    print("YES. found file")
    print("Reading a simple text file (UTF-8)")
    with open('sample.txt', 'rt') as f:
        for line in f:
            print(repr(line))
    f.close()
else:
    print("failed to find file sample.txt")

#print("Add some more lines the simple text file (UTF-8)")
#with open('sample.txt', 'wt') as a:
#    print("append Hello World", file=a)
#    print("append more Spicy Jalape", file=a)
#a.close()

print("Print new lines a simple text file (UTF-8)")
with open('sample.txt', 'rt') as f:
    for line in f:
        print(repr(line))
f.close()

print("Write lines to a new text file (UTF-8)")
with open('newfile_to_write.txt', 'wt') as w:
          w.write('stuff and more stuff \n')
          w.write('another line of more stuff')
w.close()

print("Now output the new text file (UTF-8)")
with open('newfile_to_write.txt', 'rt') as f:
    for line in f:
        print(repr(line))
f.close()
