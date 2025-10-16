import random
# heads will be 0 and tails will be 1
# I want you to move this in to get_coin_flip
# function, this function is going to take
# no arguments (no parameers)

# I want you to create a second function
# called get_user_guess which will continuously
# ask for "h" or "t"

def get_coin_flip():
    """Returns h or t based on the random coinflip""" # just a long string
    random_number = random.randint(0, 1)
    # i'm going to say that 0 is h
    # 1 t
    if random_number == 0:
        # return early
        return "h"
        # once the above line is it
        # nothing else in the function will
        # execute
    # Option 1:
    # elif random_number == 1:
    #     return "t"
    # Option 2:
    # since we have two options here
    # can just return this because it either
    # returns above or executes this.
    return "t"

def is_coin_flip_result_heads(result):
    return result == "h"

def get_user_guess():
    # we can use similar techniques
    while True:
        guess = input("please enter a guess (h/t): ")
        if guess == "h" or guess == "t":
            return guess
            # this will also break out of the loop because it's
            # in the function
        print("sorry didn't get that.")

def is_correct_guess(guess, result):
    return guess == result

def main():
    print("The ultimate coin flipper")
    # call your functions in here
    result = get_coin_flip()

    guess = get_user_guess()

    if is_correct_guess(guess, result):
        print("you guessed correctly")
    else:
        print("you're wrong")

    if is_coin_flip_result_heads(result):
        print('you flipped heads')

if __name__ == "__main__":
    main()

