from art import logo
import os

continue_bid = True
bidding = {}
def highest_bidder():
    highest_bid = 0
    winner_name = ''
    for player in bidding:
        if int(bidding[player]) > highest_bid:
            highest_bid = int(bidding[player])
            winner_name = player
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")

print(logo)
print("Welcome to the secret auction program.")
while continue_bid:
    name = input("What is your name?: ")
    amount = input("What's your bid?: $")
    bidding[name] = amount
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.: ").lower()
    if other_bidders == 'no':
        highest_bidder()
        continue_bid = False
    else:
        os.system('clear')
