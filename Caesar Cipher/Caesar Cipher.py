import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "•", 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "•"]

print(art.logo)

def encrypt(start_text, shift_amount, cipher_direction):
        end_text = " "
        if cipher_direction == "decode":
            shift_amount *= -1
        for i in start_text:
            position = alphabet.index(i)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        print(f"The {cipher_direction}d text is {end_text}")

again = False
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 2 + 1

    encrypt(start_text=text, shift_amount=shift, cipher_direction=direction)
    x = input("Again?")
    if x == "y":
        again = True
    else:
        break
