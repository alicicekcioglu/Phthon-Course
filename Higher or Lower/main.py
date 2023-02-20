import art
import game_data
import random

print(art.logo)

b = random.choice(game_data.data)
def get_input():
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']} ")
    print(art.vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']} \n\n")


score = 0

while True:
    a = b
    b = random.choice(game_data.data)

    get_input()
    choose = input("Who have more followers? Type 'A' or 'B': ")

    if a == b:
        a = random.choice(game_data.data)
        b = random.choice(game_data.data)

    elif a["follower_count"] > b["follower_count"] and choose == "A":
        score += 1


    elif b["follower_count"] > a["follower_count"] and choose == "B":
        score += 1

    else:
        print(f"Ooops! Wrong answer.\nYour score is {score}")
        c = input("Do you want to play again? (Y/N): ")
        if c == "Y":
            continue
        else:
            break
