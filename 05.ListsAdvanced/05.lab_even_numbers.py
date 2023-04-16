string_numbers = input().split(', ')
print([i for i in range(len(string_numbers)) if int(string_numbers[i]) % 2 == 0])
