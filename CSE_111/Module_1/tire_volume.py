import math  # importing math in order to use math.pi

# collecting width from user input and storing it as an int
width = int(input('\nEnter the width of the tire in mm (ex 205): '))
# collecting aspect ratio from user input and storing it as an int
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
# collecting diameter from user input and storing it as an int
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10000000000  # calculating volume of the tire with the given formula

# displaying answer to the screen
print(f'\nThe approximate volume is {volume:.2f} liters')
print()
