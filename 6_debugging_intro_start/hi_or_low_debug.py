import random

# Generate a random integer between a range
random_number = random.randint(1, 100)

# Get the user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)
print(F"user guess {user_guess}")

# Ask the user if they think they are higher or lower than the number
high_low_input = input("Do you think you are higher or lower than the number? (h/l) ")
# breakpoint point
breakpoint()
# "l" allows you to list the area where you currently are
# "ll" shows you the file or a larger area
# you can enter variable names to see what they are
# you can also go to the next line with "n"

result = ""

# Compare the user input to the random number
if user_guess == random_number:
    result = "correct"
elif user_guess > random_number:
    result = "high"
elif user_guess < random_number:
    result = "low"
else: # really if think about it this is unnecessary
    result = "error"

# multiple breakpoints is good
# debugging strategies,check all the paths.
# correct, low, and equal looks good
# breakpoint()

# Is user correct?
if result == "high" and high_low_input == "h":
    # if you're ever curious why something isn't running
    # you can always put a breakpoint() and see
    # the value of the conditional
    print("You are correct it's high!")
elif result == "low" and high_low_input == "l":
    print("You are correct it's low!")
# we could add one more scenario for when it's equal
elif result == "correct":
    print("Technically you're wrong but you guessed the number")
else:
    print('You are wrong and this is rigged...')

# breakpoint()

print(F"the random number was {random_number}")
