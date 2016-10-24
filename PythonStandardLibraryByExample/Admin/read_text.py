#!/usr/bin/env python

import fileinput
import os
import fnmatch

with fileinput.input(files=('repo.txt')) as f:
   for line in f:
#      print (line)
      print('text file: %s' % fileinput.filename(),'line number: %s' % fileinput.lineno())
      repoBaseDir = '/home/brmagee/repositories/'
      repoDir = ''.join([repoBaseDir, line]).rstrip()
      print (repoDir)

      if os.path.isdir(repoDir):
         print('Found directory: %s' % repoDir)
      else:
         print('Error: no directory: %s' % repoDir)

fileinput.close()
