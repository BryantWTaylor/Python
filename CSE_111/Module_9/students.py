import csv

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    student_dictionary = read_dictionary("students.csv", I_NUMBER_INDEX)
    
    i_number = input('Please enter an I-Number (xxxxxxxxx): ')
    if i_number in student_dictionary:
        value = student_dictionary[i_number]
        name = value[NAME_INDEX]
        print(name)
    else:
        print('No such student')



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