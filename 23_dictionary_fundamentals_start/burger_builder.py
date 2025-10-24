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

# wait
# you're actually vegan
# I want you to reassign the values on the burger
# patties 4
burger["patties"] = 4
# patty_type as beyond burger
burger["patty_type"] = "beyond burger"
# cheese False
burger["cheese"] = False
# toppings: arugula, tomato, pickle
burger["toppings"] = ["arugula", "tomato", "pickle"]
# bun: sesame seed bun.
burger["bun"] = "sesame seed"


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

# so that you folks understand how to loop through keys
# values
print("Debugging so that we know our entire dictionary")
for key, value in burger.items():
    # for example on the first iteartion
    # key is patties, value is 4

    print(F"key is {key}, value is {value}")
