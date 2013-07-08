# Our epic programmer dict with lowercase names
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }

# Asks user to input persons name - converts to lowercase
personsName = raw_input('Please enter a name: ').lower()

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if there aren't any errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print 'Name: ' + personsName.title()
    print 'Email: ' + personsInfo[0]
    print 'Number: ' + str(personsInfo[1])
except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'
