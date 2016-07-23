#!/home/brmagee/Python3/rhel6/python

#  -------------+
#  Purpose      : system information script
#  Command Line :
#  Inputs       : Options:
#               :    --debug: additional outputs for script debug mode
#               : Params:
#               :    None
#               : File(s):
#               :   list of files used by script
#  Outputs      : 0 - On success
#               : 1 - Failed
#  Author       : YOUR NAME
#  Orig Date    : DD MON YYYY
#  -------------+


# Imported Modules
import os
import re
import sys
import datetime
import time
import getopt
import argparse
import subprocess
import humanize

from datetime import datetime

#A System Information Gathering Script
import subprocess

#Command 1
def uname_func():
   uname = "uname"
   uname_arg = "-a"
   print "Gathering system information with %s command:\n" % uname
   subprocess.call([uname, uname_arg])
   print "\n"

#Command 2
def disk_func():
   diskspace = "df"
   diskspace_arg = "-hl"
   print "Gathering diskspace information %s command:\n" % diskspace
   subprocess.call([diskspace, diskspace_arg])
   print "\n"
   
#Command 2
def gitproc_func():
   gitprocess = "ps"
   gitprocess_arg = "-ef"
   print "List Git Processes %s command:\n" % gitprocess
   #subprocess.call([gitprocess, gitprocess_arg])
   list_proc = subprocess.Popen("ps -ef", shell=True, stdout = subprocess.PIPE)
   out = list_proc.stdout.read()
   for entry in out:
       if entry == "git":
          print entry
   print "\n"
   
# Main function that calls other functions
def main():
   uname_func()
   disk_func()
   gitproc_func()
   
main()

