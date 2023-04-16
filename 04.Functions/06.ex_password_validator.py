def password_validator(password):
    valid = True
    if not 6 <= len(password) <= 10:
        valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        valid = False
        print("Password must consist only of letters and digits")
    # for index in password:
    #     if index not in ascii_letters:
    #         if index in digits:
    #             digit += 1
    #         else:
    #             while not special_symbol:
    #                 valid = False
    #                 print("Password must consist only of letters and digits")
    #                 special_symbol = True
    # if digit < 2:
    #     valid = False
    #     print("Password must have at least 2 digits")
    digit_counter = [x for x in symbol_list if x.isdigit()]
    if len(digit_counter) < 2:
        valid = False
        print("Password must have at least 2 digits")
    if valid:
        print("Password is valid")


password = input()
symbol_list = ' '.join(password)
password_validator(password)
