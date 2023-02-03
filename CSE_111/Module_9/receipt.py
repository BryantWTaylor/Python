import csv

def main():
    PROD_NUMBER_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    QUANTITY_INDEX = 1


    products_dict = read_dictionary("products.csv", PROD_NUMBER_INDEX)
    print(products_dict)

    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)

        print('Requested Items')
        for row in reader:
            product_number = row[PROD_NUMBER_INDEX]
            product = products_dict[product_number]
            name = product[NAME_INDEX]
            price = product[PRICE_INDEX]
            quantity = row[QUANTITY_INDEX]
            print(f'{name}: {quantity} @ {price}')


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