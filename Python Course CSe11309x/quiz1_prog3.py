dayoftheweek = ['Noday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pickday = 0
while pickday in range(1,7):
    pickday = input("Enter day 1 to 7:")
    pickday = int(pickday)
print("day picked", dayoftheweek[pickday])
