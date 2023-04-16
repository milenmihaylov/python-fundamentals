# да се опитам отново
# judge: 50/100

n = int(input())
maze = [input() for _ in range(n)]

kate_position = []
for row in range(len(maze)):
    for collum in range(len(maze[row])):
        if maze[row][collum] == 'k':
            kate_position = [row, collum]
            break

    if len(kate_position) == 2:
        break


previous_positions = []

while True:
    row = kate_position[0]
    collum = kate_position[1]

    if maze[row - 1][collum] == ' ' and not [row - 1,collum] in previous_positions:
        previous_positions.append([row, collum])
        kate_position = [row - 1, collum]

    elif maze[row + 1][collum] == ' ' and not [row + 1,collum] in previous_positions:
        previous_positions.append([row, collum])
        kate_position = [row + 1, collum]

    elif maze[row][collum - 1] == ' ' and not [row, collum -1] in previous_positions:
        previous_positions.append([row, collum])
        kate_position = [row, collum - 1]

    elif maze[row][collum + 1] == ' ' and not [row, collum + 1] in previous_positions:
        previous_positions.append([row, collum])
        kate_position = [row, collum + 1]

    else:
        print("Kate cannot get out")
        kate_got_out = False
        break

    if kate_position[row] == n - 1 or kate_position[row] == 0 or kate_position[collum] == 0 or \
            kate_position[collum] == n - 1:
        print(f"Kate got out in {len(previous_positions) + 1} moves")
        break
