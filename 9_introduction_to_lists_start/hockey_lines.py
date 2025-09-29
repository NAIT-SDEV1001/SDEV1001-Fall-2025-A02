# let's do a new example that will have the lines

print("Oilers line checker")
# we're going have arrays of arrays
oilers_forward_lines = [
    ["Draisaitl", "Mcdavid", "Frederic"],
    ["Howard", "Nugent-Hopkins", "Tomasek"],
    ["Mangiapane", "Henrique", "Savoie"],
    ["Podkolzin", "Philp", "Kapanen"]
]

# in here we're going make a checker that checks to see if a player is on a certain line
# 1. get the input of the user of what line they want to check
line_number = int(input("What line do you want to check (1-4)? "))
line_index = line_number - 1
# that is because indices start at 0
# 2. the player name they want to check
player_name = input("Which player do you want to check? (caps first letter)")

# 3. display if the user is on that line or not.
if player_name in oilers_forward_lines[line_index]:
    print(F"{player_name} is on line {line_number}")
else:
    print(F"{player_name} is not on that line")

