numbers_list = input().split(', ')
zeros_list = []
while '0' in numbers_list:
    numbers_list.remove('0')
    zeros_list.append('0')

numbers_list += zeros_list
numbers_int_list = [int(x) for x in numbers_list]
print(numbers_int_list)
