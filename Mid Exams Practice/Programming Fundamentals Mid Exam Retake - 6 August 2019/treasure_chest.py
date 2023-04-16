def loot(treasure_list: list):
    for item in treasure_list:
        if item not in treasure_chest:
            treasure_chest.insert(0, item)


def drop(index: int):
    if (0 <= index < len(treasure_chest)) or (index < 0 and abs(index) <= len(treasure_chest)):
        item = treasure_chest[index]
        treasure_chest.pop(index)
        treasure_chest.append(item)


def steal(how_many: int, list_of_treasures):
    if how_many >= len(list_of_treasures):
        print(', '.join(list_of_treasures))
        list_of_treasures = []
    else:
        print(', '.join(list_of_treasures[(len(list_of_treasures) - how_many):]))
        list_of_treasures = list_of_treasures[:(len(list_of_treasures) - how_many)]

    return list_of_treasures


treasure_chest = [x for x in input().split('|')]

commands = input().split()
while not commands[0] == "Yohoho!":
    if commands[0] == "Loot":
        loot(commands[1:])
    elif commands[0] == "Drop":
        i = int(commands[1])
        drop(i)
    elif commands[0] == "Steal":
        count = int(commands[1])
        treasure_chest = steal(count, treasure_chest)

    commands = input().split()

sum_items_length = sum([len(item) for item in treasure_chest])

if treasure_chest:
    average_gain = sum_items_length / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
