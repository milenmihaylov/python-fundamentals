rooms = int(input())
total_free_chairs = 0
need_chairs = False
for room in range(rooms):
    text = input().split()
    chairs = len(text[0])
    visitors = int(text[1])
    needed_chairs_in_room = (visitors - chairs)
    total_free_chairs += (chairs - visitors)
    if needed_chairs_in_room > 0:
        print(f"{needed_chairs_in_room} more chairs needed in room {room + 1}")
        need_chairs = True
        needed_chairs_in_room = 0


if not need_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
