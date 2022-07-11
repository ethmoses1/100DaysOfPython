# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
# e.g. When you hit run, this is what should happen:
#
# https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4
#
# Hint
# Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.
# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:
#
# https://repl.it/@appbrewery/day-3-4-test-your-code
#
# This repl includes my testing code that will check if your code meets this assignment's objectives.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small = 15
medium = 20
large = 25
pepperoni_small = 2
pepperoni_medium_and_large = 3
cheese = 1

total = 0
if size == "S":
    total += small
    if(add_pepperoni == "Y"):
        total+=pepperoni_small
    if extra_cheese == "Y":
        total+=cheese
    print(f"Your final bill is: ${total}")

elif size == "M":
    total += medium
    if (add_pepperoni == "Y"):
        total += pepperoni_medium_and_large
    if extra_cheese == "Y":
        total += cheese
    print(f"Your final bill is: ${total}")
else:
    total += large
    if (add_pepperoni == "Y"):
        total += pepperoni_medium_and_large
    if extra_cheese == "Y":
        total += cheese
    print(f"Your final bill is: ${total}")

