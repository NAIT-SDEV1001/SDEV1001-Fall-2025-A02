# we're going to import a module built in to python
# that is called random
import random
# if you want to read the docs: https://docs.python.org/3/library/random.html#random.randint

# we're going to use randint to create a number from
# Note: variables can't have the same name as the module.
random_number = random.randint(1, 100)

# for debugging purposes
print(f"random number is {random_number}")