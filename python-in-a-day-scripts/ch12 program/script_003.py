# Our epic programmer dict from before
epic_programmer_dict = {
    'Tim Berners-Lee' : ['tbl@gmail.com', 111],
    'Guido van Rossum' : ['gvr@gmail.com', 222],
    'Linus Torvalds': ['lt@gmail.com', 333],
    'Larry Page' : ['lp@gmail.com', 444],
    'Sergey Brin' : ['sb@gmail.com', 555]
    }
print epic_programmer_dict

# Search for Tim Berners-Lee
print epic_programmer_dict['Tim Berners-Lee']

# Search for Tim Berners-Lee and get his number
print epic_programmer_dict['Tim Berners-Lee'][0]

programmer = epic_programmer_dict['Tim Berners-Lee']
print programmer[1]
