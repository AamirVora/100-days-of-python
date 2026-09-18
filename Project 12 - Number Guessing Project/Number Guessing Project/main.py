import random
from art import logo

def number_game():
    print(logo)
    numbers = range(1, 101)
    picked_number = random.choice(numbers)
    difficulty = input("Choose a difficulty: easy, or hard: ").lower()

    easy_attempts = 10
    hard_attempts = 5

    if difficulty == "easy":
        print("You have 10 attempts left")
    elif difficulty == "hard":
        print("You have 5 attempts left")

    number_guessed = False
    while not number_guessed:
        user_guess = int(input("Guess a number: "))

        if user_guess == picked_number:
            print(f"Congratulations! You guessed the correct number {picked_number}!")
            number_guessed = True
        elif user_guess > picked_number:
            print("Too high!")
            if difficulty == "easy":
                easy_attempts -= 1
                print(f"You have {easy_attempts} attempts left")
            elif difficulty == "hard":
                hard_attempts -= 1
                print(f"You have {hard_attempts} attempts left")
        elif user_guess < picked_number:
            print("Too low!")
            if difficulty == "easy":
                easy_attempts -= 1
                print(f"You have {easy_attempts} attempts left")
            elif difficulty == "hard":
                hard_attempts -= 1
                print(f"You have {hard_attempts} attempts left")

        if hard_attempts == 0 or easy_attempts == 0:
            print("You're out of lives.")
            continue_game = input("Do you want to play again?. y/n ").lower()
            if continue_game == "y":
                print("\n" * 100)
                number_game()
            elif continue_game == "n":
                print("Thanks for playing. Goodbye!")

number_game()
