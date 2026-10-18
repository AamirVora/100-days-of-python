import random
from game_data import data
from art import logo
from art import vs

player_right = True
score = 0
select_b = random.choice(data)

while player_right:
    choice_a = select_b
    select_b = random.choice(data)
    followers_count_a = choice_a["follower_count"]
    followers_count_b = select_b["follower_count"]
    select_a_full_data = choice_a["name"], choice_a["description"], choice_a["country"]
    select_b_full_data = select_b["name"], select_b["description"], select_b["country"]

    print(logo)
    print("Compare A: ", end="")
    print(select_a_full_data)
    print(vs)
    print("Against B: ", end="")
    print(select_b_full_data)
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    print("\n")

    if followers_count_a > followers_count_b and user_input == "A":
        score += 1
        print("You're correct, ", end = " ")
        print(f"Current score: {score}")
        print(select_a_full_data)
        print(followers_count_a)
        print("\n" * 30)
    elif followers_count_a < followers_count_b and user_input == "B":
        score += 1
        print("You're correct, ", end = " ")
        print(f"Current score: {score}")
        print(select_b_full_data)
        print(followers_count_b)
        print("\n" * 30)
    else:
        print("You're wrong")
        print(f"Total score: {score}")
        continue_playing = input("Do you want to try again? Y/N: ")
        if continue_playing == "Y":
            print("\n" * 30)
            score = 0
        elif continue_playing == "n":
            print("Thank you for playing")
            player_right = False
        else:
            print("invalid input")