#!/c/python34/python

import fileinput
import os
import fnmatch

with fileinput.input(files=('repo.txt')) as f:
	for line in f:
	   print (line)
	   linenum = fileinput.lineno()
	   print (linenum)
	   print (fileinput.filename())
	   repoDir = '/home/brmagee/repositories'
	   for line, subdirList, fileList in os.walk(repoDir, followlinks=True):
	      print('Found directory: %s' % line)
	   else:
	      print('Error: no directory: %s' % line)

fileinput.close()
