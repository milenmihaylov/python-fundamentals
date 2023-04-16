def check_len(password):
    if len(password) in range(6, 11):
        return True

    return False


def check_char(password):
    for char in password:
        if not char.isnumeric():
            if not char.isalpha():
                return False

    return True


def check_digits(password):
    numbers = 0
    for char in password:
        if char.isnumeric():
            numbers += 1

    if numbers >= 2:
        return True
    else:
        return False


def validator(password):
    valid_password = True

    if not check_len(password):
        print("Password must be between 6 and 10 characters")
        valid_password = False
    if not check_char(password):
        print("Password must consist only of letters and digits")
        valid_password = False
    if not check_digits(password):
        print("Password must have at least 2 digits")
        valid_password = False

    if valid_password:
        print("Password is valid")


validator(input())
