# in here we're going to create function

# let's modify this so that we get all of the toppings
# I'm going to do this with args.
def make_pizza(
        *args,
        size=None,
        crust=None,
        **kwargs
    ):
    # args here is going to be our toppings.
    # kwargs is going to be our special requests.
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
        print(F"""      - {topping}""")

    # we're going to unpack the values
    if kwargs: # quick check if there's any.
        print("    special instructions")
        # we're looping through a dictionary
        # which you're going to use the key and value
        # for example if you have
        # {'cheese': 'double', 'pepperoni': 'extra'}
        # for the first iteration
        # key = cheese
        # value = double
        # for the second iteration
        # key = pepperoni
        # value = extra
        for key, value in kwargs.items():
            print(F"      - {key}: {value}")
