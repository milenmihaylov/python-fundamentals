text = input()
after_explosion_text = ''
power = 0
for i in range(len(text)):
    if text[i] == '>':
        power += int(text[i + 1])
        after_explosion_text += text[i]
    elif power > 0:
        power -= 1
        continue
    else:
        after_explosion_text += text[i]

print(after_explosion_text)
