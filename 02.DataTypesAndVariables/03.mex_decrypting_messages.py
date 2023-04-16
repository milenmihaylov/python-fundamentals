key = int(input())
n = int(input())
decrypted_message = ''
for i in range(n):
    letter = ord(input())
    decrypted_letter = chr(letter + key)
    decrypted_message += decrypted_letter

print(decrypted_message)
