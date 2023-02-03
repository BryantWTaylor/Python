print()
# using double quotations for the following strings as the strings themselves
# contain a single quote in the form of a apostrophe.
kids_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
# started using single quotations for strings again.
shakes = float(input('What is the price of a milkshake? '))
kids = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
shakes_amount = int(input('How many milkshakes are wanted? '))
tax = float(input('What is the sales tax rate? '))

shakes_total = shakes * shakes_amount
kids_total = kids * kids_meal
adults_total = adults * adult_meal
subtotal = kids_total + adults_total + shakes_total
sales_tax = subtotal * tax / 100
total_price = sales_tax + subtotal
tip = total_price * .18

print()
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total_price:.2f}')
print(f'Suggested 18% tip: ${tip:.2f}\n')

pay_tip = input('Do you want to pay a tip? ')
if pay_tip.lower() == 'yes':
    total_payment = total_price + tip
elif pay_tip.lower() == 'no':
    total_payment = total_price

print()
print(f'Your total charge is: ${total_payment:.2f}')
amount = float(input('What is your payment amount? '))
change = amount - total_payment
print(f'Change: ${change:.2f}\n')
