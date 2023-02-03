# grade_percent = float(input('What is you grade percent? '))
# if grade_percent >= 90:
#     print('Your letter grade is an "A."')
# elif grade_percent >= 80:
#     print('Your letter grade is a "B."')
# elif grade_percent >= 70:
#     print('Your letter grade is a "C."')
# elif grade_percent >= 60:
#     print('Your letter grade is a "D."')
# elif grade_percent < 60:
#     print('Your letter grade is an "F."')
# if grade_percent >= 70:
#     print('You passed the class!')
# elif grade_percent < 70:
#     print('You did not pass the class. But you can do it next time!')

grade_percent = float(input('What is you grade percent? '))
if grade_percent >= 90:
    letter = 'A'
elif grade_percent >= 80:
    letter = 'B'
elif grade_percent >= 70:
    letter = 'C'
elif grade_percent >= 60:
    letter = 'D'
elif grade_percent < 60:
    letter = 'F'
print(f'Your letter grade is: {letter}')
if grade_percent >= 70:
    print('You passed the class!')
elif grade_percent < 70:
    print('You did not pass the class. But you can do it next time!')