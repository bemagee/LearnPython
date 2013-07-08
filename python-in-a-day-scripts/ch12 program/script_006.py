# Our epic programmer dict from before
epic_programmer_dict = {
    'Tim Berners-Lee' : ['tbl@gmail.com', 111],
    'Guido van Rossum' : ['gvr@gmail.com', 222],
    'Linus Torvalds': ['lt@gmail.com', 333],
    'Larry Page' : ['lp@gmail.com', 444],
    'Sergey Brin' : ['sb@gmail.com', 555]
    }

# Asks user to input persons name
personsName = raw_input('Please enter a name: ')

# Looks up the name in the epic dictionary
try:
    # Tries the following lines of texts, and if there isn't any errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print personsInfo
except:
    # If there are errors, then this code gets run.
    print 'No information found for that name'

