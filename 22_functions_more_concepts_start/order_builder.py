# this is going to take our customer orders
# build our pizza accordingly.

# let's import the pizza module
import pizza

def main():
    print("Welcome to the order builder")

    # let's create a loop that's going to get
    # users creating pizza
    ordering_pizza = True
    while ordering_pizza:
        ordering = input("Order another pizza (y/n)")
        if ordering == "n":
            ordering_pizza = False
            return # we could return early as a function.
        size = int(input("what size do you want of pizza (number)?"))
        crust = input("what type of crust do you want?")

        # let's actually call our pizza with key arguments
        pizza.make_pizza(size=size, crust=crust)

# the right way to write files.
if __name__ == "__main__":
    main()