class Animal:
    # define the constructor
    def __init__(self, name, color, num_legs):
        self.name = name
        self.color = color
        self.num_legs = num_legs

    # __str__ and __repr__
    def __str__(self):
        return F"Name {self.name}\n Color {self.color}\n Legs: {self.num_legs}"

    def __repr__(self):
        return F"Animal(name={self.name} color={self.color} num_legs={self.num_legs})"