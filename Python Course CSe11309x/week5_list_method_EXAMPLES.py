#!/usr/bin/env python3

# list.append(x)
# This method adds an item to the end of the list.
# It is equivalent to doing: a[len(a):] = [x]
my_list = ["Tom", "Henry", "Mickey", "Juliet", "Sophie"]    # Create a List
my_list.append("William")                                   # Append "William" to the end of the list
print(my_list)

# list.extend(x)
# This method extends the list by appending all the items in the given list.
# It is equivalent to doing: a[len(a):] = L
list_one = [1, 2, 3, 4, 5, 6, 7]                          # This is the first list
list_two = [10, 12, 14]                                   # This is the second list
list_one.extend(list_two)                                 # Extend list_one by appending all items of list_two
print(list_one)

# list.insert(i, x)
# This method inserts an item at a given position in the list. Where:
#     i : The index at which the item is to be inserted.
#     x : The item that is to be inserted.
my_list = ["Tom", "Henry", "Mickey", "Juliet", "Sophie"]    # Create a List
my_list.insert(1, "Siddhartha")                             # Insert the string "Siddhartha" at index 1
print(my_list)

# list.remove(x)
# This method removes the first item from the list whose value is x. It is an error if there is no such item.
my_list = ["Thou", "art", "precious!", "art", "gracious"]     # Create a list
my_list.remove("art")                                         # Remove the first occurrence of the string "art"
print(my_list)

# list.pop([i])
# This method removes the item at the given position in the list and returns it.
# If no index is specified , list.pop() removes the last item in the list.
# Note that the square brackets around the i in the method signature denotes that the parameter is optional, not that you should type square brackets at the position.
my_list = ["Thou", "art", "precious!", "art", "gracious"]        # Create a list
my_item = my_list.pop(2)                                         # Remove item at index 2 and return it
print("The item that was popped was: ", my_item)                 # Print my_item to see what was returned
print("my list now looks like = ", my_list)

# list.clear()
# This method removes all the items from the list.
# It is equivalent to doing: del a[:]
my_list = [2, 3, 5, 7, 11, 13]                                # Create a list
my_list.clear()                                               # Remove all the items from the list
print(my_list)

# list.index(x)
# This method returns the index in the list of the first item whose value is x.
# It is an error if there is not such item.
my_list = ["Python", "is", "awesome", "Java", "is", "Alright"]       # Create a list
my_index = my_list.index("is")                                       # Return the index of the first "is"
print("The item was first found at index:", my_index)

# list.count(x)
# This method returns the number of times x appears in the list
my_list = ["mew", "mew", "kitten", "mew", "mew"]                  # Create a list
my_count = my_list.count("mew")                                   # Return the number of times "mew" appears
print("The number of times the item appeared was:", my_count)


# list.sort(key=None, reverse=False)
# This method sorts the items of the list in place. Note that this method does not return anything.
# (The arguments are optional and can be used for sort customization, see sorted() for their explanation.)
my_list = [5, 3, 6, 1, 2, 3, 4, 7]                  # Create a list
my_list.sort()                                   # Sort the items of the list in place
print("Sorted list looks like:", my_list)

# list.reverse()
# This method reverses the items of the list in place. Note that this method does not return anything.
my_list = ["zero", "one", "two", "three", "four", "five"]        # Create a list
print("Original list:", my_list)
my_list.reverse()                                                # Reverse the items of the list in place
print("Reversed list looks like:", my_list)

# list.copy()
# This method returns a shallow copy of the list.
# It is equivalent to doing: a[:]
original_list = ["zero", "one", "two", "three"]        # Create a list
copied_list = original_list.copy()                     # Copy the original list and return it.
print("Copied list looks like:", copied_list)
