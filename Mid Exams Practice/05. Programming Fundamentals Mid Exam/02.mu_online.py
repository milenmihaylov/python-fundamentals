health = 100
bitcoins = 0

room_count = 0
quest = True

dungeons_rooms = input().split('|')
for room in dungeons_rooms:
    x = room.split()
    command = x[0]
    number = int(x[1])
    room_count += 1

    if command == 'potion':
        # potion(health, number)
        if health + number > 100:
            healed_amount = 100 - health
            health = 100
        else:
            health += number
            healed_amount = number
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == 'chest':
        #  chest(bitcoins, number)
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        monster = command
        attack = number
        # fight(health, monster, attack, room_count)
        if health > attack:
            health -= attack
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_count}")
            quest = False

    if not quest:
        break

if quest:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
