#!/tools/bin/python

#  -------------+
#  Purpose      : Quick test of isdir function
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

from datetime import datetime

log1 = open('/var/log/secure').read()

 
log2 = open('/var/log/httpd/error_log').read()
log1_lines = log1.split('n')
log2_lines = log2.split('n')

print "- SSH Access Log -"
for line in log1_lines[-6:-1]:
   print line
print "- Apache Error Log -"

for line in log2_lines[-6:-1]:
   print line