def upper(email: str, index: int):
    email = email[:index] + email[index].upper() + email[index + 1:]
    print(email)
    return email


def lower(email: str, index: int):
    email = email[:index] + email[index].lower() + email[index + 1:]
    print(email)
    return email


def insert(email: str, index: int, char: str):
    email = email[:index] + char + email[index:]
    print(email)
    return email


def change(email: str, char: str, value: int):
    ascii_value = ord(char) + value
    email = email.replace(char, chr(ascii_value))
    print(email)
    return email


def validation(email: str):
    upper_case = False
    lower_case = False
    one_digit = False
    valid_char = True

    if len(email) < 6:
        print("Email must be at least 6 characters long!")

    for ch in email:
        if not ch.isalnum() and not ch == '@':
            valid_char = False
        if ch.isupper():
            upper_case = True
        elif ch.islower():
            lower_case = True
        elif ch.isdigit():
            one_digit = True

    if not valid_char:
        print("Email must consist only of letters, digits and @!")

    if not upper_case:
        print("Email must consist at least one uppercase letter!")
    if not lower_case:
        print("Email must consist at least one lowercase letter!")
    if not one_digit:
        print("Email must consist at least one digit!")


email = input()

commands = input()
while not commands == 'Valid':
    if commands == 'Validation':
        validation(email)
    else:
        commands = commands.split()
        command = commands[0]
        if command == 'Upper':
            index = int(commands[1])
            email = upper(email, index)

        elif command == 'Lower':
            index = int(commands[1])
            email = lower(email, index)

        elif command == 'Insert':
            command, index, char = commands
            index = int(index)
            email = insert(email, index, char)

        elif command == 'Change':
            command, char, value = commands
            value = int(value)
            email = change(email, char, value)

    commands = input()
