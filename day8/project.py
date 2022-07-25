import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
play_game = True;
while play_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    def encrypt(plain_text,shift_amount, direction ):
        encrypted_word = ''
        position = 0;
        for char in plain_text:
            if char not in alphabet:
                encrypted_word += char
            else:
                index = alphabet.index(char)
                if direction == "encode":
                    position = index + shift_amount
                elif direction == "decode":
                    position = index - shift_amount
                encrypted_word += alphabet[position]
        print(f"The {direction}d text is {encrypted_word}")
    encrypt(text,shift,direction)
    restart = input("Restart cipher? (y/n): ")
    if restart == 'n':
        play_game = False
