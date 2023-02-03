import math
# square = float(input('What is the length of the side of a square? '))
# square_area = square**2
# print(f'The area of the square is: {square_area}') 
# rectangle_length = float(input('What is the length of a rectangle? '))
# rectangle_width = float(input('What is the width of a rectangle? '))
# rectangle_area = rectangle_length * rectangle_width
# print(f'The area of the rectangle is: {rectangle_area}')
# circle = float(input('What is the radius of a circle? '))
# # circle_area = circle**2 * math.pi
# circle_area = circle**2 * 3.14159
# print(f'The area of the circle is: {circle_area}')

length = float(input('Please enter a length: '))
square_area = length ** 2
circle_area = length * math.pi
cube_volume = length ** 3
sphere_volume = (4/3) * math.pi * length ** 3
print (f'The area of a square is: {square_area}')
print (f'The area of a circle is: {circle_area}')
print (f'The volume of a cube is: {cube_volume}')
print (f'The volume of a sphere is: {sphere_volume}')

