# #Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#
#Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#
#
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = [];
# for letter in letters:
#     random = random.randint(1, 26)

for letter in range(1, nr_letters+1):
    rand = random.randint(1, 26)
    password.append(letters[rand-1])
for symbol in range(1, nr_symbols+1):
    rand = random.randint(1, 9)
    password.append(symbols[rand-1])
for number in range(1, nr_numbers+1):
    rand = random.randint(1, 10)
    password.append(numbers[rand-1])

random.shuffle(password)
new_password = ''.join(password)

print(new_password)
# print(nr_letters, nr_symbols, nr_numbers);
