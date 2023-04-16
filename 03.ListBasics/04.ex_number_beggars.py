integer_string = input()
integer_str_list = integer_string.split(', ')
integer_list = []
beggars_count = int(input())

for number in integer_str_list:
    integer_list.append(int(number))

sum_list = []
for _ in range(beggars_count):
    if integer_list:
        sum_list.append(integer_list[0])
        integer_list.pop(0)
    else:
        sum_list.append(0)

while integer_list:
    for index in range(beggars_count):
        sum_list[index] += integer_list[0]
        integer_list.pop(0)
        if not len(integer_list):
            break

print(sum_list)
