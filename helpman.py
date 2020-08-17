import string

def is_word_guessed(secret_word, letters_guessed):
    if set(secret_word).issubset(letters_guessed):
    	guessed = True
    else:
    	guessed = False
    return guessed

def get_guessed_word(secret_word, letters_guessed):
    correct_letters = []
    guessed_string = ""
    for letter in letters_guessed:
        if letter in secret_word:
        	correct_letters.append(letter)
    for letter in secret_word:
    	if letter in correct_letters:
    		guessed_string += letter
    	else:
    		guessed_string += "_ "
    print(guessed_string)

def get_available_letters(letters_guessed):
    letters = list(string.ascii_lowercase)
    unguessed = ""
    for letter in letters:
        if letter not in letters_guessed:
            unguessed += letter
    return unguessed