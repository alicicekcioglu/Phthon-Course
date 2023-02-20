import random
import art
from replit import clear


def deal_card():
    """Return random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compere_score(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer won"
    elif user_score == 0:
        return "You won"
    elif computer_score > 21:
        return "You won"
    elif user_score > 21:
        return "Computer won"
    elif user_score > computer_score:
        return "You won"
    else:
        return "Computer won"

def play_game():
    print(art.logo)

    computer_card = []
    user_card = []
    is_game_over = True

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer cards: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or sum(user_card) > 21:
            is_game_over = False


        else:
            draw = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw == "y":
                user_card.append(deal_card())
            else:
                is_game_over = False

    while computer_score != 0 and sum(computer_card) < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)


    print(f"Your final hand: {user_card} and your final score: {user_score}")
    print(f"Computer final hand: {computer_card} and computer final score: {computer_score}")
    print(compere_score(user_score,computer_score))



while True:
    again = input("Do you want to play a game of Blacjack? (y/n):")
    if again == "y":
        clear()
        play_game()
    else:
        print("Game finished.")
        break



