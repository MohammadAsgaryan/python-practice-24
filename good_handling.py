import logging

logging.basicConfig(level=logging.ERROR)

# 1. Handling the correct exception with logging
try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Division error: {e}")

# 2. Using proper exception type
try:
    value = int("abc")
except ValueError as e:
    logging.error(f"Invalid integer conversion: {e}")

# 3. Correct exception for list index
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as e:
    logging.error(f"List index out of range: {e}")
