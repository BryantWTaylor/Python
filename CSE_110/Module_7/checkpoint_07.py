# task 1
number = int(input('Plese type a positive number: '))

while number < 0:
    print('Sorry, that is a negative number. Please try again.')
    number = int(input('Plese type a positive number: '))

print(f'The number is: {number}')

# task 2
candy = input('May I have a piece of candy? ')

while candy.lower() != 'yes':
    candy = input('May I have a piece of candy? ')
print('Thank you.')

# task 2 could be written as follows
# candy = ''
# while candy.lower() != 'yes':
    # candy = input('May I have a piece of candy? ')
# print('Thank you.')