print()
first_num = int(input('What is the first number? '))
second_num = int(input('What is the second number? '))

if first_num > second_num:
    print('The first number is greater.')
else:
    print('The first number is not greater.')

if first_num == second_num:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')

if second_num > first_num:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

print()

#part 2 of assignment
favorite_animal = ('dolphin')
user_animal = input('What is your favorite animal? ')
if user_animal.lower() == favorite_animal:
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')
print()