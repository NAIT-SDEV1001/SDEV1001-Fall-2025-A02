print("Golf Score Calculator")
count = 0
total_score = 0
# removed active variable

while True:
    user_input = input("What was your most recent golf score? (enter 'quit' to stop) ")
    if user_input == 'quit': # quit if the user enters 'quit'
        break
    else: # add the score to the total and increment the count
        total_score += int(user_input)
        count += 1

# use the average.

average = total_score / count
print(f"Your average golf score is {average}.")

