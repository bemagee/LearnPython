#!/usr/bin/env python3

import getopt
import os
import re
import sys
import time
from datetime import date

cnt_found = 0

# Open a text file
# find patterns
# write to a new output file

mytime = time.localtime(time.time())
print ("Local current time:", mytime)
print ("Today is:" ,mytime[1],'-',mytime[2],'-',mytime[0])
now = date.today()
print("\n")
print ("Today's Date:", now)
print("\n")

#existing_file = input("Enter the file to read: ");
#print ('Received file is :' , existing_file)

#fo = open(existing_file, "r+")

#fo.write("New text to the top from Brian\n")

#print ('Name of the file: ', fo.name)
#print ('Closed or not : ', fo.closed)
#print ('Open mode : ', fo.mode)


#fo.write("New text to the bottom from Brian\n")

#str = fo.read(25);

#print ('output from str: ', str)

current_dir = os.getcwd()
print ('Current working directory: ', current_dir)


#fo.close()
#print ('Closed or not : ', fo.closed)

# print empty lines
print("\n")

#if 'ARGV' in open('testolite-2015-01.log').read():
#    print('yes found one')

argv_log = open('argv.log', 'w')
full_log = open('full.log', 'w')
print_log = open('print.log', 'w')

for lineBuf in open('testolite-2015-01.log', 'r'):
    if 'ARGV' in lineBuf:
        #print ('entire line:',lineBuf)
        cnt_found += 1
        full_log.write(lineBuf)
        full_log.write("\n")
        line_found = re.split("\s+", lineBuf)
        #print ('line after split:',line_found)
        #print ('date:',line_found[0])
        #print ('ARGV:',line_found[3])
        #print ('SOC:',line_found[4])
        #print ('command:',line_found[5])
        #print ('FROM:',line_found[5])

        argv_log.write('%s %s %s\n' % (line_found[0], line_found[3], line_found[4]))
        print(line_found[3], line_found[4], file=print_log)
        #argv_log.write(line_found[0])
        #argv_log.write(" ")
        #argv_log.write(line_found[3])
        #argv_log.write(" ")
        #argv_log.write(line_found[4])
        #argv_log.write("\n")

print('Total lines found:' , cnt_found)

argv_log.close()
full_log.close()
print_log.close()
