import random
again = 'yes'
while again.lower() == 'yes':
    number = random.randint(1, 100)
    guess = int(input('What is your guess? '))
    guesses = 1
    while guess != number:
        if guess > number:
            print('Lower')
        elif guess < number:
            print('Higher')
        guess = int(input('What is your guess? ')) 
        guesses = guesses + 1
    print('You guessed it!')
    print(f'It took {guesses} guesses.')
    again = input('Do you want to play again (Yes/No)? ')