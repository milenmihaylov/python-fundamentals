gifts_list = input().split()
message = input()

while not message == "No Money":

    message_list = message.split()
    command = message_list[0]
    gift = message_list[1]

    if command == "OutOfStock":
        while gift in gifts_list:
            gifts_list[gifts_list.index(gift)] = "None"

    elif "Required" in message_list:
        gift_index = int(message_list[2])
        if 0 <= gift_index < len(gifts_list):
            gifts_list[gift_index] = gift

    elif command == "JustInCase":
        gifts_list[-1:] = gift

    message = input()

for item in gifts_list:
    if not item == 'None':
        print(f"{item}", end=' ')
