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

# let's take a look here at slicing lists
print("first three items")
print(groceries[0:3]) # groceries[:3]
print("Let's get the last 2 items")
print(groceries[-2:]) # this is the same as groceries[4:]
print("Let's get third and fourth of the list")
print(groceries[2:4])
# always based on the index.
# whenever you're going to access items in a list
# whether it's just the single item or
# multiple items in the list you use the []

# let's add an item at the end of the list




# Let's take a look at what happens if we sort the list
print("presorting")
print(groceries)
groceries.sort() # sorts the list in place
# sort is going sort numbers, and also
# sort names, do it's best effort of sorting.
print("sorted version of groceries")
print(groceries)
