"""
Author: ng ka ho (32360770)
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.
"""

import random

def random_number(min, max):
    """ 
    random the number between min and max
	Parameters
	----------
	min: int
		the max number
    max: int
        the min number

	Returns
	----------
	random : int
        the random number between min and max
	"""
    return random.randint(min, max)

def ask_user_to_guess(message):
    """ 
    ask user to input by keyboard
	----------
	message: string
		the message which print out to user

	Returns
	----------
	guess_number : string
        the user input
	"""
    guess_number = input(message)
    return guess_number

def check_bingo(guess_number, bingo_number):
    """ 
    check the user guess result
	----------
	guess_number: int
		the number which is input by user
    bingo_number : int
        the target number

	Returns
	----------
	result : int
        1 = bingo, 2 = higher, 3 = lower
	"""
    if guess_number == bingo_number:
        return 1
    elif guess_number > bingo_number:
        return 2
    elif guess_number < bingo_number:
        return 3

if __name__ == "__main__":

    """ 
    main logic to handle the game
	"""
    start = 1
    end = 100 
    bingo = False
    # generate the target number
    bingo_number = random_number(start, end)

    # check if not bingo, keep continue
    while not bingo:
        guess_number = 0
        # ask user to input a int, if not int or higher or lower than the number, keep asking uer to input
        while guess_number == 0 or guess_number < start or guess_number > end:
            guess_number = ask_user_to_guess(f"Please guess the number between {start} and {end}: ")
            # check whether is int
            if not guess_number.isnumeric():
                print("Please insert number")
                # reset the number
                guess_number = 0
                continue
            # cast to int
            guess_number = int(guess_number)
            # checking is 0 and higher or lower than the range
            if guess_number == 0:
                print("You cannot input 0")
            elif guess_number < start:
                print(f"You cannot input a number less than {start}")

            elif guess_number > end:
                print(f"You cannot input a number bigger than {end}")

        # check the answer
        answer = check_bingo(guess_number, bingo_number)

        # show the result, if not bingo, update the range
        if answer == 1:
            bingo = True
            print("Congrats!!!! Bingo!!!")
        elif answer == 2:
            print("it is higher than the target number")
            end = guess_number
        elif answer == 3:
            print("it is lower than the target number")
            start = guess_number