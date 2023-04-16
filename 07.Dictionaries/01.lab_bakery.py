elements = input().split()

bakery = {}
for index in range(0, len(elements), 2):
    # keys.append(line_list[index])
    # values.append(int(line_list[index + 1]))
    key = elements[index]
    value = elements[index + 1]
    bakery[key] = int(value)

print(bakery)
