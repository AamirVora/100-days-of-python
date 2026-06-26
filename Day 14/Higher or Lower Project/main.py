import random
from game_data import data
from art import logo
from art import vs


def calculate_followers():
    player_right = True

    while player_right:
        select_a = random.choice(data)
        select_b = random.choice(data)
        followers_count_a = select_a["follower_count"]
        followers_count_b = select_b["follower_count"]
        select_a_full_data = select_a["name"], select_a["description"], select_a["country"]
        select_b_full_data = select_b["name"], select_b["description"], select_b["country"]

        print(logo)
        print("Compare A: ", end="")
        print(select_a_full_data)
        print(vs)
        print("Against B: ", end="")
        print(select_b_full_data)
        user_input = input("Who has more followers? Type 'A' or 'B': ")

        if followers_count_a > followers_count_b and user_input == "A":
            print("You're correct")
            print(select_a_full_data)
            print(followers_count_a)
            player_right = False
            print("\n" * 30)
            calculate_followers()
        elif followers_count_a < followers_count_b and user_input == "B":
            print("You're correct")
            print(select_b_full_data)
            print(followers_count_b)
            player_right = False
            print("\n" * 30)
            calculate_followers()
        else:
            print("You're wrong")
            player_right = False
            continue_playing = input("Do you want to try again? Y/N: ").lower()
            if continue_playing == "y":
                print("\n" * 30)
                calculate_followers()
            elif continue_playing == "n":
                print("Thank you for playing")
            else:
                print("invalid input")


calculate_followers()
