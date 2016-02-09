# abs(x)
# This method returns the absolute value of a number. The argument maybe an integer or a floating point number.
# If the argument is a complex number, its magnitude is returned.
my_value = -11.55                             # Notice that my_value is a negative floating point number
absolute = abs(my_value)                     # Return the absolute value
print("The absolute value is:", absolute)


# len(x)
# This method returns the length (the number of items) of an object. The argument maybe an sequence (such as a string
# , bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

my_list = ["abs", "len", 1, 2, "many", "more to come"]      # Create a list called "my_list"
my_size = len(my_list)                                      # Return length (the number of items) of my_list
print("The length of my_list is:", my_size)

# max(iterable, *[, key, default])
# max(arg1, arg2, *args[, key])
# This method returns the largest item in an iterable or the largest of two or more arguments.
my_list = [-10, 12, 111, 32.3, 0, 4, 24]                        # Create a list called "my_list"
my_max1 = max(my_list)                                          # Return the largest item in my_list
my_max2 = max(my_list[0], my_list[-1])                          # Return the largest among first & last element
print("The largest item of my_list is:", my_max1)               # Print my_max1 to see what was returned
print("The larger among first and last item is:", my_max2)


# min(iterable, *[, key, default])
# min(arg1, arg2, *args[, key])
# This method returns the smallest item in an iterable or the smallest of two or more arguments.
my_list = [10, -12, 11, 32.3, 1, 14, -5]                         # Create a list called "my_list"
my_min1 = min(my_list)                                           # Return the smallest item in my_list
my_min2 = min(my_list[0], my_list[-1])                           # Return the smallest among first & last element
print("The smallest item of my_list is:", my_min1)               # Print my_min1 to see what was returned
print("The smaller among first and last item is:", my_min2)

# pow(x, y[, z])
# This method returns x to the power y. The argument z is optional. If z is present then it returns x to the
# power of y, modulo z. Note that pow(x, y) is equivalent to using the power operator: x**y
x = 5                                                   # initialize a variable x
y = 3                                                   # initialize a variable y
result = pow(x, y)                                      # Return x to the power of y. Same as x**y
print("The result of the operation is", result)

# sorted(iterable[, key][, reverse])
# This method returns a new sorted list from the items in iterable.
# Has two optional arguments which must be specified as keyword arguments.
#     key: specifies a function of one argument that is used to extract a comparison key from each list element:
#          key=str.lower. The default value is None (compare the elements directly).
#    reverse: is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
# Lets sort the following list by the first item in each sub-list.
my_list = [[2, 4], [0, 13], [11, 14], [-14, 12], [100, 3]]

# First, we need to define a function that specifies what we would like our items sorted by
def my_key(item):
    return item[0]                                            # Make the first item in each sub-list our key

new_sorted_list = sorted(my_list, key=my_key)                 # Return a sorted list as specified by our key
print("The sorted list looks like:", new_sorted_list)

# sum(iterable[, start])
# This method sums start and the items of an iterable from left to right and returns the total. start
# defaults to 0. The iterable items are normally numbers and the start value is not allowed to be a string.
my_list = [1, 2, 3, 4, 5]                        # Create a list
my_sum = sum(my_list)                           # Return the sum of the list
print("The sum of my list is :", my_sum)         # Print my_sum

# zip(*iterables)
# This method returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument
# sequence of iterables. The iterator stops when the shortest input iterable is exhausted.
x = [1, 2, 3, 4, 5]                                      # Create a list
y = ['a', 'b', 'c']                                      # Note that this list only has 3 elements
zipped = list(zip(x, y) )                                # Return the zipped object as a list of tuples
print("The result of the operation is:", zipped)

