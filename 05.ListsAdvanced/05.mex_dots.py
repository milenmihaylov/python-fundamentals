# AGAIN!
# def check_dots(board: list, dots_count: int, max_count_of_dots: int):


def horizontal_check(row, collum, board, dots_count, current_position):
    # надясно
    for i in range(collum, len(board)):
        if board[row][collum + i] == '.' and current_position not in checked_positions:
            dots_count += 1
            checked_positions.append([current_position])
            vertical_check(row, collum, board, dots_count, current_position)
        else:
            break

    # наляво
    for I in range(0, collum + 1):
        if board[row][collum - I] == '.' and current_position not in checked_positions:
            dots_count += 1
            checked_positions.append([current_position])
            vertical_check(row, collum, board, dots_count, current_position)
        else:
            break


def vertical_check(row, collum, board, dots_count, current_position):
    for j in range(row, len(board)):
        if board[row + j][collum] == '.' and current_position not in checked_positions:
            dots_count += 1
            checked_positions.append([current_position])
            horizontal_check(row, collum, board, dots_count, current_position)
        else:
            break


n = int(input())
board = [input().split() for _ in range(n)]

checked_positions = []
dots_count = 0
max_count_of_dots = 0

for row in range(len(board)):
    for collum in range(len(board[row])):
        current_position = [row, collum]
        dots_count = 0
        if board[row][collum] == '.' and current_position not in checked_positions:
            dots_count += 1
            checked_positions.append([current_position])
            # хоризонтална проверка
            horizontal_check(row, collum, board, dots_count, current_position)
            # for i in range(row, len(board)):
            #     if board[row + i][collum] == '.' and current_position not in checked_positions:
            #         dots_count += 1
            #         checked_positions.append([current_position])
            #     else:
            #         break

            # вертикална проверка
            vertical_check(row, collum, board, dots_count, current_position)
            if dots_count > max_count_of_dots:
                max_count_of_dots = dots_count

print(max_count_of_dots)



