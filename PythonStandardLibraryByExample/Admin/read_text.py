#!/c/python34/python

import fileinput

with fileinput.input(files=('repo.txt')) as f:
	for line in f:
	   print (line)
	   linenum = fileinput.lineno()
	   print (linenum)
	   print (fileinput.filename())
fileinput.close()
