#!/tools/bin/python
#  -------------+
#  Purpose      : Update all of the gitolite admin repos
#                 - runs "git pull" on every gitolite-admin directory found
#  Command Line : ./pull_all.py
#  Inputs       : Arguments: the Gitolite Slave Host to push updates
#  Outputs      : 0 - On success
#               : 1 - Failed
#  Author       : Brian Magee
#  Orig Date    : 28 January 2015
#  Version      : 1.0
#  -------------+

# Modules
import os
import subprocess
import time
from datetime import date
import fnmatch

# Var Initialize
RETURN_VAL = 0
now = date.today()
PULL_LOG=('pull_' + str(now) + '.log')

# List of Directories
GITOLITE_DIRS=[]
CURRENT_DIR = os.getcwd()

# Output Log
output_log = open(PULL_LOG, 'w')

print (now, ": Collecting Directory List from - ", CURRENT_DIR)
#output_log.write (now, ": Collecting Directory List from - ",% CURRENT_DIR)

# walk directory structure to populate dirs list
for root, dir, files in os.walk('/home/brmagee/gitolite_groups'):
    for pulldir in fnmatch.filter(dir, "gitolite-admin"):
        #print ("DIR:", root)
        #print ("pulldir:", root+"/"+pulldir)
        PULLDIR=root+"/"+pulldir
        GITOLITE_DIRS.append(PULLDIR)
        #print ("pulldir:", PULLDIR)
print("\n")

# use th dirs list to cd to each and run git pull
for DIR in GITOLITE_DIRS:
    os.chdir(DIR)
    #PWD=os.popen("/bin/pwd").read()
    print ('git pull on: %s' % DIR)
    #PULL_OUT=subprocess.popen("/tools/bin/git pull").read()
    PULL_OUT=os.popen("/tools/bin/git pull").read()
    REMOTE_OUT=os.popen("/tools/bin/git remote -v").read()
    if RETURN_VAL == 0:
        output_log.write("OK: git pull on:")
        output_log.write(DIR)
        output_log.write(PULL_OUT)
        output_log.write(REMOTE_OUT)
        output_log.write('\n')
    else:
        print ("ERROR:", DIR)
        output_log.write("ERROR: git pull on:")
        output_log.write(DIR)
        output_log.write(PULL_OUT)
        output_log.write('%3s\n' % (str(RETURN_VAL)))
