#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp


import os

print(os.getcwd())

letter = open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r")
letter_read = letter.read()

names = open("..//Mail Merge Project Start/Input/Names/invited_names.txt", "r")
names_read = names.readlines()

for n in names_read:
    n = n.strip()

    new_letter = letter_read.replace("[name]", f"{n}")

    with open(f"./Output/ReadyToSend/{n}_letter.txt", "w") as letter:
        letter.write(new_letter)




