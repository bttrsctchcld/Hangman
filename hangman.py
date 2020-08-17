import string, random, helpman, printman

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def hangman(secret_word):
    guesses = 0
    letters_guessed = []
    while guesses < 6:
        printman.print_hangman(guesses, secret_word)
        helpman.get_guessed_word(secret_word, letters_guessed)
        available = list(helpman.get_available_letters(letters_guessed))
        print(f"You have {6 - guesses} remaining guesses.")
        guess = input("Guess a letter: ").lower()
        if guess not in letters_guessed:
    	    letters_guessed.append(guess)
        win_condition = helpman.is_word_guessed(secret_word, letters_guessed)
        if win_condition:
            guesses = 0
            printman.print_hangman(guesses, secret_word)
            print(f"\nThat's right.\nIt's '{secret_word}'.\nYou're free to go.\n")
            quit()
        if guess in available and len(guess) == 1:
            letters_guessed.append(guess)
            available.remove(guess)
        else:
            print("Please enter a single letter which you haven't already guessed.")
            continue
        if guess in secret_word:
            helpman.get_guessed_word(secret_word, letters_guessed)
        elif guess not in secret_word and guesses < 6:
            guesses+=1
    printman.print_hangman(guesses, secret_word)

secret_word = choose_word(wordlist)

hangman(secret_word)