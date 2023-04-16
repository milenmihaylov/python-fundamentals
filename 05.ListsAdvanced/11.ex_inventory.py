inventory = input().split(', ')
commands = input().split(' - ')
command = commands[0]
while not command == 'Craft!':
    item = commands[1]
    if command == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif command == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif command == "Combine Items":
        temp_list = item.split(":")
        old_item = temp_list[0]
        new_item = temp_list[1]
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)

    elif command == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    commands = input().split(' - ')
    command = commands[0]


print(', '.join(inventory))
