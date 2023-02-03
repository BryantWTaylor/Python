print()
# using double quotations for the following strings as the strings themselves
# contain a single quote in the form of a apostrophe.
kids_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
# started using single quotations for strings again.
kids = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))

kids_total = kids * kids_meal
adults_total = adults * adult_meal
subtotal = kids_total + adults_total
sales_tax = subtotal * tax / 100
total_price = sales_tax + subtotal

print()
print(f'Subtotal: ${subtotal}')
print(f'Sales Tax: ${sales_tax}')
print(f'Total: ${total_price}')
print()

amount = float(input('What is the payment amount? '))
change = amount - total_price
print(f'Change: ${change}')
print()
