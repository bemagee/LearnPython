# Make function called letsAdd
def letsAdd(x,y):
    # Make addition variable equal to x + y
    addition = x + y

    # See how putting this in function does
    # not affect outside of function
    someValue = 10

    # Return addition variable
    return addition

print letsAdd(3, 5)
print someValue
