n = [[1, 2, 3], [4, 5, 6, 7, 8, 9],[10, 11]]
# Add your function here

def flatten(*args):
    total = []
    for i in range(len(args)):
        for j in range(len(args[i])):
            total = total + args[i][j]
    return total

print flatten(n)
