import linecache

filename = '/etc/passwd'

# Pick out the same line from source and cache.
# (Notice that linecache counts from 1)
print 'SOURCE:'
print '%r' % linecache.getline(filename, 4)
print
print 'CACHE:'
print '%r' % linecache.getline(filename, 5)

