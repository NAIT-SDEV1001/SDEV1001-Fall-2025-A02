# Inheritance

## Why is this important?

Inheritance is a very important concept in Object Oriented Programming. It allows us to extend existing functionality of a class to other classes without having to rewrite code.

At a high level, inheritance is the idea that class can inherit properties and methods from other classes. There are parent classes and child classes, where the child inherits the properties and methods from the child.

The best way to illustrate this of course, is through an example. We will be using the example of Animals.


## Steps

1. Create two files: `__main__.py` which will hold our main program, and `animals.py` which will hold our classes.

2. In `animals.py`, add the following code

```python
class Animal:
    def __init__(self, name, color, num_legs):
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nNumber of Legs: {self.num_legs}"

    def __repr__(self):
        return f"Animal(name={self.name}, color={self.color}, num_legs={self.num_legs})"

```
This a class called `Animal`, which contains some of the attributes that all animals have: a name, a color, and the number of legs. We are overriding the `__str__` and `__repr__` methods here as well to show the values of these properties.

In addition to attributes of animals, let's add some of the things that all animals __do__. Add the following methods to the `Animal` class

```python
    def eat(self):
        print(f"{self.name} starts eating. Nom nom nom...")

    def make_a_noise(self):
        print(f"{self.name} makes an interesting noise.")

    def move(self):
        print(f"{self.name} runs around!")
```

All animals (for the purposes of this lesson) make some sort of noise, eat, and move.

Now the the `Animal` class is complete, add the following code to `__main__.py` so we can see this code in action.

This code is going to create three new animals, a dog, a cat, and a bird.

```python
def main():
    # create the animals
    dog = Animal("Ranger", "Brown", 4)
    cat = Animal("Soul Destroyer", "Black", 4)
    bird = Animal("Furry Birdy", "Green", 2)

    # add animals to list
    animals = [dog, cat, bird]

    # loop through the attributes and methods of each animal
    for animal in animals:
        print("-----------------")
        print(animal)
        
        animal.make_a_noise()
        animal.move()
        animal.eat()
        print("-----------------")

if __name__ == "__main__":
    main()
```

So we've created our three animals. They all make noises, move around, and eat and the attributes are displayed correctly.

But dogs, cats, and birds make different sounds. They have their own attributes unique to their species. How can we have the same attributes and methods as all animals in addition to having unique attributes and methods without duplicating code?

The answer is inheritance.

With inheritance, there is a parent class and child classes. Child classes "inherit" all of the attributes and methods from their parent, so the code does not have to be rewritten.

We can create a new class that has the same attributes and methods as Animal, but also its own unique attributes and methods.


Let's start by creating a Dog class, starting with the constructor.

```python
class Dog(Animal):
    def __init__(self, name, color, num_legs, breed):
        super().__init__(name, color, num_legs)
        self.breed = breed
```

In the constructor we include the same parameters as the Animal class, but we have added a fourth one specific to the Dog, breed.

Notice the use of the line `super()`. This is a reference to the __parent__ class, Animal. When we execute the line `super().__init__(name, color, num_legs)` we are calling the __parent constructor__. This is required because the constructor in the `Animal` class is what sets the name, color, and num_legs attributes. While not strictly necessary, it is most common to call the parent constructor at the beginning of the child constructor before setting attributes of the child.

We can use `super()` to access the methods of the parent class instead of the current class. We will see another example of this later.

Back in the `__main__.py`, change the setting of the `dog` variable to be a `Dog` class instead of an `Animal`. Make sure to include the new `breed` parameter. 

```python
dog = Dog("Ranger", "Brown", 4, "Labrador")
```

Run the code again.

Notice that everything runs exactly as it had originally, even though the methods and attributes don't exist in the `Dog` class. But because `Dog` inherits from `Animal`, `Dog` contains all of the same attributes and methods as `Animal`.

But `breed` isn't printing. This because it is not included in the `__str__` method of Dog.

With inheritance we can __override__ methods that belong to the parent class. Meaning that these methods will execute instead of the one in the parent. All we need to do is a define a method in the child with the same name.

Write the following code in the `Dog` class to override the `__str__` method so that when we print the `Dog` class, this version is executed instead.

```python
def __str__(self):
    # call the Animal __str__() to get the name, color, and num_legs string.
    return_string = super().__str__() 

    # append the breed attribute of the dog
    return_string += f"\nBreed: {self.breed}"

    # return the updated string
    return return_string
```

First we are calling the `Animal` implementation of the `__str__()` method, since this string contains our name, color, and num_legs. Afterwards we append the breed to that string and return the updated version. We could just write a string that includes all 4 attributes in the `Dog` implementation instead of calling `super().__str__()`, but this saves us rewriting code. 

We can override any methods in the parent, including ones we have written ourselves. Let's override the `make_a_noise()` method in the `Dog` class to be more specific to how a dog makes a noise.

Add the following code to the `Dog` class.

```python
def make_a_noise(self):
    print(f"{self.name} starts barking loudly! Bark Bark!")
```

Now when we call `make_a_noise()`, this will execute instead of the default one specified in `Animal`.

Child classes can have their own unique methods. Dogs chase cars sometimes, so write the following code in the `Dog` class:

```python
def chase_car(self):
    print(f"{self.name} chases after a Honda Civic!")
```

In `__main__.py` call this new method after the eat() method call:

```python
animal.make_a_noise()
animal.move()
animal.eat()
animal.chase_car() # add the chase_car() method call
```

When you execute this code, you will notice that when the animal is a `Dog`, the code executes just fine, but when it is __not__ a `Dog`, the program crashes.

This is because only the `Dog` class has this method, not the `Animal` class.

To fix this, we need to make sure that the variable is a `Dog` before executing it. Use the built-in Python function `isinstance()` to check what type a variable is. It will return True or False indicating if the variable is of the type specified.

```python
animal.make_a_noise()
animal.move()
animal.eat()

# check that the animal is a dog before executing chase_car()
if isinstance(animal, Dog):
    animal.chase_car()
```


Exercises
--------------------------------------------
Implement a Cat and Bird classes that inherit from Animal. Don't forget to change the class types of the cat and bird variables in `__main__.py`.

These are the requirements:

Cat:
- cats have the "pattern" attribute (string) that describes their pattern ("tabby", "solid color", etc.) and an "anger_level" attribute (int) that represents the cat's default anger level.
- When a cat makes a noise:
    - If the anger_level is less than 10, it should say "Purr purr".
    - If the anger_level is between 10 and 20, it should say "Meow meow".
    - If the anger_level is over 20, it should say "Hiss!"
- The properties should print as part of the `__str__` method.
- Create a method that will make the cat knock things off of a ledge.

- In the `__main__.py`, update the code so that the method that knocks things off is called when the animal is a Cat.

Bird
- Birds should have a wingspan attribute (float) that represents the bird's wingspan.
- When the bird eats, it should peck at food instead of going "nom nom nom."
- When a bird moves it should fly around.
- When the bird makes a noise it should say "I want crackers".
- The wingspan should be part of the output of the `__str__` method.