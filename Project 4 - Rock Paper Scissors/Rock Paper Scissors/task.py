import random

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


user = input("Type 1 for rock, 2 for paper or 3 for scissors ")

computer_input = [rock, paper, scissors]

if user == "1":
    print(rock)
elif user == "2":
    print(paper)
elif user == "3":
    print(scissors)

random_computer_input = random.choice(computer_input)
print(random_computer_input)

if random_computer_input == rock and user == "1" or random_computer_input == paper and user == "2" or random_computer_input == scissors and user == "3":
    print("Its a draw")
elif random_computer_input == rock and user == "2" or random_computer_input == scissors and user == "1" or random_computer_input == paper and user == "3":
    print("You Win")
elif random_computer_input == paper and user == "1" or random_computer_input == scissors and user == "2" or random_computer_input == rock and user == "3":
    print("You Lose")