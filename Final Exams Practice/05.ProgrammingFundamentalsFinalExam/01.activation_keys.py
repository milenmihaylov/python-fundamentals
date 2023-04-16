def contain_str(key: str, string: str):
    if string in key:
        print(f"{key} contains {string}")
    else:
        print("Substring not found!")


def flip(key: str, case, start_i, end_i):
    if case == 'Upper':
        key = key[:start_i] + key[start_i:end_i].upper() + key[end_i:]
    elif case == 'Lower':
        key = key[:start_i] + key[start_i:end_i].lower() + key[end_i:]
    print(key)
    return key


def slicing(key: str, start_i: int, end_i: int):
    key = key[:start_i] + key[end_index:]
    print(key)
    return key


activation_key = input()

commands = input()
while not commands == 'Generate':
    commands = commands.split(">>>")
    command = commands[0]
    if command == 'Contains':
        substring = commands[1]
        contain_str(activation_key, substring)

    elif command == 'Flip':
        case = commands[1]
        start_index = int(commands[2])
        end_index = int(commands[3])
        activation_key = flip(activation_key, case, start_index, end_index)

    elif command == 'Slice':
        start_index = int(commands[1])
        end_index = int(commands[2])
        activation_key = slicing(activation_key, start_index, end_index)

    commands = input()

print(f"Your activation key is: {activation_key}")
