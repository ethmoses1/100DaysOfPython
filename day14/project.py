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
    if score > 0: print(f"You're right! Current score: {score}")
    print(f"Compare A: {p1['name']}, a {p1['description']}, from {p1['country']}")
    print(vs)
    print(f"Against B: {p2['name']}, a {p2['description']}, from {p2['country']}")


while continue_palying:
    os.system("clear")
    print(logo)
    
    display_opitions(opition_a,opition_b)
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if opition_a['follower_count'] > opition_b['follower_count'] and user_choice == "A":
        score +=1
        opition_a = opition_b
        opition_b = generate_random_individuals()
    elif opition_b['follower_count'] > opition_a['follower_count'] and user_choice == "B":
        score +=1
        opition_a = opition_b
        opition_b = generate_random_individuals()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_palying = False
