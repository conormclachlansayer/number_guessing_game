# Main script for Number Guessing Game - using classes in classes folder
## Import Classes and Libraries
from classes.main_classes import generate_game
import random


# Start writing game
# Welcome statement
print("Welcome to this Number Guessing Game.")

# First ask user for their name:
name = input("To get started, please tell me your first name.\n")

# Start game
running = True

while running:
    # Next ask for difficulty
    print(f'Welcome {name}! Great to have you here. Please select your desired difficulty level.')
    difficulty = int(input(f'1) Easy (guessing a number between 0 and 10, inclusive)\n2) Medium (guessing a number between 0 and 40, inclusive)\n3) Hard (guessing a number between 0 and 80, inclusive)\n4) Custom - select your own upper and lower bounds!\n'))

    # Select upper and lower bounds
    if difficulty == 1:
        upper = 10
        lower = 0
    if difficulty == 2:
        upper = 40
        lower = 0
    if difficulty == 3:
        upper = 80
        lower = 0
    if difficulty == 4:
        upper = int(input("Please input your desired upper limit (inclusive):\n"))
        lower = int(input("Please input your desired lower limit (inclusive):\n"))

    # Generate game
    new_game = generate_game(name=name, difficulty=difficulty, upper=upper, lower=lower)

    # Generate winning number
    winning_number = int(new_game.generate_winning_number())

    # Reset to 4 guesses, and range to upper and lower
    remaining_guesses = 4
    upper_limit = new_game.upper
    lower_limit = new_game.lower 

    while remaining_guesses > 0:

        # User guesses
        if remaining_guesses == 1:
            print(f'You have {remaining_guesses} guess remaining.\n')
        else:
            print(f'You have {remaining_guesses} guesses remaining.\n')

        guess = int(input(f'Please guess a number between {lower_limit} and {upper_limit}:\n'))

        # Check if win and if guess too high
        win = new_game.check_if_win(winning_number, guess)
        too_high = new_game.check_if_too_high(winning_number, guess)

        # End game if win, continue if not
        if win and not too_high:
            remaining_guesses = 0
        elif too_high:
            upper_limit = guess
            remaining_guesses -= 1
        elif not too_high:
            lower_limit = guess
            remaining_guesses -= 1

        if remaining_guesses == 0 and not win:
            print(f'\nOh no you have run out of guesses! The winning number was {winning_number}. Better luck next time!\n')

    play_again = int(input(f'Thank you for playing this guessing game. I hope you had fun! Would you like to play again? Please select from one of the following:\n1) Yes\n2) No\n'))

    if play_again==1:
        continue
    else: 
        running = False


    



