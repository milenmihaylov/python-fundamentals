from string import ascii_lowercase


def first_operation(letter: str, number: int):
    if letter.isupper():
        position = int(ascii_lowercase.index(letter.lower()) + 1)
        number /= position
    else:
        position = int(ascii_lowercase.index(letter.lower()) + 1)
        number *= position
    return number


def second_operation(letter: str, number: int):
    if letter.isupper():
        position = int(ascii_lowercase.index(letter.lower()) + 1)
        number -= position
    else:
        position = int(ascii_lowercase.index(letter.lower()) + 1)
        number += position
    return number


strings_list = input().split()
total_sum = 0
for string in strings_list:
    first_letter = string[0]
    last_letter = string[-1]

    number = first_operation(first_letter, int(string[1:-1]))
    total_sum += second_operation(last_letter, number)

print(f"{total_sum:.2f}")
