import random
import art

print(art.logo)

def game():

    def computer_guess():
        numbers = range(1, 100)
        a = random.choice(numbers)
        return a

    computer_guess()
    number = computer_guess()
    print(number)

    lives = input("Do you want to play hard mode or easy mode?:\n")
    if lives == "easy":
        lives = 10
    else:
        lives = 5

    while lives >= 0:
        if lives == 0:
            print(f"You out of lives. Computer guess was {number}")
            break

        player_guess = int(input("Guess a number between 1 and 100:\n"))
        if number == player_guess:
            print("You win.")
            print(f"Computer guess was {number}")

        elif number > player_guess:
            print("Too low")
            lives -= 1
        else:
            print("Too high")
            lives -= 1


game()