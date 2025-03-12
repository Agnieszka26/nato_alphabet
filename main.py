import pandas

#TODO 1. Create a dictionary in this format:
letters_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter:row.code for (index, row) in letters_frame.iterrows() }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word= input("What is your word to spell?\n")
new_list_user_letters = [item.upper() for item in user_word]
new_list_nato_words_user = [dictionary[l] for l in new_list_user_letters]

print(new_list_nato_words_user)
