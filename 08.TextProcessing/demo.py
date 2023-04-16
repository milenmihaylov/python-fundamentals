text = input()

rage_message = ''
current_string = ''
current_digit = ''
rage_list = []
last_digit_index = -1
unique_symbols = 0
for index in range(len(text)):
    if text[index].isdigit():
        current_string = text[last_digit_index + 1:index].upper()
        current_digit = text[index]
        if index != len(text) - 1 and text[index + 1].isdigit():
            current_digit += text[index + 1]

        rage_message += current_string * int(current_digit)
        last_digit_index = index

unique_symbols = len(set(rage_message))
print(f"Unique symbols used: {unique_symbols}")
print(rage_message)
