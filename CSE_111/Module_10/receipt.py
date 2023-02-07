import csv
from datetime import datetime

def main():
    PROD_NUMBER_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    QUANTITY_INDEX = 1

    try:
        products_dict = read_dictionary("products.csv", PROD_NUMBER_INDEX)
        current_date_and_time = datetime.now()
    
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            print('Inkom Emporium\n')
            total_quantity = 0
            subtotal = 0
            for row in reader:
                product_number = row[PROD_NUMBER_INDEX]
                product = products_dict[product_number]
                name = product[NAME_INDEX]
                price = float(product[PRICE_INDEX])
                quantity = int(row[QUANTITY_INDEX])
                total_quantity += quantity
                subtotal += (price * quantity)
                print(f'{name}: {quantity} @ {price}')

            sales_tax = subtotal * .06
            grand_total = subtotal + sales_tax
            print(f'\nNumber of Items: {total_quantity}')
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales Tax: {sales_tax:.2f}')
            print(f'Total: {grand_total:.2f}\n')

            print('Thank you for shopping at the Inkom Emporium.')
            print(f'{current_date_and_time:%c}')
            
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")
    except (KeyError) as error:
        print(f"Error: unkown product ID in the request.csv file {error}")



def read_dictionary(filename, key_column_index):
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