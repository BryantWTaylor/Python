# Function to calculate windchill for given temperature and for given windspeed
def find_windchill(temp, wind):
    windchill = (35.74 + (0.6215 * temp) - 35.75 * (wind ** 0.16) + (0.4275 * temp * (wind ** 0.16)))
    return windchill

# Function to convert user input temperature from Celsius to Fahrenheit
def convert_temp(celsius_temp):
    fahrenheit_temp = (celsius_temp * 1.8) + 32
    return fahrenheit_temp

wind = 0
user_temp = float(input('\nWhat is the temperature? '))
temp_type = input('Fahrenheit or Celsius (F/C)? ')
print()

if temp_type.lower() == 'c':
    for i in range(0, 12):
        wind += 5
        print(f'At temperature {convert_temp(user_temp):.1f}F, and wind speed {wind} mph, the windchill is: {find_windchill(convert_temp(user_temp), wind):.2f}F')
    
else:
    for i in range(0, 12):
        wind += 5
        print(f'At temperature {user_temp:.1f}F, and wind speed {wind} mph, the windchill is: {find_windchill(user_temp, wind):.2f}F')
print()
