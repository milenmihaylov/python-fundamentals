factor = int(input())
count = int(input())
list_numbers = []
number = 0
while len(list_numbers) < count:
    number += 1
    if number % factor == 0:
        list_numbers.append(number)

print(list_numbers)
