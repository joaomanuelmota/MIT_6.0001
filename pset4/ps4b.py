# Problem Set 4B
# Name: João Mota

import string


### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words("words.txt")
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''

    def get_message_text(self):
        return self.message_text
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text

        '''

    def get_valid_words(self):
        return self.valid_words.copy()
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        # delete this line and replace with your code here

    def build_shift_dict(self, shift):
        lowercase_alphabet = string.ascii_lowercase
        uppercase_alphabet = string.ascii_uppercase
        dictionary = {}

        for i, char in enumerate(lowercase_alphabet):
            dictionary[char] = lowercase_alphabet[(i + shift) % 26]

        for i, char in enumerate(uppercase_alphabet):
            dictionary[char] = uppercase_alphabet[(i + shift) % 26]

        return dictionary
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        

        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # delete this line and replace with your code here

    def apply_shift(self, shift):
        dictionary = self.build_shift_dict(shift)
        return ''.join(dictionary.get(char, char) for char in self.message_text)
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # delete this line and replace with your code here


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        super().__init__(text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # delete this line and replace with your code here

    def get_shift(self):
        return self.shift

        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
          # delete this line and replace with your code here

    def get_encryption_dict(self):
        return self.encryption_dict.copy()

        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        # delete this line and replace with your code here

    def get_message_text_encrypted(self):
        return self.message_text_encrypted
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
         # delete this line and replace with your code here

    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
         # delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        super().__init__(text)

        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # delete this line and replace with your code here

    def decrypt_message(self):
        best_shift = 0
        max_valid_words = 0
        best_decrypyted_message = ''

        for shift in range(26):
            decrypted_message = self.apply_shift(26 - shift)
            words = decrypted_message.split()
            valid_word_count = sum(word in self.valid_words for word in words)

            if valid_word_count > max_valid_words:
                max_valid_words = valid_word_count
                best_shift = 26 - shift
                best_decrypyted_message = decrypted_message

        return (best_shift, best_decrypyted_message)
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
         # delete this line and replace with your code here


if __name__ == '__main__':
    #    #Example test case (PlaintextMessage)
    #    plaintext = PlaintextMessage('hello', 2)
    #    print('Expected Output: jgnnq')
    #    print('Actual Output:', plaintext.get_message_text_encrypted())
    #
    #    #Example test case (CiphertextMessage)
    #    ciphertext = CiphertextMessage('jgnnq')
    #    print('Expected Output:', (24, 'hello'))
    #    print('Actual Output:', ciphertext.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE
    plaintext = PlaintextMessage('hello',2 )
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:' (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    # TODO: best shift value and unencrypted story

     # delete this line and replace with your code here
