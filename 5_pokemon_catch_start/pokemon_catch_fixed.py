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
GREAT_BALL_BONUS = 30
ULTRA_BALL_BONUS = 50
MASTER_BALL_BONUS = 100

print("You encountered a wild Charizard!")

ball_choice = input("""
    Which ball would you like to throw:
    1: Poke Ball
    2: Great Ball
    3: Ultra Ball
    4: Master Ball1
                    
""")

ball_choice = int(ball_choice)

roll = random.randint(1, 100)

if ball_choice == 1:
    print("Throwing Poke Ball...")
    roll += POKE_BALL_BONUS
elif ball_choice == 2:
    print("Throwing Great Ball...")
    roll += GREAT_BALL_BONUS
elif ball_choice == 3:
    print("Throwing Ultra Ball...")
    roll += ULTRA_BALL_BONUS
else:
    print("Throwing Master Ball...")
    roll += MASTER_BALL_BONUS

if roll >= CHARIZARD_CATCH_CHANCE:
    print("Congratulations! You caught Charizard.")
else:
    print("Charizard escaped!")

# Error 1:
#   Type: NameError
#   Line: 14
#   Why did it happen: == was used when creating the constant
# Error 2:
#   Type: Wrong function used
#   Line: 20
#   Why did it happen: the "print" function was used to get the value from the user. Should have been an "input"
# Error 3:
#   Type: AttributeError
#   Line: 28
#   Why did it happen: the random function was spelled incorrectly, should be "randint", not "randoint"
# Error 4:
#   Type: Master ball always thrown
#   Line: 30, 33, 36
#   Why did it happen: The if/else chain is checking the value as an integer, we didn't cast the input as a int
# Error 5:
#   Type: Indentation Error
#   Line: 31
#   Why did it happen: The print() statement is indented incorrectly.
# Error 6:
#   Type: Ultraball is lowering chance of catching
#   Line: 38
#   Why did it happen: The -= operator is being used, so it is subtracting 50, not adding it.