# I want you to create a dictionary

# patties: 2
# patty_type: beef
# cheese: true
# toppings: lettuce, tomato, eggs
# bun: ciabatta
burger = {
    "patties": 2, # int
    "patty_type": "beef", # string
    "cheese": True, # boolean
    "toppings": [ # a list of items
        "lettuce",
        "tomato",
        "eggs",
    ],
    "bun": "ciabatta" # string
}

# print out the dictionary.
# print(burger)

# I want you to print out a couple of things
# THe number of patties and the patty type by accessing the
print(F"You have {burger['patties']} {burger['patty_type']} patties on your burger")
# dictionary via keys
# make if statement that will check if the use has cheese.
if burger["cheese"]: # it's true or false
    print("you have cheese on this burger")

# I'm going to get you folks to list in order with the index
# the toppings on the burger
print("your toppings are")
# for index, topping in enumerate(burger['toppings']): # burger['toppings'] is a list of strs.
# the same as doing
for index in range(len(burger["toppings"])):
    topping = burger["toppings"][index]
    print(F"- {index + 1}: {topping}")
