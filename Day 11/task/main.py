# My CODE
# import random
# from art import logo
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# play_game = input("Do you want to play a game of Blackjack? y/n ").lower()
#
# if play_game == "y":
#     print(logo)
#
# player_cards = random.sample(cards, 2)
# dealer_cards = random.sample(cards,1)
#
# current_player_score = sum(player_cards)
# dealer_score = sum(dealer_cards)
#
#
# print(f"Your Cards: {player_cards}")
# print(f"Your current Score : {current_player_score}")
#
# print(f"Computers first card : {dealer_cards}")
# print(f"Computer's current Score : {dealer_score}")
#
# another_card = input("Type 'y' to get another card or type 'n' to pass ").lower()
#
# hit = True
#
# new_dealer_score = dealer_score
# new_dealer_deck = dealer_cards
# new_player_deck = player_cards
# new_player_score = current_player_score
#
# while new_dealer_score < 17:
#     choose_new_card = random.choice(cards)
#     new_dealer_score += choose_new_card
#     new_dealer_deck += [choose_new_card]
#
#
# if another_card == "n":
#     print(f"Your final hand : {player_cards}")
#     print(f"final score : {current_player_score}")
#     print(f"Computer final hand : {new_dealer_deck}")
#     print(f"Computer final score : {new_dealer_score}")
#
# elif another_card == "y":
#     while hit:
#         new_player_card_choose = random.choice(cards)
#         new_player_deck.append(new_player_card_choose)
#         print(f"Your hand : {new_player_deck}")
#         new_player_score = sum(new_player_deck)
#         print(f"your score : {new_player_score}")
#
#         if new_player_score > 21:
#             print("Bust, You lose.")
#             hit = False
#
#         if new_player_score < 21:
#             another_card = input("Type 'y' to get another card or type 'n' ").lower()
#
#         if another_card == "n":
#             hit = False
#
# print(f"Your final hand : {new_player_deck}")
# print(f"final score : {new_player_score}")
# print(f"Computer final hand : {new_dealer_deck}")
# print(f"Computer final score : {new_dealer_score}")
#
#
# if new_dealer_score == 21:
#     print("Blackjack, Dealer won!!")
# elif new_player_score == 21:
#     print("Blackjack, You won!!")
# elif new_dealer_score > 21 or new_player_score < 21 and new_player_score > new_dealer_score:
#     print("You win.")
# elif new_dealer_score < 21 and new_dealer_score > new_player_score or new_player_score > 21:
#     print("You lose.")

# GPT CODE
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    score = sum(hand)

    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


play_game = input("Do you want to play a game of Blackjack? y/n ").lower()

if play_game == "y":
    print(logo)

player_cards = random.sample(cards, 2)
dealer_cards = random.sample(cards, 1)

current_player_score = calculate_score(player_cards)
dealer_score = calculate_score(dealer_cards)

print(f"Your Cards: {player_cards}")
print(f"Your current Score : {current_player_score}")

print(f"Computer's first card : {dealer_cards[0]}")

another_card = input("Type 'y' to get another card or type 'n' to pass ").lower()

hit = True

new_dealer_score = dealer_score
new_dealer_deck = dealer_cards.copy()

new_player_deck = player_cards.copy()
new_player_score = current_player_score

# Dealer draws until 17 or higher
while new_dealer_score < 17:
    choose_new_card = random.choice(cards)
    new_dealer_deck.append(choose_new_card)
    new_dealer_score = calculate_score(new_dealer_deck)

if another_card == "y":
    while hit:
        new_player_card_choose = random.choice(cards)
        new_player_deck.append(new_player_card_choose)

        new_player_score = calculate_score(new_player_deck)

        print(f"Your hand : {new_player_deck}")
        print(f"Your score : {new_player_score}")

        if new_player_score > 21:
            hit = False
        else:
            another_card = input(
                "Type 'y' to get another card or type 'n' to pass "
            ).lower()

            if another_card == "n":
                hit = False

print(f"\nYour final hand : {new_player_deck}")
print(f"Your final score : {new_player_score}")

print(f"Computer final hand : {new_dealer_deck}")
print(f"Computer final score : {new_dealer_score}")

# Result logic
if len(new_dealer_deck) == 2 and new_dealer_score == 21:
    print("Blackjack! Dealer won!")

elif len(new_player_deck) == 2 and new_player_score == 21:
    print("Blackjack! You won!")

elif new_player_score > 21:
    print("Bust! You lose.")

elif new_dealer_score > 21:
    print("Dealer busts! You win.")

elif new_player_score > new_dealer_score:
    print("You win.")

elif new_dealer_score > new_player_score:
    print("You lose.")

else:
    print("Draw.")













