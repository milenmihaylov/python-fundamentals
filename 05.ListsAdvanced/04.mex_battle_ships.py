n = int(input())
field = [[int(x) for x in input().split()] for _ in range(n)]

destroyed_ships = 0

for i in input().split():
    attack = i.split('-')
    row = int(attack[0])
    collum = int(attack[1])
    if field[row][collum] > 0:  # проверяваме дали има кораб
        field[row][collum] -= 1  # удряме кораба

        if field[row][collum] == 0:  # проверяваме дали кораба е унищожен
            destroyed_ships += 1  # сумираме унищожените кораби


print(destroyed_ships)
