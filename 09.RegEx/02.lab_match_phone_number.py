import re

text = input()
pattern = r'(\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b)'

phone_numbers = re.finditer(pattern, text)
print(', '.join([phone.group() for phone in phone_numbers]))
