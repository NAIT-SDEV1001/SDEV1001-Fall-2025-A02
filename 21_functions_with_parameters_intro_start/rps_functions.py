
def translate_number_to_choice(choice_number):
    if choice_number == 0:
        return "scissor"
    if choice_number == 1:
        return "rock"
    if choice_number == 2:
        return "paper"

def is_winner(player_one, player_two):
    ''' return a boolean that checks if player one is the winner '''
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
    user_choice = translate_number_to_choice(user_input)
    computer_choice = translate_number_to_choice(computer_input)
    if user_choice == computer_choice:
        print(F"this is a tie both chose {user_choice}")


    elif is_winner(user_choice, computer_choice):
        print(F"User wins '{user_choice}' beats '{computer_choice}'")

    elif is_winner(computer_choice, user_choice):
        print(f"Computer wins '{computer_choice}' beats '{user_choice}'")
    else:
        print("Error in processing")



