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

            # we're going to add special requests to the toppings
            # we're going to prompt users for a topping
            # a special request like double cheese for example.
            # again this is going to be with dictionaries
            # which are similar to javascript objects.
            # similar in that they are key value pairs
            special_requests = {} # a dictionary
            # below is going to be the key.
            special_request_topping = input("""
            What topping would you like to modify (enter done) when done?
            """)
            while special_request_topping != "done":
                amount = input("How much? (light, extra, double)")
                # we're going to add this to the special
                # request dictionary
                # passing the topping as the key
                # and the amount is the value
                special_requests[special_request_topping] = amount
                special_request_topping = input("""
            What topping would you like to modify (enter done) when done?
                """)
            # going to look like the following
            # {'cheese': 'double', 'pepperoni': 'extra'}

            # let's actually call our pizza with key arguments
            # we're just going to handle these toppings
            # from the first step
            # pizza.make_pizza(size=size, crust=crust)
            # let's add the toppings and unpack them
            pizza.make_pizza(
                # below we're using arg unpacking
                *toppings, # these args need to be before key word arguments
                size=size,
                crust=crust,
                # we're going to take a look here at the toppings
                **special_requests
            )
        else:
            print("I didn't get that.")
# the right way to write files.
if __name__ == "__main__":
    main()