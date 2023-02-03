with open('hr_system.txt') as hr_file:
    for line in hr_file:
        clean_line = line.strip()
        parts = clean_line.split(' ')
        names = parts[0]
        id_numbers = parts[1]
        titles = parts[2]
        salaries = float(parts[3])

        if titles.lower() == 'engineer':
            print(f'{names} (ID: {id_numbers}), {titles} - ${(salaries / 24) + 1000:.2f}')
        else:
            print(f'{names} (ID: {id_numbers}), {titles} - ${(salaries / 24):.2f}')