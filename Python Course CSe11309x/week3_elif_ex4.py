# Write a program which asks the user to type a string and then:
# Print "Dog" if "dog" is in the input string.
# Print "Cat" if "cat" is in the input string. (if both "dog" and "cat" are in the input string then you should only print "Dog")
# Otherwise prints "None". (Pay attention to capitalization).

user_response=input("Type anything:")
if 'dog' in user_response:
    print ('Dog')
elif 'cat' in user_response:
    print ('Cat')
else:
    print ('None')