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
        ordering = input("Order another pizza (y/n) ")
        if ordering == "n":
            ordering_pizza = False
            # you could use return here
            # you could use continue
        elif ordering == "y":
            size = int(input("what size do you want of pizza (number)? "))
            crust = input("what type of crust do you want? ")

            # let's think about toppings
            # you could have just a cheese pizza
            # you could have cheese, pepperoni, peppers, onions
            # you could have pineapple, no cheese, ham.
            # there's a different amount of toppings.
            toppings = []
            topping = input("Add a topping type (done) when done: ")
            while topping != "done":
                # we're going to make this an array of toppings
                toppings.append(topping)
                topping = input("Add a topping type (done) when done: ")

            breakpoint()

            # let's actually call our pizza with key arguments
            # we're just going to handle these toppings
            pizza.make_pizza(size=size, crust=crust)
        else:
            print("I didn't get that.")
# the right way to write files.
if __name__ == "__main__":
    main()