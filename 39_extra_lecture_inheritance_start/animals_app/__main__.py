from .animals import Animal, Dog, Cat

print("Our Animals app")

dog = Dog(name="Reg", color="Brown", num_legs=4,
          breed="Golden Lab") # custom to Dog class
cat = Cat(name="Sushi", color="Black", num_legs=4,
          anger_level=10, pattern="Siamese") # custom to Cat class
bird = Animal(name="Barry", color="Yellow", num_legs=2)

# let's create a list of animals here
all_animals = [dog, cat, bird]

# let's loop through the animals and see how
# their functions behave.
for animal in all_animals:
    print("------------------")
    print(F"class type: {type(animal)}")
    print(animal)
    print("Using the functions\n") # \n stands for new line
    # let's test out methods of a class
    animal.make_a_noise()
    animal.eat()
    animal.move()

    # we can check to see if an animal is an instance of a certain class
    if isinstance(animal, Cat):
        animal.knock_over("glass")


    print("------------------")