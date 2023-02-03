import math 
print('Welcome to the Velocity Calculator. Please enter the following:')
mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter: '))
time = float(input('Time (in seconds): '))
density = float(input('Density of the fluid (in kg/m^3, 1.3 for air 1000 for water): '))
area = float(input('Cross sectional area (in m^2): '))
constant = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

inner_c = (1 / 2) * density * area * constant
velocity = math.sqrt((mass * gravity) / inner_c) * (1 - math.exp((-math.sqrt(mass * gravity * inner_c) / mass) * time ))

print()
print(f'The inner value of c is: {inner_c:.3f}')
print(f'The velocity after {time} seconds is: {velocity:.3f} m/s \n')