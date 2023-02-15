import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

NAME_INDEX = 0
EMAIL_INDEX = 1
DATE_INDEX = 2
current_date_and_time = datetime.now()
discount_date = current_date_and_time - relativedelta(years=2)

def main():
    print("\nWelcome to the Glasses Price Calculator!")
    # create dictionary of previous customers
    customer_dict = make_dictionary("customers.csv", EMAIL_INDEX)

    # ask user for the price of the frames that they picked out.
    frame_price = float(input("\nWhat is the price of the frames? "))

    # ask user what type of lens they need: (Single Vision or Progressive)
    lens_type = input("What type of lens do you need? (Single Vision / Progressive) ").lower()

    # ask user if they require a thinner lens based on their RX.
    lens_thinkness = input("Do you need a thinner lens based on your prescription? (Y / N) ").lower()

    # ask user for their name.
    name = input("\nPlease enter your name: ").capitalize()

    # ask user for their email as this is used for the key in the dicitonary.
    email = input("Please enter your email address: ")

    # get the subtotal before any potential discount by calling two of my created fucntions, get_lens_price is a parameter for get_combined_price
    pre_discount_subtotal = get_combined_price(get_lens_price(lens_type, lens_thinkness), frame_price)

    # print out the pre discount subtotal.
    print(f"\nThe subtotal is: ${pre_discount_subtotal:.2f}")


    # calling the get discount function to see if the customer is a return client or if they are a new client.
    discount = get_discount(email, customer_dict)

    # printing out the final prices with tax and any discounts that the customer may have received.
    if discount != None:
        discount_amount = pre_discount_subtotal * discount
        print(f"Your discount amount is: ${discount_amount:.2f}")
        total = (pre_discount_subtotal - discount_amount)
    else:
        total = pre_discount_subtotal

    tax_amount = total * .0725
    final_total = total + tax_amount
    print(f"The sales tax is: ${tax_amount:.2f}")
    print(f"Your total cost is: ${final_total:.2f}\n")
    print(f"Thank you for shopping with us, {name}. Have a wonderful day!\n")


def get_lens_price(lens_type, thickness):
    """This function will take the type of lens that the user has chosen as 
        well as the thickness and determine the cost of the lens based on 
        those parameters.
        
        Parameters 
            type: The tupe of lens that the user chose
            thickness: if the user chose the thinner lens
        Return: price of the lens based on the parameters"""

    if lens_type == "single vision" and thickness == "y":
        price = 79.99
    elif lens_type == "single vision" and thickness == "n":
        price = 59.99
    elif lens_type == "progressive" and thickness == "n":
        price = 129.99
    else:
        price = 159.99
    
    return price

def get_combined_price(lens_price, frame_price):
    """This function will take the price of the lens that we get from
        the get_lens_price() function and the price of the frames that
        the user input and add them together to give us our subtotal.
        
        Parameters 
            lens_price: The price of lens that was calculated from the function
            frame_price: price of the frames the user input.
        Return: The sum of the two parameters to give us the subtotal of this set
                of glasses"""
    
    subtotal = lens_price + frame_price
    return subtotal

def get_discount(email, dictionary):
    """This function will take the email of the customer and 
        and if they are a new customer. If they claim they are a new customer
        we will search our dictionary for their info and if we don't find them, 
        they will get a 10% discount and if we find them and it has been over
        2 years since their last purchase, they will get a 5% discount.
        
        Parameters 
            name: The name of the customer
            email: The email address of the customer
            new_customer: if the customer is a new customer or not
            dictionary: the customer dictionary that has a the previous customers
        Return: The discount amount that the customer will get"""
    
    if email in dictionary:
        value = dictionary[email]

        last_purchase_date = value[DATE_INDEX]
        converted_date = datetime.strptime(last_purchase_date, "%Y-%m-%d")
        if converted_date > discount_date:
            discount = None
        if converted_date < discount_date:
            discount = .05
    else:
        discount = .10
    return discount


def make_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary
    

if __name__ == "__main__":
    main()
