def add(card: str):
    if card in all_cards:
        deck.append(card)
    else:
        print("Card not found.")


def insert(card: str, index: int):
    if card in all_cards and (0 <= index < len(deck) or abs(index) <= len(deck)):
        deck.insert(index, card)
    else:
        print("Error!")


def remove(card: str):
    if card in deck:
        deck.remove(card)
    else:
        print("Card not found.")


def swap(card_1: str, card_2: str):
    index_1 = deck.index(card_1)
    index_2 = deck.index(card_2)
    deck[index_1], deck[index_2] = deck[index_2], deck[index_1]


all_cards = input().split(':')
deck = []
commands = input().split()
while not commands[0] == 'Ready':
    if commands[0] == 'Add':
        add(commands[1])

    elif commands[0] == 'Insert':
        insert(commands[1], int(commands[2]))

    elif commands[0] == "Remove":
        remove(commands[1])

    elif commands[0] == 'Swap':
        swap(commands[1], commands[2])

    elif commands[0] == 'Shuffle':
        deck.reverse()

    commands = input().split()

print(' '.join(deck))
