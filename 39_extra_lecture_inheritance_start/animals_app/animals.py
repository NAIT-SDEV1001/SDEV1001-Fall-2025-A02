class Animal:
    # define the constructor
    def __init__(self, name, color, num_legs):
        self.name = name
        self.color = color
        self.num_legs = num_legs

    # __str__ and __repr__
    def __str__(self):
        return F" Name {self.name}\n Color {self.color}\n Legs: {self.num_legs}"

    def __repr__(self):
        return F"Animal(name={self.name} color={self.color} num_legs={self.num_legs})"

    # lets' implement our functions here.
    def eat(self):
        print(F"{self.name} starts eating... ")

    def make_a_noise(self):
        print(F"{self.name} makes a noise")

    def move(self):
        print(F"{self.name} runs around")


# let's create a class that inherits from Animal
class Dog(Animal):
    # If you just use pass below (and nothing else it's going to have the same
    # functionality as animal.)
    # pass

    # let's override the init to have the same functionality
    def __init__(self,  name, color, num_legs, breed):
        # I want to use the constructor of the Animal class
        # we're going to do this using something called "super()".
        super().__init__(name, color, num_legs)
        self.breed = breed

    # let's continue to change the functionality but keep some the same.
    def __str__(self):
        # get the original animal string
        animal_string = super().__str__()
        # super().__str__() is calling the Animal (parent)'s method of __str__
        # we're just adding the breed to it.
        return F"{animal_string}\n Breed {self.breed}"

    def make_a_noise(self):
        print(F"{self.name} starts barking! bark! bark!")


# create a Cat class
# import it in the __main__
# change Sushi to use a Cat class
# add properties of breed, anger_level
# override make_a_noise to be dependant on the anger level
# less 30 purrs
# between 31-60 meow
# over 60 it hisses.