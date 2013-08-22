# call with two args count_debug.py PATTERN FILE
# example:  python count_debug.py DENIED ~/DEV/FLEXLM/MONITOR/debug.log

import fileinput, sys, string
match_cnt = 0
max_counter = 0
# take the first argument out of sys.argv and assign it to searchterm
searchterm, sys.argv[1:] = sys.argv[1], sys.argv[2:]
for line in fileinput.input():
    num_matches = string.count(line, searchterm)
    match_cnt = string.count(line, searchterm)
    if num_matches:                     # a nonzero count means there was a match
	print line
        print "found '%s' %d times in %s on line %d." % (searchterm, num_matches, 
            fileinput.filename(), fileinput.filelineno())
        max_counter = max_counter + 1
print "Total searchterm '%s' found %d." % (searchterm, max_counter)
