def jackpot(left_str: str, right_str: str):
    for symbol in winning_symbols:
        jackpot_combo = symbol * 10
        if left_str == jackpot_combo and right_str == jackpot_combo:
            return True
    return False


def winner(left_str: str, right_str: str):
    for symbol in winning_symbols:
        if (symbol * 6) in left_str and (symbol*6) in right_str:
            count = check_next(symbol, left_str, right_str)
            return symbol, count
    return False, False


def check_next(symbol: str, left_str: str, right_str: str):
    count = 6
    for i in range(7,11):
        if (i*symbol) in left_str and (i*symbol) in right_str:
            count += 1
    return count


text = input().replace(',', '')
tickets = text.split()
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    left_half = ticket[:10]
    right_half = ticket[10:]

    if jackpot(left_half, right_half):
        winning_symbol = left_half[0]
        print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
        continue

    winning_symbol, winning_length = winner(left_half, right_half)
    if winning_symbol:
        print(f'ticket "{ticket}" - {winning_length}{winning_symbol}')
        continue
    else:
        print(f'ticket "{ticket}" - no match')
        continue
