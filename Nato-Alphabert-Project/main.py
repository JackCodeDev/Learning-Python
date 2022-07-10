import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(df)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

new_data = {row.letter: row.code for (index, row) in df.iterrows()}
print(new_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter the word: ")
new_list = [new_data[letter] for letter in name.upper()]
print(new_list)
