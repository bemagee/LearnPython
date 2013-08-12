# Page 287
# 6.1.1 Parsing Paths
import os.path
for path in [ '/one/two/three',
		'/one/two/three/',
		'/',
		'.',
		'']:
	print '%15s : %s' % (path, os.path.split(path))
