import random
words = ['pokemon', 'pikachu', 'vampire', 'pokedex', 'ocarina', 'tamriel', 'morthal',
'ancient', 'skyborn', 'stalker', 'gasopod', 'bleeder', 'crawler', 'emperor', 'treader']

print()
print('Welcome to the word guessing game!')  # Welcome

# Initial variables
secret_word = random.choice(words)
guess = ''
guesses = 0
secret_length = len(secret_word)

# Initail hint
print('Your first hint is:', end=' ')
for index in range(secret_length):
    print('_', end=' ')
print()

# first guess and length check
while guess.lower() != secret_word:
    guess = input('\nWhat is your guess? ')
    if len(guess) != len(secret_word):
        print('\nSorry, the guess must have the same number of letters as the secret word.')
    else:
        if guess.lower() != secret_word:
            print('\nYour guess was not correct? ')
            print('Your hint is:', end=' ')
            # guess length defined here so that new guess will be stored
            guess_length = len(guess)
            for index in range(secret_length) and range(guess_length):
                letter_secret = secret_word[index]
                letter_guess = guess.lower()[index]
                if letter_secret == letter_guess:
                    print(letter_guess.upper(), end=' ')
                elif secret_word[0] == letter_guess or secret_word[1] == letter_guess or secret_word[2] == letter_guess or secret_word[3] == letter_guess or secret_word[4] == letter_guess or secret_word[5] == letter_guess or secret_word[6] == letter_guess:
                    print(letter_guess.lower(), end=' ')
                elif letter_secret != letter_guess:
                    print('_', end=' ')
        else:
            print('\nCongratulations! You guessed it!')
    guesses = guesses + 1

print(f'It took you {guesses} guesses.')
print()
