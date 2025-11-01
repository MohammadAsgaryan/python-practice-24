# Examples of bad error handling in Python

# 1. Catching all exceptions silently
try:
    x = 10 / 0
except:
    pass  # Error swallowed, bad practice

# 2. Using print instead of logging
try:
    value = int("abc")
except ValueError:
    print("Something went wrong")

# 3. Catching a wrong exception type
try:
    items = [1, 2, 3]
    print(items[10])
except ValueError:
    print("Wrong exception type - this will not work")
