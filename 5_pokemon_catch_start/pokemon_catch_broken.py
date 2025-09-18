# This program is meant to simulate the process of catching a Charizard in the wild.
# Charizard has a catch threshold of 95, meaning a player must score at least 95 when they throw a ball to catch it.
# There are four types of balls, and each add a bonus to the catch chance.
#   - Poke Ball, Bonus: 10
#   - Great Ball, Bonus: 30
#   - Ultra Ball, Bonus: 50
#   - Master Ball, Bonus: 100
# The player chooses a ball, and the bonus is added to the player's roll when they try to catch the Charizard

import random

CHARIZARD_CATCH_CHANCE = 95

POKE_BALL_BONUS = 10
# fixed the equal operator to assingment.
GREAT_BALL_BONUS = 30
ULTRA_BALL_BONUS = 50
MASTER_BALL_BONUS = 100

print("You encountered a wild Charizard!")

# assigning a print looks weird.
# fix let's change the print to an input
# input needs to be converted to an int
ball_choice = int(input("""
    Which ball would you like to throw (enter the number):
    1: Poke Ball
    2: Great Ball
    3: Ultra Ball
    4: Master Ball
"""))

# let's take a look at the docs.
# randint is a function and let's try it.
roll = random.randint(1, 100)
# we can test all cases by just override this random piece.
# debugging
# make sure that our does what we expect.
roll = 1

if ball_choice == 1:
    # fixed indentation
    print("Throwing Poke Ball...")
    # this is equivalent to roll = roll + 1
    roll += POKE_BALL_BONUS
elif ball_choice == 2:
    print("Throwing Great Ball...")
    roll += GREAT_BALL_BONUS
elif ball_choice == 3:
    print("Throwing Ultra Ball...")
    roll -= ULTRA_BALL_BONUS
else:
    print("Throwing Master Ball...")
    roll += MASTER_BALL_BONUS

if roll >= CHARIZARD_CATCH_CHANCE:
    print("Congratulations! You caught Charizard.")
else:
    print("Charizard escaped!")