#lists and variables
items = []
item = ''

#getting input and appending list
print('Please enter the items of the shopping list (type "quit" to finish):')
while item != 'quit':
    item = input('Item: ').lower()
    if item != 'quit':
        items.append(item)

#printing out the list
print('The shopping list is:')
for item in items:
    print(item.capitalize())
print()

#printing out the list with indexes
print('The shopping list with indexes is:')
for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item.capitalize()}')
print()

change = int(input('Which item would you like to change?: '))
new_item = input('What is the new item? ')
items[change] = new_item

for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item.capitalize()}')
print()

