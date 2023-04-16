integers_list = input().split()
count_of_numbers_to_remove = int(input())

for index in range(len(integers_list)):
    integers_list[index] = int(integers_list[index])

for _ in range(count_of_numbers_to_remove):
    integers_list.remove(min(integers_list))

for index in range(len(integers_list)):
    integers_list[index] = str(integers_list[index])

print(", ".join(integers_list))

integers_1_list = [int(x) for x in integers_list]

print(', '.join(str(x) for x in integers_1_list))
