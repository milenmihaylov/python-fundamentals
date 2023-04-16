def fire(section: int, force: int):
    if 0 <= section < len(warship):
        warship[section] -= force
        if warship[section] <= 0:
            print("You won! The enemy ship has sunken.")
            return True


def defend(first_index: int, second_index: int, force: int):
    if 0 <= first_index < len(pirate_ship) and 0 <= second_index < len(pirate_ship):
        # if 0 <= first_index <= second_index <= len(pirate_ship):
        for i in range(first_index, second_index + 1):
            pirate_ship[i] -= force
            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                return True


def repair(section: int, amount: int):
    if 0 <= section < len(pirate_ship):
        pirate_ship[section] += amount
        if pirate_ship[section] > maximum_health_capacity:
            pirate_ship[section] = maximum_health_capacity


def status():
    damaged_sections = 0
    for section in pirate_ship:
        if section < maximum_health_capacity * 0.2:
            damaged_sections += 1
    print(f"{damaged_sections} sections need repair.")


pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
maximum_health_capacity = int(input())

stalemate = True
commands = input().split()
while not commands[0] == "Retire":
    if commands[0] == "Fire":
        index = int(commands[1])
        damage = int(commands[2])
        warship_destroyed = fire(index, damage)
        if warship_destroyed:
            stalemate = False
            break

    elif commands[0] == "Defend":
        start_index = int(commands[1])
        end_index = int(commands[2])
        damage = int(commands[3])
        pirate_ship_destroyed = defend(start_index, end_index, damage)
        if pirate_ship_destroyed:
            stalemate = False
            break

    elif commands[0] == "Repair":
        index = int(commands[1])
        health = int(commands[2])
        repair(index, health)

    elif commands[0] == "Status":
        status()

    commands = input().split()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
