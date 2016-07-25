#!/tools/bin/python
#  -------------+
#  Purpose      : Removes .nfs files from directory tree older than one day
#                 - executes a find command on the repository tree to find .nfs* files that are 
#                    left by caused by one side hanging up in the middle of an nfs transaction.  
#                    Perhaps something with the netapp filers
#                    -bash-3.2$ ls -la /projects/git-stg-bcg/gitbsesw/refsw/baseline.git/objects/pack/.nfs0000000000dc95020000074b
#                    -r--r--r-- 1 gitbsesw git_bcg_grp 5303197435 Jun 27 00
#  Command Line : ./remove_nfs_files.py
#  Inputs       : Arguments: Base directory of the Git repositories
#  Outputs      : 0 - On success
#               : 1 - Failed
#  Author       : Brian Magee
#  Orig Date    : 28 June 2016
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
NFS_LOG=('remove_nfs_files.' + str(now) + '.log')

# List of Directories
CURRENT_DIR = os.getcwd()
REPO_DIRS = os.path.join('/home/brmagee', 'repositories')
#REPO_DIRS=[CURRENT_DIR/repositories]

# Output Log
output_log = open(NFS_LOG, 'w')

print (now, ": Looking for repositories directory in - ", REPO_DIRS)

import fnmatch
import os

for file in os.listdir(REPO_DIRS):
    print file
    if fnmatch.fnmatch(file, '.nfs*'):
        print ("found nfs file:", file)
