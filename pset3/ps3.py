import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    inFile.close()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):
    word = word.lower()
    score1 = 0

    if word == '':
        return 0
    else:
        for letter in word:
            if letter in SCRABBLE_LETTER_VALUES:
                score1 += SCRABBLE_LETTER_VALUES[letter]

        score2 = (7 * len(word)) - 3 * (n - len(word))

        if score2 <= 1:
            score2 = 1

        score = score1 * score2
    return score


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


def deal_hand(n):
    hand = {}
    num_vowels = int(math.ceil(n / 3))
    hand["*"] = 1

    for i in range(num_vowels - 1):  # Subtract 1 to account for the '*' wildcard
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels - 1, n - 1):  # Adjust to account for the '*' wildcard
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    new_hand = hand.copy()
    word = word.lower()
    for letter in word:
        if letter in new_hand:
            new_hand[letter] -= 1
            if new_hand[letter] == 0:
                del new_hand[letter]
    return new_hand


def is_valid_word(word, hand, word_list):
    def can_form_word(word, hand):
        hand_copy = hand.copy()
        for letter in word:
            if letter not in hand_copy or hand_copy[letter] <= 0:
                return False
            hand_copy[letter] -= 1
        return True

    word = word.lower()

    if "*" in word:
        for vowel in VOWELS:
            possible_word = word.replace("*", vowel)
            if possible_word in word_list and can_form_word(word, hand):
                return True
        return False
    else:
        return word in word_list and can_form_word(word, hand)


def calculate_handlen(hand):
    return sum(hand.values())


def play_hand(hand, word_list, n):
    score = 0
    while calculate_handlen(hand) > 0:
        print("Current Hand: ", end="")
        display_hand(hand)

        word = input("Enter word, or '!!' to indicate that you are finished: ")
        if word == "!!":
            break
        else:
            if is_valid_word(word, hand, word_list):
                word_score = get_word_score(word, n)
                score += word_score
                print(f"'{word}' earned {word_score} points. Total: {score} points")
            else:
                print("That is not a valid word. Please choose another word.")

            hand = update_hand(hand, word)

    print(f"Ran out of letters. Total score: {score} points")
    return score


def substitute_hand(hand, letter):
    if letter not in hand:
        return hand

    hand_copy = hand.copy()
    count = hand_copy[letter]
    del hand_copy[letter]

    available_letters = set(VOWELS + CONSONANTS) - set(hand_copy.keys())
    new_letter = random.choice(list(available_letters))
    hand_copy[new_letter] = count

    return hand_copy


def play_game(word_list):
    total_score = 0
    total_hands = int(input("Enter total number of hands: "))
    subs_count = 1
    replay_count = 1

    for _ in range(total_hands):
        hand = deal_hand(HAND_SIZE)
        print("Current hand: ", end="")
        display_hand(hand)

        if subs_count == 1:
            subs = input("Would you like to substitute a letter? ").lower().strip()
            if subs == "yes":
                subs_count -= 1
                letter = input("Which letter would you like to replace: ").strip().lower()
                hand = substitute_hand(hand, letter)

        score = play_hand(hand, word_list, HAND_SIZE)

        if replay_count == 1:
            replay = input("Would you like to replay the hand? ").lower().strip()
            if replay == "yes":
                replay_count -= 1
                score2 = play_hand(hand, word_list, HAND_SIZE)
                score = max(score, score2)

        total_score += score
        print(f"Total score for this hand: {score}")

    print(f"Total score over all hands: {total_score}")
    return total_score


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
