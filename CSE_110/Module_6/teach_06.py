first_age = int(input('What is the age of the first rider? '))
first_height = int(input('What is the height of the first rider? '))

is_second_rider = input('Is there a second rider (yes/no)? ')
if is_second_rider.lower() == 'yes':
    second_age = int(input('What is the age of the second rider? '))
    second_height = int(input('What is the height of the second rider? '))

#rules
    if first_height < 36 or second_height < 36: #first rule
        can_ride = False
    else:
        if first_age >= 18 or second_age >= 18: #third rule
            can_ride = True
        else:
            can_ride = False
else:
    if first_age >= 18 and first_height >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride == True:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')