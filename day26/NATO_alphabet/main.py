
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

new_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
list = [new_dictionary[letter] for letter in word]

print(list)