age1 = int(input('What is the age of the first rider? '))
height1 = int(input('What is the height of the first rider? '))
if age1 >= 12 and age1 < 18:
    golden1 = input('Do you have a golden passport? ')

is_second_rider = input('Is there a second rider (yes/no)? ')

if is_second_rider.lower() == 'yes':
    age2 = int(input('What is the age of the second rider? '))
    height2 = int(input('What is the height of the second rider? '))

    if age2 >= 12 or age1 < 18:
        golden2 = input('Do you have a golden passport for the second rider? ')

        if height1 < 36 or height2 < 36:
            can_ride = False
        else:
            if age1 >= 18 or age2 >= 18 or golden1.lower() == 'yes' or golden2.lower() == 'yes': #stretch
                can_ride = True
            elif age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52: #stretch
                can_ride = True
            elif (age1 >=16 and age2 >= 14) or (age1 >= 14 and age2 >= 16): #stretch
                can_ride = True
            else:
                can_ride = False
else:
    if (age1 >= 18 or golden1.lower() == 'yes') and height1 >= 62: #stretch
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')