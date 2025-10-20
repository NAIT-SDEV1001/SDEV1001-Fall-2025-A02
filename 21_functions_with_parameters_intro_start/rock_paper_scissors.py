import random

from rps_functions import get_game_result

if __name__ == "__main__":
    user_input =  int(input("Scissor (0), rock (1), paper (2): "))
    computer_input = random.randint(0, 2)

    get_game_result(user_input, computer_input)