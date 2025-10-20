
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

# use this function to get the user input string an
# and the computer string.


def get_game_result(
    user_input,
    computer_input
):
    ''' This is going to the result and print if the
    user has won.
    '''
    # use our function above
    user_choice = translate_number_to_choice(user_input)
    computer_choice = translate_number_to_choice(computer_input)
    print("user_choice", user_choice)
    print("computer_choice", computer_choice)

    # to get the game result
    # three scenarios
    # tie if both results
    # user wins
    # computer wins





