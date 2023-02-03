account_names = []
account_balances = []
name = ''
balance = 0
total_balance = 0
largest_balance = -1
largest_name = ''

print("\nEnter the names and balances of bank accounts (type 'quit' when done)")
while name.lower() != 'quit':
    name = input('What is the name of this account? ')
    if name.lower() != 'quit':
        balance = float(input('What is the balance? '))
        account_names.append(name.capitalize())
        account_balances.append(balance)

print('\nAccount Information:')
for i in range(len(account_balances)):
    balance = account_balances[i]
    name = account_names[i]
    print(f'{i}. {name} - ${balance:.2f}')

for balance in account_balances:
    total_balance += balance
print(f'\nTotal: ${total_balance:.2f}')
print(f'Average: ${total_balance / len(account_balances):.2f}')

for i in range(len(account_names)):
    balance = account_balances[i]
    name = account_names[i]
    if balance > largest_balance:
        largest_balance = balance
        largest_name = name
print(f'Highest balance: {largest_name} - ${largest_balance:.2f}')

print()
update = 'yes'

while update.lower() == 'yes':
    update = input('Do you want to update an account? ')
    if update.lower() == 'yes':
        index = int(input('Which index do you want to update? '))
        balance = float(input('What is the new amount? '))
        account_balances[index] = balance
    print('\nAccount Information:')
    for i in range(len(account_balances)):
        balance = account_balances[i]
        name = account_names[i]
        print(f'{i}. {name} - ${balance:.2f}')
print()


