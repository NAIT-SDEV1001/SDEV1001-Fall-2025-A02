
# create a function called `translate_number_to_choice`
def translate_number_to_choice(choice_number):
    # with the choice_number as an arguments
    # which will return
    # "scissor" for choice_number 0,
    if choice_number == 0:
        return "scissor"
    # "rock" for choice_number 1
    if choice_number == 1:
        return "rock"
    # "paper" for choice_number 2
    if choice_number == 2:
        return "paper"
    # and the number otherwise.

# we're going to create an is_winner funciton to check if a user is a winner or not.

def is_winner(player_one, player_two):
    ''' return a boolean that checks if player one is the winner '''
    # note we're just doing the condition here.
    return ((player_one == "paper" and player_two == "rock")
        or (player_one == "rock" and player_two == "scissors")
        or  (player_one == "scissors" and player_two == "paper"))

def get_game_result(
    user_input,
    computer_input
):
    ''' This is going to the result and print if the
    user has won.
    '''
    # use our function above
    # use this function to get the user input string an
    # and the computer string.
    user_choice = translate_number_to_choice(user_input)
    computer_choice = translate_number_to_choice(computer_input)
    # print("user_choice", user_choice)
    # print("computer_choice", computer_choice)
    # to get the game result
    # three scenarios
    # tie if both choices are the same the it's a tie
    if user_choice == computer_choice:
        print(F"this is a tie both chose {user_choice}")

    # breakpoint()
    # user wins
    # we're converting the following to a function
    # if ((user_choice == "paper" and computer_choice == "rock")
    #     or (user_choice == "rock" and computer_choice == "scissors")
    #     or  (user_choice == "scissors" and computer_choice == "paper")):
    # to
    # if is_winner(user_choice, computer_choice):

    elif is_winner(user_choice, computer_choice):
        print(F"User wins '{user_choice}' beats '{computer_choice}'")

    # computer wins
    # we're going to do the same here conver
    # if ((computer_choice == "paper" and user_choice == "rock")
    #     or (computer_choice == "rock" and user_choice == "scissors")
    #     or  (computer_choice == "scissors" and user_choice == "paper")):
    # to
    # if is_winner(computer_choice, user_choice):
    elif is_winner(computer_choice, user_choice):
        print(f"Computer wins '{computer_choice}' beats '{user_choice}'")
    else:
        print("Error in processing")

# Note:
# as a general smaller functions with good names lead to more readable code.



