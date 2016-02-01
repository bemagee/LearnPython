# Write a program that asks the user to enter a positive integer n. Assuming that this integer is in seconds, your
# program should convert the number of seconds into days, hours, minutes, and seconds and prints them exactly in the
# format specified below. Here are a few sample runs of what your program is supposed to do:

# when user enters
# 369121517
# your program should print:
# 4272 days 5 hours 45 minutes 17 seconds

# when user enters
# 24680
# your program should print:
# 0 days 6 hours 51 minutes 20 seconds

# when user enters
# 129600
# your program should print:
# 1 days 12 hours 0 minutes 0 seconds

# Note that the numbers and words in the above output are separated by only one space. All the words are in lower case.
# Your output should exactly match the format shown above.

entered_seconds = input("Enter the number of seconds: ")
seconds = int(entered_seconds)

if seconds < 0 :
    print("INVALID")
elif seconds >= 86400 :
    days = seconds//86400
    hours_left = seconds%86400
    if hours_left > 0 :
        hours = hours_left//3600
        seconds_left = hours_left%3600
print("seconds entered", seconds, "days", days, "hours", hours_left, "seconds", seconds_left)