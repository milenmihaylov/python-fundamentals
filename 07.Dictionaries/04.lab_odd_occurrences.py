words = [word.lower() for word in input().split()]
elements = {}
for el in words:
    if el not in elements:
        elements[el] = 0
    elements[el] += 1

for el in elements:
    if not elements[el] % 2 == 0:
        print(el, end=' ')
