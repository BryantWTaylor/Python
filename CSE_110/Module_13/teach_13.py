import math

def compute_area_square(length):
    area = compute_area_rectangle(length, length)
    return area

def compute_area_rectangle(length, width):
    area = length * width
    return area

def compute_area_circle(radius):
    area = (radius ** 2) * math.pi
    return area

def compute_area(shape, length, width=None):
    if shape == 'square':
        area = compute_area_circle(length)
    elif shape == 'circle':
        area = compute_area_circle(length)
    elif shape == 'rectangle':
        area = compute_area_rectangle(length, width)
        
    return area

# side_of_square = float(input('What is the length of the side of a square? '))
# length_of_rect = float(input('What is the length of the side of a rectangle? '))
# width_of_rect = float(input('What is the width of the side of a rectangle? '))
# radius_of_circle = float(input('What is the radius of a circle? '))

# area_square = compute_area_square(side_of_square)
# print(f'The area of the square is {area_square}.')
# area_rect = compute_area_rectangle(length_of_rect, width_of_rect)
# print(f'The area of the rectangle is {area_rect}.')
# area_cirlce = compute_area_circle(radius_of_circle)
# print(f'The area of the circle is {area_cirlce}.')

shape = ''

while shape != 'quit':
    shape = input("What kind of shape are we working with? (Square, Rectangle, Circle; Type 'Quit' to Exit) ").lower()
    print()
    if shape == 'square':
        side_of_square = float(input('What is the length of the side of a square? '))
        area_square = compute_area(shape, side_of_square)
        print(f'The area of the square is {area_square}.')
        print()
    elif shape == 'rectangle':
        length_of_rect = float(input('What is the length of the side of a rectangle? '))
        width_of_rect = float(input('What is the width of the side of a rectangle? '))
        area_rect = compute_area(shape, length_of_rect, width_of_rect)
        print(f'The area of the rectangle is {area_rect}.')
        print()
    elif shape == 'circle':
        radius_of_circle = float(input('What is the radius of a circle? '))
        area_cirlce = compute_area(shape, radius_of_circle)
        print(f'The area of the circle is {area_cirlce}.')
        print()
    elif shape == 'quit':
        print('Thank you for using our Area Calculator. Have a great day!')
        print()
    else:
        print('Not a valid response. Please try again.')
