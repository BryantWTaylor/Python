print('Welcome to the word guessing game!')
secret_word = 'pokemon'

guess = ''
guesses = 0

while guess.lower() != secret_word:
    guess = input('What is your guess? ')
    if guess.lower() != secret_word:
        print('Your guess was not correct? ')
    else:
        print('Congratulations! You guessed it!')
    guesses = guesses + 1

print(f'It took you {guesses} guesses.')
