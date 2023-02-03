'''You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.'''
from datetime import datetime

subtotal = float(input('\nPlease enter the subtotal: '))
current_date_and_time = datetime.now()
day = current_date_and_time.weekday()
sales_tax = subtotal * .06

if (day == 1 or day == 2) and subtotal >= 50:
    discount = subtotal * .10
    new_subtotal = subtotal - discount
    discounted_sales_tax = new_subtotal * .06
    print(f'Discount amount is: {discount:.2f}')
    print(f'Sales tax amount is: {discounted_sales_tax:.2f}')
    print(f'Total: {new_subtotal + discounted_sales_tax:.2f}')
    print()
else:
    print(f'Sales tax amount is: {sales_tax:.2f}')
    print(f'Total: {subtotal + sales_tax:.2f}')
    print()


