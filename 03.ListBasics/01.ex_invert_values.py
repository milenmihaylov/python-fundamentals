string_numbers = input()
list_numbers = string_numbers.split()
list_int = []
for i in list_numbers:
    number = int(i)
    list_int.append(number * (-1))

print(list_int)

