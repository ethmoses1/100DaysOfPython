# Instructions
# Make a rock, paper, scissors game.
#
# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.
#
# Start the game by asking the player:
#
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
#
# From there you will need to figure out:
#
# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_list = ["Rock", "Paper", "Scissors"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
user_choice = game_list[user_input]
# print(user_choice)

random_number = random.randint(0, 2)
computer_choice = game_list[random_number]

if user_choice == "Rock" and computer_choice == "Scissors":
    print(f"You win {rock}\n bits \n{scissors}")
elif user_choice == "Rock" and computer_choice == "Paper":
    print(f"You lose {paper}\n bits \n{rock}")
elif user_choice == "Scissors" and computer_choice == "Rock":
    print(f"You lose {rock}\n bits \n{scissors}")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print(f"You win {scissors}\n bits \n{paper}")
elif user_choice == "Paper" and computer_choice == "Scissors":
    print(f"You lose {scissors}\n bits \n{paper}")
elif user_choice == "Paper" and computer_choice == "Rock":
    print(f"You win {paper}\n bits \n{rock}")

