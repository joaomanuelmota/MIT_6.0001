# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations
from itertools import permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words("words.txt")
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
     #delete this line and replace with your code here
    
    def get_message_text(self):
        return self.message_text
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        #delete this line and replace with your code here

    def get_valid_words(self):
        return self.valid_words.copy()
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        #delete this line and replace with your code here
                
    def build_transpose_dict(self, vowels_permutation):
        vowels = 'aeiou'
        transpose_dict = {}

        #interact through all lowercase letters
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char in vowels:
                index = vowels.index(char)
                transpose_dict[char] = vowels_permutation[index]
                transpose_dict[char.upper()] = vowels_permutation[index].upper()
            else:
                transpose_dict[char] = char
                transpose_dict[char.upper()] = char.upper()

        return transpose_dict
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        #delete this line and replace with your code here
    
    def apply_transpose(self, transpose_dict):
        encrypted_message = ''

        for char in self.message_text:
            if char.isalpha():
                encrypted_message += transpose_dict[char]
            else:
                encrypted_message += char

        return encrypted_message
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        #delete this line and replace with your code here
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        super().__init__(text)
        self.valid_words = load_words()
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass #delete this line and replace with your code here

    def decrypt_message(self):
        vowels = 'aeiou'
        best_decryption = self.message_text
        max_valid_words = 0

        for perm in permutations(vowels):
            vowels_permutation = ''.join(perm)
            transpose_dict = self.build_transpose_dict(vowels_permutation)

            # Create reverse dictionary for decryption
            reverse_dict = {v: k for k, v in transpose_dict.items()}

            decrypted_message = self.apply_transpose(reverse_dict)
            valid_words = sum(word.lower() in self.valid_words for word in decrypted_message.split())

            if valid_words > max_valid_words:
                max_valid_words = valid_words
                best_decryption = decrypted_message

        return best_decryption

        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #delete this line and replace with your code here
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
