items = []
item = ''
action = -1

print()
print('Welcome to the Shopping Cart Program!\n')


while action != 5:
    print('Please select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
    action = int(input('\nPlease enter an action: '))
    if action == 1:
        item = input('\nWhat item do you want to add? ').lower()
        items.append(item.capitalize())
        print(f'{item.capitalize()} was added to your shopping cart.')
    elif action == 2:
        print('\nThe contents of the shopping cart are:')
        for item in items:
            print(item)

print('\nThank you. Goodbye.')
print()