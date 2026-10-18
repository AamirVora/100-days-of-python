import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# df = pd.DataFrame.to_dict(data)

nato_dict = {
    row.letter : row.code for (index, row) in data.iterrows()
}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


user_text = input("Enter your text: ").upper()
user_list = list(user_text)

converted_words = [nato_dict[i] for i in user_list]
print(converted_words)




