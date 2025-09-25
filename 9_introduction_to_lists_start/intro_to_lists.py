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
groceries.append("more apples granny smith (better ones)")

# let's insert an item
groceries.insert(1, "fish")

# so can you rename things
# we really want iceberg lettuce.
# and we also know that the index of lettuce is 0
GROCERY_ITEM = "iceberg lettuce" #
groceries[0] = GROCERY_ITEM
# same as the assignment operator.
# let's take a look at where the index is

# Let's take a look at what happens if we sort the list
print("presorting")
print(F"the presorted index of {GROCERY_ITEM} is {groceries.index(GROCERY_ITEM)}")
print(groceries)
groceries.sort() # sorts the list in place
# sort is going sort numbers, and also
# sort names, do it's best effort of sorting.
print("sorted version of groceries")
print(groceries)

print(F"the sorted index of {GROCERY_ITEM} is {groceries.index(GROCERY_ITEM)}")

# remove items in this list
REMOVE_ITEM = "apples"
# this is going to remove with the value name
groceries.remove(REMOVE_ITEM)

# let's remove fish at index
groceries.pop(2)

print("after our removals")
print(groceries)
