def last_char(word, length):
    word = word[length:]
    result = 0
    for ch in word:
        result += ord(ch)
    return result


word_1, word_2 = input().split()
total_sum = 0
words_list = list(zip(word_1, word_2))
for a, b in words_list:
    total_sum += ord(a) * ord(b)

if len(word_1) > len(word_2):
    total_sum += last_char(word_1, len(word_2))
elif len(word_1) < len(word_2):
    total_sum += last_char(word_2, len(word_1))

print(total_sum)
