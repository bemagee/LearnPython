my_int = input("enter a integer: ")
print(my_int)
new_int = int(my_int)
x = type(new_int)
print(new_int, "of type", x)
if (new_int%3):
    print('No')
else:
    print('Yes')