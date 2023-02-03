with open('books_and_chapters.txt') as book_file:
    largest = -1
    largest_book = ''
    largest_scripture = ''

    user_scripture = input('What volume of scriptures would you like to learn about? ')

    for line in book_file:
        clean_line = line.strip()
        parts = clean_line.split(':')
        book = parts[0]
        chapters = int(parts[1])
        scripture = parts[2]


        # part 01
    #     print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapters}')
    
    #     if chapters > largest:
    #         largest = chapters # part 2
    #         largest_book = book # part 3
    #         largest_scripture = scripture # part 3

    #     if scripture.lower() == 'book of mormon':
    #         if chapters > largest:
    #             largest = chapters
    #             largest_book = book
        if scripture.lower() == user_scripture.lower():
            if chapters > largest:
                largest = chapters
                largest_book = book

    print(f'The book that has the most chapters in {user_scripture} is {largest_book} with {largest} chapters.')
    # print(f'The book that has the most chapters in the Book of Mormon is {largest_book} with {largest} chapters.')

    # print(f'The book that has the most chapter in the scriptures is {largest_book} in The {largest_scripture} with {largest} chapters.')