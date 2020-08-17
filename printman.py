import string

def print_hangman(guesses, secret_word):
	if (guesses == 0):
		print ("""
		      __________
	              |     |
	              |
	              |
	              |
	              |
	              |_________
	             """)
	elif (guesses == 1):
		print ("""
		      __________
	              |     |
	              |
	              |     |
	              |     |
	              |
	              |_________
	             """)
	elif (guesses == 2):
		print ("""
		      __________
	              |     |
	              |
	              |    \|
	              |     |
	              |
	              |_________
	             """)
	elif (guesses == 3):
		print ("""
		      __________
	              |     |
	              |
	              |    \|/
	              |     |
	              |
	              |_________
	             """)
	elif (guesses == 4):
		print ("""
		      __________
	              |     |
	              |
	              |    \|/
	              |     |
	              |    ^
	              |_________
	             """)
	elif (guesses == 5):
		print ("""
		      __________
	              |     |
	              |
	              |    \|/
	              |     |
	              |    ^ ^
	              |_________
	             """)
	elif (guesses == 6):
		print ("""
              __________
                  |     |
                  |     0
                  |    \|/
                  |     |
                  |    ^ ^
                  |__________
                """)
		print(f"\nNo more guesses.\nThe word was '{secret_word}'.\nMy condolences.\n")