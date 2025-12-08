from .animals import Animal, Dog

print("Our Animals app")

dog = Dog(name="Reg", color="Brown", num_legs=4)
cat = Animal(name="Sushi", color="Black", num_legs=4)
bird = Animal(name="Barry", color="Yellow", num_legs=2)

# let's create a list of animals here
all_animals = [dog, cat, bird]

# let's loop through the animals and see how
# their functions behave.
for animal in all_animals:
    print("------------------")
    print(animal)
    print("Using the functions\n")
    # let's test out methods of a class
    animal.make_a_noise()
    animal.eat()
    animal.move()
    print("------------------")