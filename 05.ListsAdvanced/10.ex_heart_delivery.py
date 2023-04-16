neighborhood = [int(x) for x in input().split('@')]
command = input().split()
cupid_position = 0
while not command[0] == 'Love!':
    length = int(command[1])
    # if command[0] == 'Jump':
    cupid_position += length

    if cupid_position >= len(neighborhood):
        cupid_position = 0

    if neighborhood[cupid_position] > 0:
        neighborhood[cupid_position] -= 2
        if neighborhood[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")

    elif neighborhood[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")

    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

# къдто видиш for жикъл го замени с  лист comprehension
# failed_houses = 0
# mission_failed = False
# for house in neighborhood:
#     if not house == 0:
#         mission_failed = True
#         failed_houses += 1
#
# if not mission_failed:
#     print("Mission was successful.")
# else:
#     print(f"Cupid has failed {failed_houses} places.")

failed_houses = [house for house in neighborhood if not house == 0]
if not failed_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_houses)} places.")
