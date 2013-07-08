# Create programmer dictionary
epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
                        'Guido van Rossum' : 'gvr@gmail.com',
                        'Linus Torvalds': 'lt@gmail.com' }

# Add more programmers to the dictionary
epic_programmer_dict['Larry Page'] = 'lp@gmail.com'
epic_programmer_dict['Sergey Brin'] = 'sb@gmail.com'
epic_programmer_dict['Me'] = 'me@gmail.com'

# Delete Sergey Brin from the dictionary
del epic_programmer_dict['Sergey Brin']

# Check the dictionary to see if Sergey Brin was removed
print epic_programmer_dict
