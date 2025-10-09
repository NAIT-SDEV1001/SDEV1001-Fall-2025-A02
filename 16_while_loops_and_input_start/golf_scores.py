print("Golf Score Calculator")

# I want you to keep track of a couple of things
# the amount of scores entered
count = 0
# the total score that the user entered
total_score = 0
# use a while loop to check if the user has entered
# we're going to use a flag to see if the user
# is still entering scores
entering_scores = True
# this will be the condition that we'll turn to false
# the enters "quit"
while entering_scores:
    user_input = input("""
        What was your most recent score (enter 'quit' to stop)
    """) # you can use """ for a multiline string
    # handle the case where user quits first
    # 2. if they wrote "quit" which exit the loop
    if user_input == "quit":
        entering_scores = False
        continue
        # this is different than break but has some similarities
        # if the line "conintue" is hit it will immediately go
        # to the next iteration
    # 1. a score (which you keep track of)
    total_score += int(user_input)
    count += 1


# at then end print the average score.
average_score = total_score/count

print(F"your average score is {average_score}")
