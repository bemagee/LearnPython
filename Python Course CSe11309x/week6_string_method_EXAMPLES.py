#!/usr/bin/env python3



# String Methods With Examples

# ***Remember: square brackets indicate optional arguments.***

# str.capitalize( )
# This method returns a copy of the first character capitalized and the rest lowercased.
my_string = "sTrInG mEtHoDs"                # Create a string
new_string = my_string.capitalize()         # Capitalize 1st, lower rest & return
print("original string =", my_string, "-> new string =", new_string)

# str.casefold( )
# This method returns a casefolded copy of the string. Casefolded strings may
# be used for caseless matching. Casefolding is similar to lowercasing but more
# aggressive because it is intended to remove all case distinctions in a string.
my_string = "sTrInG mEtHoDs"               # Create a String
new_string = my_string.casefold()          # Return a casefolded copy
print("original string =", my_string, "-> new string =", new_string)

# str.center(width[, fillchar])
# This method returns a centered in a string of length width. Padding is done
# using the specified fillchar (default is an ASCII space). The original string
# is returned if width is less than or equal to len(s).
my_string = "sTrInG mEtHoDs"               # Create a String
new_string = my_string.center(20, 'x')     # Center in 20 spaces, fill spaces with 'x' & return
print("original string =", my_string, "-> new string =", new_string)

# str.count(sub[, start[, end]])
# This method returns the number of non-overlapping occurrences of substring sub
# in the range [start, end]. Optional arguments start and end are interpreted as
# in slice notation.
my_string = "this is python. It is awesome!"     # Create a String
my_count = my_string.count('is', 0, -1)          # count occurrences of'is' and return
print("original string =", my_string, "-> how many 'is' strings =", my_count)


# str.endswith(suffix[, start[, end]])
# This method returns True if the string ends with the specified suffix, otherwise
# returns False. suffix can also be a tuple of suffixes to look for. With optional
# start, test beginning at that position. With optional end, stop comparing at that
# position.
my_string = "we love python"              # Create a String
my_value = my_string.endswith('python')   # Return a boolean
print("original string =", my_string, "-> does string end with 'python' =", my_value)

# str.find(sub[, start[, end]])
# This method returns the lowest index in the string where substring sub is found
# such that sub is contained in the slice s[start:end]. Optional arguments start
# and end are interpreted as in slice notation. This method returns -1 if sub is
# not found.
my_string = "we love python"        # Create a String
my_index = my_string.find('o')      # Return the lowest index where substring was found
print("original string =", my_string, "-> what is the lowest string index for 'o' =", my_index)

# str.format(*args, **kwargs)
# This method performs a string formatting operation. The string on which this
# method is called can contain literal text or replacement fields delimited by
# braces {}. Each replacement field contains either the numeric index of a positional
# argument, or the name of a keyword argument. It returns a copy of the string where
# each replacement field is replaced with the string value of the corresponding argument.
a = 10
b = 30
my_sum = a + b
my_product = a * b
print("The sum of a and b is {0} and their product is {1}".format(my_sum, a*b))

# str.index(sub[, start[, end]])
# This method returns the lowest index in the string where substring sub is found
# such that sub is contained in the slice s[start:end]. Optional arguments start
# and end are interpreted as in slice notation. This method is very similar to str.find
# except it raises a ValueError if the substring is not found.
my_string = "we love python"        # Create a String
my_index = my_string.index('o')     # Return lowest index at which the substring was found
print("original string =", my_string, "-> what is the string index for 'o' =", my_index)

# str.isalnum()
# This method returns True if all the characters in the string are alphanumeric and
# there is at least one character, False otherwise.
my_string_1 = "StarWars2016"              # Notice there is no space
my_string_2 = "I love star wars 2016"     # This string contains spaces
check_1 = my_string_1.isalnum()           # Returns a Boolean value
check_2 = my_string_2.isalnum()           # Returns a Boolean value
print ("check_1 is: {0} and check_2 is: {1}".format(check_1, check_2))   # Check to see what was returned

''' Several other methods that are similar to str.isalnum() which return some
Boolean value are as following:

str.isalpha()
Return True if all characters in the string are alphabetic and there is at least one
character, False otherwise. Alphabetic characters are those characters defined in the
Unicode character database as 'Letter'

str.isdecimal()
Return True if all characters in the string are decimal characters and there is at
least one character, False otherwise. Decimal characters are those from general category
'Nd'. This category includes digit characters, and all characters that can be used to
form decimal-radix numbers, e.g. U+0660, ARABIC-INDIC DIGIT ZERO.

str.isdigit()
Return True if all characters in the string are digits and there is at least one character,
False otherwise. Digits include decimal characters and digits that need special handling,
such as the compatibility superscript digits. Formally, a digit is a character that has the
property value Numeric_Type=Digit or Numeric_Type=Decimal.

str.isidentifier()
Return True if the string is a valid identifier according to the language definition, section
Identifiers and Keywords.

str.islower()
Return True if all cased characters in the string are lowercase and there is at least one
cased character, false otherwise.

str.isnumeric()
Return True if all characters in the string are numeric characters, and there is at least
one character, False otherwise. Numeric characters include digit characters, and all characters
that have the Unicode numeric value property

str.isprintable()
Return True if all characters in the string are printable or the string is empty, False
otherwise. Nonprintable characters are those characters defined in the Unicode character
database as 'Other' or 'Separator', excepting the ASCII space (0x20) which is considered
printable.

str.isspace()
Return True if there are only whitespace characters in the string and there is at least
one character, False otherwise. Whitespace characters are those characters defined in the
Unicode character database as 'Other' or 'Separator' and those with bidirectional property
being one of 'WS', 'B', or 'S'.

str.istitle()
Return True if the string is a titlecased string and there is at least one character, for
example uppercase characters may only follow uncased characters and lowercase characters
only cased ones. Return False otherwise.

str.isupper()
Return True if all cased characters in the string are uppercase and there is at least one
cased character, False otherwise

'''

# str.lstrip([chars])
# This method returns a copy of the string with leading characters removed. The chars
# argument is a string specifying the set of characters to be removed. If omitted or
# None, the Chars argument defaults to removing whitespace. The chars argument is not
# a prefix; rather all combinations of its values are stripped.
my_string = "   python is fun"     # Notices the whitespaces
new_string = my_string.lstrip()    # strip leading characters & return
print("original string =", my_string, "-> new string =", new_string)

# str.replace(old, new[, count])
# This method returns a copy of the string with all occurrences of substring old
# replaced by new. If the optional argument count is given, only the first count
# occurrences are replaced.
my_string = "we love python very very much"     # Notice there are five spaces in the string
new_string = my_string.replace(" ", "Z", 3)     # Replace first 3 white spaces with 'Z' & return
print("original string =", my_string, "-> new string =", new_string)


# str.rfind(sub[, start[, end]])
# This method returns the highest index in the string where substring sub is found
# such that sub is contained in the slice s[start:end]. Optional arguments start and
# end are interpreted as in slice notation. This method returns -1 if sub is not found.
my_string = "we love python"        # Create a String
my_index = my_string.rfind('o')     # Return the highest index at which the substring was found
print("original string =", my_string, "-> what is the highest string index for 'o' =", my_index)

# str.rindex(sub[, start[, end]])
# This method performs like rfind() but raises ValueError when the substring sub is not found.


# str.split(sep=None, maxsplit=-1)
# This method returns a list of the words in the string, using sep as the delimiter
# string. If maxsplit is given, at most maxsplit splits are done. If maxsplit is
# not specified or -1, then there is no limit on the number of splits.
my_string = "1,3,5,7,9,11"         # Notice that the numbers here are separated by commas
my_list = my_string.split(',')     # Return a list, split using comma as delimiter
print("original string =", my_string, "-> converted to a list split on ',' =", my_list)

# str.strip([chars])
# This method returns a copy of the string with the leading and trailing characters removed.
# The chars argument is a string specifying the set of characters to be removed. If omitted
# or None, the chars argument defaults to removing whitespace. The char argument is not a
# prefix or a suffix; rather, all combinations of its values are stripped.
my_string = "    https://docs.python.org/3/     "    # Notice the white spaces in the string
new_string = my_string.strip()                       # Remove all leading & trailing characters & return
print("original string =", my_string, "-> new string =", new_string)

