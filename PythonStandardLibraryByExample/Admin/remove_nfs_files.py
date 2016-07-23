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
#REPO_DIRS=[]
REPO_DIRS = os.path.join('/home/brmagee', 'repositories')
CURRENT_DIR = os.getcwd()

# Output Log
output_log = open(NFS_LOG, 'w')

print (now, ": Looking for repositories directory in - ", CURRENT_DIR)

# walk directory structure to populate dirs list
for root, dir, files in os.walk('repositories'):
    for repodir in fnmatch.filter(files, '.nfs*'):
        print ("NFS FILE:", file)
        print ("repodir:", root+"/"+repodir)
        NFS_FILE=root+"/"+repodir
        REPO_DIRS.append(NFS_LOG)
        #print ("repodir:", NFS_LOG)
print("\n")

# use the dirs list to cd to each and run find for .nfs files 
for DIR in REPO_DIRS:
    os.chdir(DIR)
    #PWD=os.popen("/bin/pwd").read()
    print ('find on: %s' % DIR)
    #NFS_LOG=subprocess.popen("/tools/bin/git pull").read()
    NFS_LOG=os.popen("/tools/bin/find . -name '.nfs*' -print").read()
    FIND_OUT=os.popen("/tools/bin/find . -name '.nfs*' -print").read()
    if RETURN_VAL == 0:
        output_log.write("OK: find on:")
        output_log.write(DIR)
        output_log.write(NFS_OUT)
        output_log.write(FIND_OUT)
        output_log.write('\n')
    else:
        print ("ERROR:", DIR)
        output_log.write("ERROR: find on:")
        output_log.write(DIR)
        output_log.write(NFS_OUT)
        output_log.write('%3s\n' % (str(RETURN_VAL)))
