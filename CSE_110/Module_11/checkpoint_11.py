with open("books.txt") as book_file:
    for line in book_file:
        clean_line = line.strip()
        print(clean_line)
