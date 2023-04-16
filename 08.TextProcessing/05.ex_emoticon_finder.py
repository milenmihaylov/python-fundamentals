text = input()
for i in range(len(text) -1):
    if text[i] == ':' and text[i+1] != ' ':
        print(text[i] + text[i+1])
