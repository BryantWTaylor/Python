import math  # importing math in order to use math.pi
from datetime import datetime # importing datetime to be able to get current date and time

# collecting width from user input and storing it as an int
width = int(input('\nEnter the width of the tire in mm (ex 205): '))
# collecting aspect ratio from user input and storing it as an int
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
# collecting diameter from user input and storing it as an int
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10000000000  # calculating volume of the tire with the given formula

current_date_time = datetime.now() #variable to store current date and time for future use in code

# displaying answer to the screen
print(f'\nThe approximate volume is {volume:.2f} liters')
print()

# The following is a set of if statements of 5 of the most popular tire sizes with prices to be displayed to the user.
if width == 225 and aspect_ratio == 65 and diameter == 17:
    print('We found 3 sets of tires that might be a good fit for you.\nA good set at $99 each. A Better set at $145 each. A BEST set at $197 each.\n')
elif width == 275 and aspect_ratio == 55 and diameter == 20:
    print('We found 3 sets of tires that might be a good fit for you.\nA good set at $152 each. A Better set at $195 each. A BEST set at $263 each.\n')
elif width == 235 and aspect_ratio == 40 and diameter == 19:
    print('We found 3 sets of tires that might be a good fit for you.\nA good set at $157 each. A Better set at $165 each. A BEST set at $215 each.\n')
elif width == 235 and aspect_ratio == 60 and diameter == 18:
    print('We found 3 sets of tires that might be a good fit for you.\nA good set at $105 each. A Better set at $176 each. A BEST set at $249 each.\n')
elif width == 235 and aspect_ratio == 45 and diameter == 18:
    print('We found 3 sets of tires that might be a good fit for you.\nA good set at $104 each. A Better set at $151 each. A BEST set at $200 each.\n')
elif width == 245 and aspect_ratio == 60 and diameter == 18:
    print('We found 3 sets of tires that might be a good fit for you.\nA good set at $124 each. A Better set at $184 each. A BEST set at $250 each.\n')
else:
    print("We couldn't find any results in our quick access database,\nbut one of our sales associates would be happy to help you find the right tires for your vehicle.\n")


purchase = input('Would you like to buy some tires? ').lower() # asking user if they would like to buy some tires.

# if statement regarding whether or not the member decided to purchase tires.
if purchase == 'yes':
    phone_number = input('What is your phone number? ') # gathering users phone number for future sale of tires
    print('\nThank you! We will be in touch. Have a fantastic day.')
    print()
else:
    phone_number = 'N/A' # user decided not to purchase tires, so we have not collected a phone number and will store "N/A" in the txt file
    print('Thank you! Have a wonderful day.')
    print()


with open("volumes.txt", "at") as volume_file: # opening the file, printing to it and then closing the file.
    print(f'{current_date_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, Phone: {phone_number}\n', file=volume_file)
    volume_file.close()
