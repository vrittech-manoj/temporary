def add(x, y):
    return x + y

def add(x, y, z):
    return x + y + z

print(add(2, 3))       # Output: Error - TypeError: add() missing 1 required positional argument: 'z'
print(add(2, 3, 4))    # Output: 9
