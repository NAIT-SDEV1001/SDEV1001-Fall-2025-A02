ONE_ACRE_OF_LAND_IN_SQFT = 43560 # we this
# 1 get the user input
acre_amount_text = input("Acre to Square foot converter. How many acres do you have?")
print(F"You have {acre_amount_text} acres")
# 2 convert it to an int
acre_amount = int(acre_amount_text)
# 3 a little maths.
square_feet = ONE_ACRE_OF_LAND_IN_SQFT*acre_amount

print(F"Which is equal to: {square_feet} square feet")