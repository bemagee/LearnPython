#!/tools/bin/python -tt

#  -------------+
#  Purpose      : Short description of script
#                 - list of features
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
import os,re,sys,datetime,time,getopt
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Local Vars
CAPITOLIZEVARS=''
OUTPUT = False
OUTPUT_FILE = ''
ListNums = []
DICTNums = {}


# Process ARGs
try:
        options, remainder = getopt.getopt(
        sys.argv[1:],
        'o:d',
        ['output=',
        'debug',
        ])
except getopt.GetoptError, err:
    print 'ERROR:', err
    sys.exit(1)

for opt, arg in options:
    if opt in ('-o', '--output'):
        outdir = "inv_output"
        output_file = '%s/%s' % (outdir,arg)
        print "Output filename is %s\n" % (output_file)
        if os.path.isdir(outdir):   # Run the command mkdir in the system shell
            print "yes. there is an existing folder\n"
        else:
            os.mkdir(outdir)   # Run the command mkdir in the system shell
        output = True
    elif opt in ('-d', '--debug'):
        debug = True

# get the list of users from the key files in keydir
UsersList = os.listdir("keydir")   # Run the command ls in the system shell
# Count how many users are at this site
TOTALUSERS = len(Users)

if debug:
    print 'ARG INFO'
    print 'Logfile to scan  :', Log_file
    print 'debug   :', debug
    print 'output   :', output


##############################################################################
## -------------+
## Name         : Module Usage
## Purpose      : Displays Module usage
## Inputs       : None
## Outputs      : None
## -------------+
##############################################################################
def ThisModule:
    total = 0
    for ITEM in LIST:
        print "ITEM = " + CHECK
        if stock[ITEM] > 0:
            total += prices[ITEM]
            print total
            stock[ITEM] -= 1
    return total


#
# End of script
#


