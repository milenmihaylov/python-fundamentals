def shoot(index: int, power: int):
    if index in range(len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def add(index: int, power: int):
    if index in range(len(targets)):
        targets.insert(index, power)
    else:
        print("Invalid placement!")


def strike(index: int, radius: int):
    if index >= radius and len(targets) >= index + radius + 1:
        for j in range(index + radius, index - radius - 1, -1):
            targets.pop(j)
    else:
        print("Strike missed!")


targets = [int(x) for x in input().split()]
command = input().split()
while not command[0] == 'End':
    if command[0] == "Shoot":
        shoot(index=int(command[1]), power=int(command[2]))
    elif command[0] == 'Add':
        add(index=int(command[1]), power=int(command[2]))
    elif command[0] == 'Strike':
        strike(index=int(command[1]), radius=int(command[2]))

    command = input().split()

print('|'.join([str(x) for x in targets]))
