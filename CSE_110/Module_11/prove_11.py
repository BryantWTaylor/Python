with open("life-expectancy.csv") as life_file:
    lowest_expectancy = 1000
    highest_expectancy = -1
    life_file = life_file.readlines()[1:]

    for line in life_file:
        clean_line = line.strip()
        parts = clean_line.split(',')
        countries = parts[0]
        years = int(parts[2])
        expectancies = float(parts[3])
    
        if expectancies > highest_expectancy:
            highest_expectancy = expectancies
        
        if expectancies < lowest_expectancy:
            lowest_expectancy = expectancies
    
    print(f'The lowest life expectancy is: {lowest_expectancy}')
    print(f'The highest life expectancy is: {highest_expectancy}')

