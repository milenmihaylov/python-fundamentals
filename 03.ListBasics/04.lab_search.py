n = int(input())
word = input()
strings_list = []
string_with_word_list = []
for i in range(n):
    given_string = input()
    strings_list.append(given_string)
    if word in given_string:
        string_with_word_list.append(given_string)

print(strings_list)
print(string_with_word_list)
