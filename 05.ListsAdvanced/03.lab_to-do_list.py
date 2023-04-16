notes_list = [0] * 10

command = input()
while not command == 'End':
    importance, task = command.split('-')
    current_index = int(importance) - 1
    notes_list[current_index] = task

    command = input()

print([el for el in notes_list if not el == 0])
