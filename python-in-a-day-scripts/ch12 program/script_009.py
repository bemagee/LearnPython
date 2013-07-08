# Our epic programmer dict
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555]
    }

# Asks user to input persons name
personsName = raw_input('Please enter a name: ').lower()

# Looks up the name in the epic dictionary
try:
    # Trys the following lines of texts, and if there isn't any errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print 'Name: ' + personsName.title()
    print 'Email: ' + personsInfo[0]
    print 'Number: ' + str(personsInfo[1])
except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'

# Adding the loop
userWantsMore = True
while userWantsMore == True:
    # Code goes here
    userWantsMore = False
