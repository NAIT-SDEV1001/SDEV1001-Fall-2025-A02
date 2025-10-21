# in here we're going to create function

# let's modify this so that we get all of the toppings
# I'm going to do this with args.
def make_pizza(*args, size=None, crust=None):
    # args here is going to be our toppings.

    # make an f-string that can span multiple lines.
    print(F"""
    Summarizing the pizza
    a {size} inch pizza
    with a {crust}
    """)

    print("""
    Toppings to our pizza are as follows:
    """)
    # our args is going to be a list here.
    for topping in args:
        print(F"""     - {topping}""")