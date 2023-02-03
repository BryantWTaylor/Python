def display_regular(message):
    print(message)

def display_uppercase(message):
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    new_message = message.lower()
    print(new_message)

user_string = input('What is your message: ')
display_regular(user_string)
display_uppercase(user_string)
display_lowercase(user_string)