import fileinput, sys, string
match_cnt = 0
# take the first argument out of sys.argv and assign it to searchterm
searchterm, sys.argv[1:] = sys.argv[1], sys.argv[2:]
for line in fileinput.input():
    num_matches = string.count(line, searchterm)
    match_cnt = string.count(line, searchterm)
    if num_matches:                     # a nonzero count means there was a match
        match_cnt += 1
        print "found '%s' %d times in %s on line %d." % (searchterm, num_matches, 
            fileinput.filename(), fileinput.filelineno())
        print match_cnt
