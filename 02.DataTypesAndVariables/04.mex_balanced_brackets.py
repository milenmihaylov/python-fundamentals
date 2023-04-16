n = int(input())
balanced = True
char_list = []

for i in range(n):
    character = input()
    if character == '(' or character == ')':
        char_list.append(character)

if len(char_list) % 2 == 0:
    for j in range(len(char_list) - 1):
        if char_list[j] == char_list[j + 1]:
            balanced = False
            break
        else:
            balanced = True
else:
    balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
