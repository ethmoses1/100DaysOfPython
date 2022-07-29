#Higher Lower Game
from art import logo,vs
from game_data import data
from random import choice
import os

opition_a = choice(data)
opition_b = choice(data)
score = 0
continue_palying = True
def generate_random_individuals():
    random = choice(data)
    if random['name'] != opition_a['name']:
        return random

def display_opitions(p1, p2):
    print(f"Compare A: {p1['name']}, a {p1['description']}, from {p1['country']}")
    print(vs)
    print(f"Against B: {p2['name']}, a {p2['description']}, from {p2['country']}")

def highest_individual():
    if opition_a['follower_count'] > opition_b['follower_count']:
        return 'A'
    elif opition_b['follower_count'] > opition_a['follower_count']:
        return 'B'
def check_win(user_choice):
    global score
    if user_choice == highest_individual():
        return 1
    else:
        return 0

while continue_palying:
    print(logo)
    display_opitions(opition_a,opition_b)
    play_game = True
    while play_game:
        user_choice = input("Who has more followers? Type 'A' or 'B': ")
        if check_win(user_choice) == 1:
            os.system('clear')
            score +=1
            print(logo)
            print(f"You're right! Current score: {score}")
            opition_a = opition_b
            opition_b = generate_random_individuals()
            display_opitions(opition_a,opition_b)
        else:
            os.system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            play_game = False
    continue_palying = False
    