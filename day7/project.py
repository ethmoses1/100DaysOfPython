#Build a Hangman Game

#Step 1
import random
import hangman_words
import hangman_art
stages = hangman_art.stages
logo = hangman_art.logo
word_list = hangman_words.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word  = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower();
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for char in chosen_word:
#     if guess == char:
#         print("yes")
#     else:
#         print("No")


#Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# guess = input("Guess a letter: ").lower()

display = []

for char in chosen_word:
    display.append("_")

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# position = 0
# for char in chosen_word:
#     if char == guess:
#         display[position] = char
#     position = position+1

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# word = ' '.join(display);
#
# print(word)



#Step 3




#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     position = 0
#     for char in chosen_word:
#         if char == guess:
#             display[position] = char
#         position = position + 1
#     if "_" in display:
#         word = ' '.join(display);
#         print(word)
#     else:
#         word = ''.join(display);
#         print("")
#         print("     You win!🎉")
#         print(f"The word was {word}.")


#Step 4



#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

#TODO-2: - If guess is not a letter in the chosen_word,
play_game = True
print(logo)
print(' '.join(display))
while play_game:
    guess = input("Guess a letter: ").lower()
    position = 0
    char_exists = False
    for char in chosen_word:
        if char == guess:
            display[position] = char
            char_exists = True;
        position = position + 1
    if "_" in display:
        word = ' '.join(display);
        print(word)
        if char_exists == False:
            lives = lives-1
        print(stages[lives])
    else:
        word = ''.join(display);
        print("")
        print("     You win!🎉")
        print(f"The word was {word}.")
    if "_" not in display or lives == 0:
        print("     You lose!😢")
        print(f"The word was {chosen_word}.")
        play_again = input("Play again (y/n): ").lower()
        if play_again == "y":
            lives = 6
        else:
            play_game = False


    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.