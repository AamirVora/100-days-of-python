# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

bidders_list = {}

more_Bidders = True
while more_Bidders:
    bidder_name = input("Enter you Name: ").lower()
    bidder_bid = int(input("Enter your Bid: "))
    more_bidders = input("Do you have more bidders? (y/n): ").lower()

    if more_bidders == "n":
        more_Bidders = False
    elif more_bidders == "y":
        print("\n" * 100)
    else:
        more_Bidders = False

    bidders_list[bidder_name] = bidder_bid

highest_bid = max(bidders_list.values())
bidder_name = ""

for bidder in bidders_list:
    if bidders_list[bidder] == highest_bid:
        bidder_name = bidder
print(f"The highest bidder is {bidder_name} with ${highest_bid}")


