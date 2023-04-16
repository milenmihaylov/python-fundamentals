line_1 = input().split()
line_2 = input().split()
line_3 = input().split()


def won_player(line, index):  # which player has won
    if line[index] == '1':
        print("First player won")
    elif line[index] == '2':
        print("Second player won")
    elif line[index] == '0':
        print('Draw!')


# patterns:
game_finished = False

# columns
for i in range(3):
    if line_1[i] == line_2[i] and line_1[i] == line_3[i] and line_2[i] == line_3[i]:
        won_player(line_1, i)
        game_finished = True
        break

# rows
if line_1[0] == line_1[1] == line_1[2] and not game_finished:
    won_player(line_1, 0)
    game_finished = True
elif line_2[0] == line_2[1] == line_2[2] and not game_finished:
    won_player(line_2, 0)
    game_finished = True
elif line_3[0] == line_3[1] == line_3[2] and not game_finished:
    won_player(line_3, 0)
    game_finished = True

# diagonals
if (line_1[0] == line_2[1] == line_3[2] or line_1[2] == line_2[1] == line_3[0]) and not game_finished:
    won_player(line_2, 1)
    game_finished = True

if not game_finished:
    print("Draw!")
