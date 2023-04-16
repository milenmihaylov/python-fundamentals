import string
number = int(input())

for i in range(number):
    letter_1 = string.ascii_letters[i]
    for j in range(number):
        letter_2 = string.ascii_letters[j]
        for l in range(number):
            letter_3 = string.ascii_letters[l]
            print(letter_1 + letter_2 + letter_3)



