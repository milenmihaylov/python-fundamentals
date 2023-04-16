def check_right(board, row, collum):
    if collum + 1 < len(board) and board[row][collum + 1] == '.' and [row, collum + 1] not in checked_positions:
        return True


def check_left(board, row, collum):
    if collum - 1 >= 0 and board[row][collum - 1] == '.' and [row, collum - 1] not in checked_positions:
        return True


def check_up(board, row, collum):
    if row - 1 >= 0 and board[row -1][collum] == '.' and [row -1, collum] not in checked_positions:
        return True


def check_down(board, row, collum):
    if row + 1 >= 0 and board[row +1][collum] == '.' and [row +1, collum] not in checked_positions:
        return True


n = int(input())
board = [input().split() for _ in range(n)]

board_size = len(board)
max_count_of_dots = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == '.':
            checked_positions = []
            row = i
            collum = j
            dots_count = 0

            while True:
                if not board[row][collum] == '.':
                    break
                elif check_right(board, row, collum):
                    collum += 1
                    checked_positions.append([row, collum])
                elif check_left(board, row, collum):
                    collum -= 1
                    checked_positions.append([row, collum])
                elif check_up(board, row, collum):
                    row -= 1
                    checked_positions.append([row, collum])
                elif check_down(board, row, collum):
                    row += 1
                else:
                    board[row][collum] = '-'
                    checked_positions = []
                    dots_count += 1
                    row = i
                    collum = j
                    if dots_count > max_count_of_dots:
                        max_count_of_dots = dots_count


print(max_count_of_dots)