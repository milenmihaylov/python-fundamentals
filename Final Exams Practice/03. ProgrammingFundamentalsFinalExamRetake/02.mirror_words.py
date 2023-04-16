import re

text = input()
pattern = r'(?P<symbol>\@|\#)[A-Za-z]{3,}(?P=symbol){2}[A-Za-z]{3,}(?P=symbol)'
possible_words_count = 0
mirror_words = []

matches = re.finditer(pattern, text)
for word in matches:

    possible_words_count += 1
    first_word = word.group()[1:int(len(word.group()) * 0.5 - 1)]
    second_word = word.group()[int(len(word.group()) * 0.5 + 1): -1]

    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

if possible_words_count == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{possible_words_count} word pairs found!")
    if len(mirror_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(', '.join(mirror_words))
