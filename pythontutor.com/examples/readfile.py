#!/c/python27/python

# Open a file
fo = open("foo.txt", "r")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print "Read Line: %s" % (line)

line = fo.readline(5)
print "Read Line: %s" % (line)

# Close opend file
fo.close()
