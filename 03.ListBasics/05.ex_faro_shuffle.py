deck = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):

    half_size = len(deck) // 2
    first_half_deck = deck[:half_size]  # презаписваш списъка на половин дължина
    second_half_deck = deck[half_size:]

    shuffled_deck = []
    for i in range(half_size):
        shuffled_deck.append(first_half_deck[i])
        shuffled_deck.append(second_half_deck[i])

    deck = shuffled_deck
    # first_half_deck = []
    # second_half_deck = []
    #
    # for i in range(len(deck) // 2):
    #     first_half_deck.append(deck[0])
    #     deck.pop(0)
    # for i in range(len(deck)):
    #     second_half_deck.append(deck[0])
    #     deck.pop(0)
    #
    # for i in range(len(second_half_deck)):
    #     deck.append(first_half_deck[0])
    #     first_half_deck.pop(0)
    #     deck.append(second_half_deck[0])
    #     second_half_deck.pop(0)

print(deck)

