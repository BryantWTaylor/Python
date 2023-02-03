with open('hr_system.txt') as hr_info:
    for line in hr_info:
        clean_line = line.strip()
        parts = clean_line.split('')

        names = parts[0]
        id_numbers = parts[1]
        job_titles = parts[2]
        salaries = float(parts[3])
        
        if job_titles.lower() == 'engineer':
            print(f'{names} ({id_numbers}), {job_titles} - ${(salaries / 24) + 1000:.2f}')
        else:
            print(f'{names} ({id_numbers}), {job_titles} - ${salaries / 24:.2f}')