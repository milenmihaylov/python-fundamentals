import re

text = input()

emojis_list = []
cool_threshold = 1

pattern = r"(?P<symbols>\*\*|\:\:)(?P<emoji>[A-Z][a-z]{2,})(?P=symbols)"
pattern_numbers = r'\d'

valid_emojis = re.finditer(pattern, text)
for emoji in valid_emojis:
    emojis_list.append(emoji.group())

for number in re.findall(pattern_numbers, text):
    cool_threshold *= int(number)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis_list)} emojis found in the text. The cool ones are:")

for emoji in emojis_list:
    coolness = 0
    for i in range(2, len(emoji) - 2):
        coolness += ord(emoji[i])
    if coolness >= cool_threshold:
        print(emoji)



