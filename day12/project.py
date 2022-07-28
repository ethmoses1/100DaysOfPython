#Project
from art import logo
import random
print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5
random_guess_number = random.randint(1, 100)
def deduct_life(level):
    if level == 'easy':
        return EASY_LEVEL-1
    else:
        return  HARD_LEVEL- 1
def check_life(level):

    if level == 'easy':
        if EASY_LEVEL > 0:
            return True
        else:
            return False
    else:
        if HARD_LEVEL > 0:
            return True
        else:
            return False

def check_player_inpout():
    player_number = int(input("Make a guess: "))
    if player_number == random_guess_number:
        return 1
    elif player_number > random_guess_number:
        print('Too High')
    elif player_number < random_guess_number:
        print('Too Low')

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

continue_guess_game = True

while continue_guess_game:
    if difficulty == 'easy':
        if check_life('easy'):
            print(f"You have {EASY_LEVEL} attempts remaining to guess the number.")
            if check_player_inpout() == 1:
                print(f"You got it! The answer was {random_guess_number}.")
                continue_guess_game = False
            else:
                EASY_LEVEL = deduct_life('hard')
        else:
            print("You've run out of guesses, you lose.")
            continue_guess_game = False
    else:
        if check_life('hard'):
            print(f"You have {HARD_LEVEL} attempts remaining to guess the number.")
            if check_player_inpout() == 1:
                print(f"You got it! The answer was {random_guess_number}.")
                continue_guess_game = False
            else:
                HARD_LEVEL = deduct_life('hard')
        else:
            print("You've run out of guesses, you lose.")
            continue_guess_game = False

