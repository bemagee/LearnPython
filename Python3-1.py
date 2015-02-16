#!/usr/bin/env python3

import os
import re
import sys
import time

# Open a text file
# find patterns
# write to a new output file

mytime = time.localtime(time.time())
print ("Local current time:", mytime)
print ("Today is:" ,mytime[1],'-',mytime[2],'-',mytime[0])

existing_file = input("Enter the file to read: ");
print ('Received file is :' , existing_file)

fo = open(existing_file, "r+")

fo.write("New text to the top from Brian\n")

print ('Name of the file: ', fo.name)
print ('Closed or not : ', fo.closed)
print ('Open mode : ', fo.mode)


fo.write("New text to the bottom from Brian\n")


str = fo.read(25);

print ('output from str: ', str)

current_dir = os.getcwd()
print ('Current working directory: ', current_dir)

fo.close()
print ('Closed or not : ', fo.closed)

# print empty lines
print("\n")

if 'ARGV' in open('test2.txt').read():
    print('yes found one')

for lineBuf in open('gitolite-2015-01.log', 'r'):
    if 'ARGV' in lineBuf:
        #print ('entire line:',lineBuf)
        line_found = re.split("\s+", lineBuf)
        print ('line after split:',line_found)
        print ('date:',line_found[0])
        print ('ARGV:',line_found[3])
        print ('SOC:',line_found[4])
        print ('command:',line_found[5])
        print ('FROM:',line_found[6])
        print("\n")
