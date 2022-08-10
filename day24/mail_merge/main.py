#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()

list_of_names = []
with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.read()
    list_of_names = names.split("\n")

for name in list_of_names:
    new_letter = letter_contents.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as ready_letter:
        ready_letter.write(new_letter)
