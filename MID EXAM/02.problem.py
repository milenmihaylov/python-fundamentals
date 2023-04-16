def join(genre: str):
    if genre not in genres_list:
        genres_list.append(genre)


def drop(genre: str):
    if genre in genres_list:
        genres_list.remove(genre)


def replace(old_genre: str, new_genre: str):
    if old_genre in genres_list and new_genre not in genres_list:
        # може да даде грешка ако има повтарящи се жанрове
        genres_list.insert(genres_list.index(old_genre), new_genre)
        genres_list.remove(old_genre)


genres_list = input().split(' | ')
commands = input().split()
while not commands[0] == 'Stop!':
    if commands[0] == 'Join':
        join(commands[1])

    elif commands[0] == 'Drop':
        drop(commands[1])

    elif commands[0] == "Replace":
        replace(commands[1], commands[2])

    commands = input().split()

print(' '.join(genres_list))
