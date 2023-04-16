def decipher_ch(word):
    character_code = ''.join([ch for ch in word if ch.isdigit()])
    deciphered_code = chr(int(character_code))
    deciphered_characters = word.replace(character_code, deciphered_code)

    return deciphered_characters


def switch_letters(word):
    if len(word) > 2:
        deciphered_word = word[0] + word[-1] + word[2:-1] + word[1]
        return deciphered_word
    else:
        return word


secret_message = input().split()
broken_message = [switch_letters(decipher_ch(word)) for word in secret_message]

print(' '.join(broken_message))
