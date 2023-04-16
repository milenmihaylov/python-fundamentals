text = input().replace(' ', '')
char_dict = {}
for ch in text:
    if ch not in char_dict:
        char_dict[ch] = 0
    char_dict[ch] += 1

for char, occurrences in char_dict.items():
    print(f"{char} -> {occurrences}")


''' with list:
text = input().replace(' ', '')
text_unique = []
for ch in text:
    if ch not in text_unique:
        text_unique.append(ch)

for el in text_unique:
    occurrences = text.count(el)
    print(f"{el} -> {occurrences}")
'''