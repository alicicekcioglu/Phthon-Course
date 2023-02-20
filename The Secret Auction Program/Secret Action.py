from replit import clear
from Art import logo

print(logo)

def find_highest_bidder(bidding_record):
    highest= 0
    winner = ""
    for i in bidding_record:
        value = bidding_record[i]
        if value > highest:
            highest = value
            winner = i
    print(f"{winner} is the winner!")


def ask_name_and_bid():
    bidding_finish = False
    while not bidding_finish:

        name = input("Name: ")
        bid = float(input("Bid: "))
        bids = {name: bid}

        user = input("Anyone else? (y/n): ")
        if user == "n":
            bidding_finish = True
            find_highest_bidder(bids)
        else:
            clear()


ask_name_and_bid()
