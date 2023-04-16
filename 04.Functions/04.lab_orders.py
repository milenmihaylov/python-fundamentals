def order(item, quantity):
    item_price = 0
    if item == 'coffee':
        item_price = 1.50
    elif item == 'water':
        item_price = 1
    elif item == 'coke':
        item_price = 1.40
    elif item == 'snacks':
        item_price = 2

    total_price = item_price * quantity
    return total_price


print(f"{order(input(), int(input())):.2f}")
