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

if __name__ == "__main__":
    first_car = Car("toyota", "corolla", 2006)
    second_car = Car("Cadillac", "escalada", 2020)
