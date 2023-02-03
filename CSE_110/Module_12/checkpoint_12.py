people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_age = 1000
youngest_name = ''

for line in people:
    clean_line = line.strip()
    parts = clean_line.split(' ')
    name = parts[0]
    age = int(parts[1])

    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f'The youngest age is {youngest_age}')
print(f'The youngest person is {youngest_name}')
