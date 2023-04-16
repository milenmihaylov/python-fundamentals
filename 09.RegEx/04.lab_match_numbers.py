import re

text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
valid_numbers = re.finditer(pattern, text)
for number in valid_numbers:
    print(f"{number.group()}", end=' ')
