import os
import re

count = 0
pattern = 'ab'

fm = open('bm','r')
for line in fm:
    for match in re.findall(pattern, line):
        print 'Found "%s"' % match
        print 'Here it is "%s"' % line
        count = count + 1
print count

