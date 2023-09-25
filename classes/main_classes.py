# Importing Libraries
import random

# Creating Classes

# Class is generate game
class generate_game:
    def __init__(self, name, difficulty, upper, lower):
        self.name = name
        self.difficulty = difficulty        
        self.upper = upper
        self.lower = lower

    def generate_winning_number(self):
        return random.randrange(self.lower, self.upper)

    def check_if_win(self, win_no, select_no):
        if win_no == select_no:
            print(f'Congratulations, you have correctly guessed the winning number!')
            win = True
        elif select_no > win_no:
            print(f'{select_no} is not the winning number. This guess was too high.')
            win = False
        else:
            print(f'{select_no} is not the winning number. This guess was too low.')
            win = False
        return win
    
    def check_if_too_high(self, win_no, select_no):
        if select_no > win_no:
            too_high = True
        else:
            too_high = False
        return too_high