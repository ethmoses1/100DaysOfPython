############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21,
# then the computer loses. If none of the above, then the player with the highest score wins.

from art import logo
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def cal_score(cards_dealt):
    score = 0
    for card in cards_dealt:
        score += card
    return score
def deal_card(player):
    card = random.choice(cards)
    if player == "computer":
        computer_cards.append(card)
    else:
        player_cards.append(card)
continue_playing = True


def check_if_Player_lost(player_cards, computer_cards):
    if 11 in player_cards and cal_score(player_cards) > 21:
        index = player_cards.index(11)
        player_cards[index] = 1
    if cal_score(player_cards) > 21:
        deal_card("computer")
        print(f"        Your cards: {player_cards}, current score: {cal_score(player_cards)}")
        print(f"        Computer's first card: {computer_cards[0]}")
        print(f"        Your final hand {player_cards}, final score: {cal_score(player_cards)}")
        print(f"        Computer's final hand: {computer_cards}, final score: {cal_score(computer_cards)}")
        print("You went over. You lose 😭")
        return True
    else:
        return False
def check_if_computer_won():
    print(f"        Your final hand {player_cards}, final score: {cal_score(player_cards)}")
    print(f"        Computer's final hand: {computer_cards}, final score: {cal_score(computer_cards)}")
    if cal_score(player_cards) <= 21 and cal_score(player_cards) > cal_score(computer_cards):
        print("You Win😁")
    elif cal_score(player_cards) < cal_score(computer_cards):
        print("You lose 😤")
    elif cal_score(player_cards) == cal_score(computer_cards):
        print("Draw")
play_blackjack_game = True
while play_blackjack_game:
    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_blackjack == 'y':
        end_game = False
        while end_game == False:
            print(f"        Your cards: {player_cards}, current score: {cal_score(player_cards)}")
            print(f"        Computer's first card: {computer_cards[0]}")
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == 'y':
                deal_card("player")
                if check_if_Player_lost(player_cards, computer_cards):
                    end_game = True
            elif get_another_card == 'n':
                deal_card("computer")
                check_if_computer_won()
                end_game = True





