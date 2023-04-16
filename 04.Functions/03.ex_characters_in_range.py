def characters():
    char_1 = input()
    char_2 = input()
    char_string = ''
    for i in range(ord(char_1) + 1, ord(char_2)):
        char_string += chr(i) + ' '

    return char_string


print(characters())
