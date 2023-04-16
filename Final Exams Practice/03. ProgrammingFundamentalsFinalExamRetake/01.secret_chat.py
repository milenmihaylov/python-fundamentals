def insert_space(message: str, index: int):
    message = message[:index] + ' ' + message[index:]
    print(message)
    return message


def reverse(message: str, string: str):
    if string in message:
        message = message.replace(string, '', 1) + string[::-1]
        print(message)
    else:
        print('error')
    return message


def change_all(message: str, substring: str, replacement: str):
    if substring in message:
        message = message.replace(substring, replacement)
        print(message)
    return message


concealed_message = input()

instructions = input()
while not instructions == 'Reveal':
    instructions = instructions.split(':|:')
    instruction = instructions[0]
    if instruction == 'InsertSpace':
        index = int(instructions[1])
        concealed_message = insert_space(concealed_message, index)

    elif instruction == 'Reverse':
        substring = instructions[1]
        concealed_message = reverse(concealed_message, substring)

    elif instruction == 'ChangeAll':
        substring = instructions[1]
        replacement = instructions[2]
        concealed_message = change_all(concealed_message, substring, replacement)

    instructions = input()

print(f"You have a new text message: {concealed_message}")
