rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random


while True:
    possible_choices = [paper, scissors, rock]
    computer_choice = random.choice(possible_choices)
    x = int(input("1 = paper\n2 = scissors\n3 = rock\n"))
    if x > 3 or x < 1:
        print("You typed an invalid number, you lose!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            continue
        else:
            print("You are boring :/\n")
        break

    else:
        player_choice = possible_choices[x-1]

        if player_choice == computer_choice:
            print(f"Both players selected same thing! {player_choice}"
                  f"\nDraw!\n...")

        elif player_choice == paper:
            if computer_choice == scissors:
                print(f"Computer selected {computer_choice}\n"
                      f"You selected{player_choice}\n"
                      f"Computer win")
            else:
                print(f"Computer selected {computer_choice}\n"
                      f"You selected{player_choice}\n"
                      f"You win")


        elif player_choice == scissors:
            if computer_choice == rock:
                print(f"Computer selected {computer_choice}\n"
                      f"You selected{player_choice}\n"
                      f"Computer win")
            else:
                print(f"Computer selected {computer_choice}\n"
                      f"You selected{player_choice}\n"
                      f"You win")


        elif player_choice == rock:
            if computer_choice == paper:
                print(f"Computer selected {computer_choice}\n"
                      f"You selected{player_choice}\n"
                      f"Computer win")
            else:
                print(f"Computer selected {computer_choice}\n"
                      f"You selected{player_choice}\n"
                      f"You win")


        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            continue
        else:
            print("You are boring :/\n")
        break

