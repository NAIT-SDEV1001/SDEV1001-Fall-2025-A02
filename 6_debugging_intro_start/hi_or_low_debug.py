import random

# Generate a random integer between a range
random_number = random.randint(1, 100)

# Get the user input
user_input = input("Guess a number between 1 and 100: ")
user_guess = int(user_input)
print(F"user guess {user_guess}")

# Ask the user if they think they are higher or lower than the number
high_low_input = input("Do you think you are higher or lower than the number? (h/l) ")

result = ""

# Compare the user input to the random number
if user_guess == random_number:
    result = "correct"
elif user_guess > random_number:
    result = "high"
elif user_guess < random_number:
    result = "low"
else: 
    result = "error"

# Is user correct?
if result == "high" and high_low_input == "h":
    print("You are correct it's high!")
elif result == "low" and high_low_input == "l":
    print("You are correct it's low!")
else: 
    print('You are wrong and this is rigged...')

print(F"the random number was {random_number}")