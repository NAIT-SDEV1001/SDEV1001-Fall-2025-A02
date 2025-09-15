# we're going to import a module built in to python
# that is called random
import random
# if you want to read the docs: https://docs.python.org/3/library/random.html#random.randint

# we're going to use randint to create a number from
# Note: variables can't have the same name as the module.
random_number = random.randint(1, 100)

# for debugging purposes this is really good to have to test all conditions.
print(f"random number is {random_number}")

# what I want to do
# 1. get the user guess
user_guess = int(input("What number do you want to guess? "))
# can I compare an input to a number, but we have to convert it to a number first
# compare the input to the random number
# if it's exact I want you to print out: you guessed the number
if user_guess == random_number:
    print("you guessed the number")
    # if it's lower I want you to print out: your guess is lower than (random number)
elif user_guess < random_number:
    print(f"your guess is lower than {random_number}")
    # if it's higher I want you to print out: your guess is higher than (random number)
elif user_guess > random_number:
    print(f"your guess is greater than {random_number}")

