# numbers = []
# number = -1
# total = 0
# largest = 0

# print('Enter a list of numbers, type 0 when finished.')
# while number != 0:
#     number = int(input('Enter number: '))
#     if number != 0:
#         numbers.append(number)

# for number in numbers:
#     total += number

# for number in numbers:    
#     if number > largest:
#         largest = number

# amount = len(numbers)
# average = total / amount

# print(f'The sum is: {total}')
# print(f'The average is: {average}')
# print(f'The largest number is {largest}')

numbers = []
number = -1
total = 0
largest = 0
smallest_positive = 1000

print('Enter a list of numbers (positive and negative), type 0 when finished.')
while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numbers.append(number)

for number in numbers:
    total += number

for number in numbers:    
    if number > largest:
        largest = number

for number in numbers:    
    if number > 0 and number < smallest_positive:
        smallest_positive = number

amount = len(numbers)
average = total / amount
numbers.sort()

print(f'The sum is: {total}')
print(f'The average is: {average}')
print(f'The largest number is: {largest}')
print(f'The smallest positive number is: {smallest_positive}')
print('The sorted list is:')
for number in numbers:
    print(number)