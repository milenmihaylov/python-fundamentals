input_string = input()

digits_list = [x for x in input_string if x.isdigit()]
non_digits = ''.join([x for x in input_string if not x.isdigit()])

take_list = [int(digits_list[index]) for index in range(len(digits_list)) if index % 2 == 0]
skip_list = [int(digits_list[index]) for index in range(len(digits_list)) if not index % 2 == 0]

result_string = ''
for i in range(len(take_list)):
    m = take_list[i]
    result_string += non_digits[:m]
    non_digits = non_digits[m:]

    n = skip_list[i]
    non_digits = non_digits[n:]

print(result_string)
