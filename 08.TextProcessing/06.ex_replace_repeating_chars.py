text = input()
last_letter = ''
new_text = ''
for ch in text:
    if ch == last_letter:
        continue
    else:
        new_text += ch
        last_letter = ch

print(new_text)
