items = []
item_prices = []
price = 0
item = ''
action = -1


print()
print('Welcome to the Shopping Cart Program!')


while action != 5:
    print('\nPlease select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
    action = int(input('Please enter an action: '))
    if action == 1:
        item = input('\nWhat item do you want to add? ').lower()
        price = float(input(f"What is the price of '{item.capitalize()}'? ")) #double quotes used because single quotes contained in string
        items.append(item.capitalize())
        item_prices.append(price)
        print(f"'{item.capitalize()}' has been added to your shopping cart.") #double quotes used because single quotes contained in string
    elif action == 2:
        print('\nThe contents of the shopping cart are:')
        for i in range(len(items)):
            item = items[i]
            price = item_prices[i]
            print(f'{i+1}. {item:<10} - ${price:.2f}')
        amount_of_items = len(items)
        if amount_of_items == 0:
            print('There is nothing in your shopping cart. Add some items! It is almost \033[1;31;40mChristmas!\033[1;37;40m')
        else:
            print(f'The total number of items in your cart is: {amount_of_items}.\nAre you sure that is enough? \033[1;31;40mChristmas \033[1;37;40mis around the corner!')
    elif action == 3:
        list_length = len(items)
        item_remove = int(input('Which item would you like to remove? '))
        item_remove = item_remove - 1
        if item_remove < list_length and item_remove >= 0:
            print(f"'{items[item_remove]}' was removed.")
            items.pop(item_remove)
            item_prices.pop(item_remove)
        else:
            print('Sorry, that is not a valid item number.')
    elif action == 4:
        total_cart = 0
        for price in item_prices:
            total_cart += price
        print(f'The total price of the items in the shopping cart is ${total_cart:.2f}')
    elif action != 5:
        print('Please enter a valid selection.')

print('\nThank you for shopping with us! \033[1;32;40mMerry \033[1;31;40mChristmas!')
print('\033[1;37;40m')