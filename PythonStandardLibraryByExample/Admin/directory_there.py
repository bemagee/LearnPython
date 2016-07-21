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

outdir="/tmp"

if os.path.isdir(outdir):   # Run the command mkdir in the system shell
    print ('yes. there is an existing folder', outdir, '\n')
    os.chdir(outdir)
    subprocess.call(["ls"])
else:
    print ("nope, directory not found\n")
#   os.mkdir(outdir)   # Run the command mkdir in the system shell



#
# End of script
#





















