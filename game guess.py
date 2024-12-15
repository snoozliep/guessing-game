import random
from words import words

def get_valid_word(word_list):
    """
    Selects a random valid word from the provided word list.
    """
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.lower()

word = get_valid_word(words)
guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        word = get_valid_word(words)
        guessedWord = ['_'] * len(word)
        attempts = 10
    elif attempts == 0:
        print('\nYou\'ve run out of attempts! The word was: ' + word)
        word = get_valid_word(words)
        guessedWord = ['_'] * len(word)
        attempts = 10
