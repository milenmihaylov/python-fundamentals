n = int(input())
# for number in range(1, n + 1):
#     str_number = str(number)
#     sum_digits = 0
#     for digit in str_number:
#         digit = int(digit)
#         sum_digits += digit
#     if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
#         print(f"{number} -> True")
#     else:
#         print(f"{number} -> False")

for num in range(1, n + 1):
    sum_digits = 0
    digits = num
    while digits > 0:
        sum_digits += digits % 10
        digits = digits // 10
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
