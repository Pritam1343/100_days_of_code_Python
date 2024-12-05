import os

auction_data = {}
cont = True
temp_winner = 0

def bidder_entry(bid, name):
    auction_data[bid] = name
    global temp_winner
    if bid > temp_winner:
        temp_winner = bid
    return temp_winner

def clear_terminal():
    print("\n" * 500)


while cont:
    clear_terminal()
    print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
    ''')
    name = input("What is your name ?\n")
    bid = int(input("What's your bid? $\n"))
    bidder_entry(bid,name)
    is_continue = input("Are there any other Bidders? Type 'yes' or 'no'\n").lower()

    if is_continue == "yes":
        clear_terminal()
    elif is_continue == "no":
        clear_terminal()
        print("Good Bye ..")
        cont = False
    else:
        clear_terminal()
        print("You have not entered 'yes'/'no' !!!")

winner_name = auction_data[bidder_entry(bid, name)]
print(f"The winner is {winner_name} with a bid of ${bidder_entry(bid, name)}")

#for debugging
print(auction_data)
