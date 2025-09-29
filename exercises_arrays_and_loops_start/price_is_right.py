# import the random module
import random

print("Welcome to the Price is Right! Guess the price of this coffee")

random_prices = [
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
]

guess = int(input("Guess the price of the item: "))
# remember to use breakpoint in your code it's handy!
# breakpoint()
# we're going to use the in operator
if guess in random_prices:
    print("You win!")
else:
    print("You lose!")

print(F"The prices were {random_prices}")