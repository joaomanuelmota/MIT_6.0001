# Problem Set 2, hangman.py
# Name: João Mota
# Collaborators:
# Time spent: endless hours :)

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def get_guessed_word(secret_word, letters_guessed):
    return ''.join([char if char in letters_guessed else '_ ' for char in secret_word])

    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def get_available_letters(letters_guessed):
    available_letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
        if letter in available_letters:
            available_letters.remove(letter)
    return ''.join(available_letters)
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"


def hangman(secret_word):

    letters_guessed = []
    guess = 6
    warnings = 3
    vowels = ["a", "e", "i", "o"]

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("_" * len(secret_word))
    print(f"You have {guess} guesses left.")
    print(f"You have {warnings} warnings left. ")
    print(f"Available Letters: {get_available_letters(letters_guessed)}")
    print(secret_word) # For debugging purposes


    while guess > 0 and not is_word_guessed(secret_word, letters_guessed):
        letter = input("Please guess a letter: ").lower()
        if letter.isalpha() and len(letter) == 1:
            if letter in letters_guessed:
                print(f"You've already guessed the letter '{letter}'.")
                if warnings > 0:
                    warnings -= 1
                    print(f"You have {warnings} warnings left.")
                else:
                    guess -= 1
                    print(f"You have {guess} guesses left.")
            else:
                letters_guessed.append(letter)
                if letter in secret_word:
                    print(f"Good Guess: {get_guessed_word(secret_word, letters_guessed)}")
                    print("________________")
                    print(f"You have {guess} guesses left.")
                    print(f"Available Letters: {get_available_letters(letters_guessed)}")
                else:
                    if letter not in vowels:
                        guess -= 1
                    else:
                        guess -= 2
                    print(f"Ops, That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    print("________________")
                    print(f"Available Letters: {get_available_letters(letters_guessed)}")
                    print(f"You have {guess} guesses left.")
        else:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guess -= 1
                print(f"Oops! That is not a valid letter. You have {guess} guesses left: {get_guessed_word(secret_word, letters_guessed)}")
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guess * len(set(secret_word))
        print(f"Congratulations, you guessed the word!: {secret_word}")
        print(f"Your total score for this game is: {total_score}")
    elif guess == 0:
        print(f"Game over. The word was '{secret_word}")

    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ', '')

    if len(other_word) != len(my_word):
        return False

    for mw_char, ow_char in zip(my_word, other_word):
        if mw_char == ow_char:
            continue
        if mw_char == "_" and ow_char not in my_word:
            continue
        else:
            return False
    return True
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''




def show_possible_matches(my_word):
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print('Hints: ', " ".join(matches))
    else:
        print("No matches found!")

    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"




def hangman_with_hints(secret_word):

    letters_guessed = []
    guess = 6
    warnings = 3
    vowels = ["a", "e", "i", "o"]


    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("_" * len(secret_word))
    print(f"You have {guess} guesses left.")
    print(f"You have {warnings} warnings left. ")
    print(f"Available Letters: {get_available_letters(letters_guessed)}")
    print(secret_word) # For debugging purposes


    while guess > 0 and not is_word_guessed(secret_word, letters_guessed):
        letter = input("Please guess a letter: ").lower()
        if (letter.isalpha() or letter == "*") and len(letter) == 1:
            if letter == "*":
                my_word = get_guessed_word(secret_word, letters_guessed)
                show_possible_matches(my_word)
            elif letter in letters_guessed:
                print(f"You've already guessed the letter '{letter}'.")
                if warnings > 0:
                    warnings -= 1
                    print(f"You have {warnings} warnings left.")
                else:
                    guess -= 1
                    print(f"You have {guess} guesses left.")
            else:
                letters_guessed.append(letter)
                if letter in secret_word:
                    print(f"Good Guess: {get_guessed_word(secret_word, letters_guessed)}")
                    print("________________")
                    print(f"You have {guess} guesses left.")
                    print(f"Available Letters: {get_available_letters(letters_guessed)}")
                else:
                    if letter not in vowels:
                        guess -= 1
                    else:
                        guess -= 2
                    print(f"Ops, That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    print("________________")
                    print(f"Available Letters: {get_available_letters(letters_guessed)}")
                    print(f"You have {guess} guesses left.")
        else:
            if warnings > 0:
                warnings -= 1
                print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guess -= 1
                print(f"Oops! That is not a valid letter. You have {guess} guesses left: {get_guessed_word(secret_word, letters_guessed)}")
    if is_word_guessed(secret_word, letters_guessed):
        total_score = guess * len(set(secret_word))
        print(f"Congratulations, you guessed the word!: {secret_word}")
        print(f"Your total score for this game is: {total_score}")
    elif guess == 0:
        print(f"Game over. The word was '{secret_word}")

    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
