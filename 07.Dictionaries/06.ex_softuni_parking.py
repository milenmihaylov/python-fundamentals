parking_register = {}

for _ in range(int(input())):
    commands = input().split()
    if commands[0] == 'register':
        user = commands[1]
        plate_number = commands[2]
        if user not in parking_register:
            parking_register[user] = plate_number
            print(f"{user} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_register[user]}")

    elif commands[0] == 'unregister':
        user = commands[1]
        if user in parking_register:
            parking_register.pop(user)
            print(f"{user} unregistered successfully")
        else:
            print(f"ERROR: user {user} not found")

for user, plate_number in parking_register.items():
    print(f"{user} => {plate_number}")
