numbers_list = input().split()
# numbers_int = [int(x) for x in numbers_list]
chars = input()
message_letter = ''
final_message = ''


for number in numbers_list:
    chars_index = 0
    for digit in number:
        chars_index += int(digit)

    if chars_index > len(chars):
        n = chars_index // len(chars)
        chars_index -= n * len(chars)
    elif chars_index == len(chars):
        chars_index = 0

    message_letter = chars[chars_index]
    final_message += message_letter

    first_half_chars = chars[:chars_index]
    second_half_chars = chars[chars_index + 1:]
    chars = first_half_chars + second_half_chars

print(final_message)
