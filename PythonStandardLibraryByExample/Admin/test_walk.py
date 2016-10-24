#!/tools/bin/python
#  -------------+
# Import the os module, for the os.walk function

import os
import fnmatch
 
# Set the directory you want to start from
repoDir = '/home/brmagee/repositories'
for dirName, subdirList, fileList in os.walk(repoDir, followlinks=True):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
        if fnmatch.fnmatch(fname, '.nfs*'):
                print ("found nfs file:", fname)
