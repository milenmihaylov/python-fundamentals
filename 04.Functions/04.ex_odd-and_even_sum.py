def even_and_odd_sum():
    number = input()
    even_sum = 0
    odd_sum = 0
    for digit in number:
        int_digit = int(digit)
        if int_digit % 2 == 0:
            even_sum += int_digit
        else:
            odd_sum += int_digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(even_and_odd_sum())
