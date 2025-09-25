groceries  = [
    "lettuce",
    "tomatoes",
    "bread",
    "milk",
    "chicken",
    "apples"
]
# the entire list.
print("groceries")
print(groceries)

# accessing items
# the you access items in a list is you have
# an index, and you put this in square brackets
# an index starts at 0
# the last index is -1 or length of the list -1

print(F"First item in the list is {groceries[0]}")

print(F"the length of the list is {len(groceries)}")

last_index = len(groceries) - 1
print(F"the last item is {groceries[last_index]}")

# in the breakpoint I'm going to check the error
# if i try to access an index outside of the list (say 1000)
# the error looks like the following IndexError: list index out of range
# breakpoint()

