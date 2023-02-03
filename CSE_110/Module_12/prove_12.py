with open("life-expectancy.csv") as life_file:
    # used for finding the overeall lowest
    lowest_expectancy = 1000
    lowest_year = 0
    lowest_country = ''
    # used for finding the overall highest
    highest_expectancy = -1
    highest_year = 0
    highest_country = ''
    # used for finding the highest in the given year
    year_highest_exp = -1
    year_highest_country = ''
    # used for finding the lowest in the given year
    year_lowest_exp = 1000
    year_lowest_country = ''
    # used to calculate the average life expectancy in the given year
    iterations = 0
    total = 0
    # used to find the lowest for the given country
    country_lowest_exp = 1000
    country_lowest_year = 0
    # used to find the highest for the given country
    country_highest_exp = -1
    country_highest_year = 0
    # used to calcultate the average life expectancy for the given country
    country_total = 0
    country_iterations = 0
    # used to find the life expectancy for the given year and country
    both_exp = 0

    user_year = int(input('\nEnter the year of interest: '))
    user_country = input('Enter a country of interest: ')

    # used to skip the header of the csv file
    life_file = life_file.readlines()[1:]

    for line in life_file:
        clean_line = line.strip()
        parts = clean_line.split(',')
        countries = parts[0]
        years = int(parts[2])
        expectancies = float(parts[3])

# finding the overall lowest
        if expectancies < lowest_expectancy:
            lowest_expectancy = expectancies
            lowest_year = years
            lowest_country = countries

# finding the overall highest
        if expectancies > highest_expectancy:
            highest_expectancy = expectancies
            highest_year = years
            highest_country = countries

# using the given year
        if years == user_year:
            # finding the average
            total = expectancies + total
            iterations = iterations + 1
            # finding the lowest
            if expectancies < year_lowest_exp:
                year_lowest_exp = expectancies
                year_lowest_country = countries
            # finding the highest
            if expectancies > year_highest_exp:
                year_highest_exp = expectancies
                year_highest_country = countries
            # finding the life expectancy for the user given year and country
            if user_country.lower() == countries.lower():
                both_exp = expectancies

# using the given country
        if countries.lower() == user_country.lower():
            # country average life expectancy
            country_total = expectancies + country_total
            country_iterations = country_iterations + 1
            # finding the lowest life expectancy for the given country
            if expectancies < country_lowest_exp:
                country_lowest_exp = expectancies
                country_lowest_year = years
            # finding the highest life expectancy for the given country
            if expectancies > country_highest_exp:
                country_highest_exp = expectancies
                country_highest_year = years

    print(
        f'\nThe overall lowest life expectancy is: {lowest_expectancy} from {lowest_country} in {lowest_year}.')
    print(
        f'The overall highest life expectancy is: {highest_expectancy} from {highest_country} in {highest_year}.')

    print(f'\nFor the year {user_year}:')
    print(
        f'The average life expectancy across all countries was {total / iterations:.2f}.')
    print(
        f'The lowest life expectancy was in {year_lowest_country} with {year_lowest_exp}.')
    print(
        f'The highest life expectancy was in {year_highest_country} with {year_highest_exp}.')

    print(f'\nFor the country {user_country.capitalize()}:')
    print(
        f'The overall average life expectancy for {user_country.capitalize()} is {country_total / country_iterations:.2f}.')
    print(
        f'The lowest life expectancy for {user_country.capitalize()} was in {country_lowest_year} with {country_lowest_exp}.')
    print(
        f'The highest life expectancy for {user_country.capitalize()} was in {country_highest_year} with {country_highest_exp}.')

    print(
        f'\nThe life expectancy for {user_country.capitalize()} in {user_year} is {both_exp}.')
    print()
