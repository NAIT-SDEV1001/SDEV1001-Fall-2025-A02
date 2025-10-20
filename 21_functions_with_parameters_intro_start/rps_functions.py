
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
    print("user_choice", user_choice)
    print("computer_choice", computer_choice)
    breakpoint()
    # to get the game result
    # three scenarios
    # tie if both choices are the same the it's a tie
    if user_choice == computer_choice:
        print(F"this is a tie both chose {user_choice}")

    # user wins
    # computer wins





