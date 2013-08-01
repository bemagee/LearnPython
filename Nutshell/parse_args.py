import optparse 

def main(): 
    p = optparse.OptionParser() 
    p.add_option('--verbose', '-v', action='store_true') 
    p.add_option('--name', '-n', default="world") 
    options, arguments = p.parse_args() 
    if options.verbose: print "Greetings and salutations,", 
    else: print "Hello", 
    print '% s!' % options.name 

if __name__ == '__main__': 
    main()

"""
Martelli, Alex (2009-06-30). Python in a Nutshell (Kindle Locations 6861-6865). O'Reilly Media. Kindle Edition. 
"""
