import pandas

letters_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter:row.code for (index, row) in letters_frame.iterrows() }
is_num = True
while is_num:
    user_word= input("What is your word to spell?\n")
    try:
        new_list_user_letters = [item.upper() for item in user_word]
        new_list_nato_words_user = [dictionary[l] for l in new_list_user_letters]
    except KeyError:
        print("Only words and letters, please!")
    else:
        print(new_list_nato_words_user)
        is_num=False
