class Car:
    # define constructor which will be method
    # called on creation
    # you need to make self as the first arguemnt
    # to the instance itself.
    def __init__(self, make, model, year):
        # attach the parameters to the object itself
        self.make = make
        self.model = model
        self.year = year

    # let's add a method here.
    def honk(self): # self will always be the first param in python
        print(F"{self.make} {self.model} is honking")

    # to make our output in the code not look like
    # <__main__.Car object at 0x000002A02ED76F90> for example
    # we need to create a string method
    def __str__(self):
        return F"Car(make={self.make}, model={self.model}, year={self.year})"

if __name__ == "__main__":
    first_car = Car("toyota", "corolla", 2006)
    second_car = Car("Cadillac", "escalade", 2020)

    # when using the methods you're going to see that there's
    # a difference in the objects when calling honk.
    first_car.honk()
    second_car.honk()

    print("let's take a look at what the classes look like")
    print(first_car)
    print(second_car)