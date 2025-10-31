import random
# heads will be 0 and tails will be 1
random_number = random.randint(0, 1)

user_guess = input("Guess the coin flip! Enter heads or tails (h/t): ")

if random_number == 0:
    print("The coin flip was: heads")
elif random_number == 1:
    print("The coin flip was: tails")

if ((random_number == 0 and user_guess == "h")
    or (random_number == 1 and user_guess == "t")):
    print("you guessed correct!")
else:
    print("you guessed wrong!")
