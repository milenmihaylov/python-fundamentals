budget = float(input())
flour_price = float(input())

pack_of_eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price

cozonac_price = flour_price + pack_of_eggs_price + 0.25 * milk_price
cozonac_count = int(budget // cozonac_price)
colored_eggs = 0

for cozonac in range(1, cozonac_count + 1):
    colored_eggs += 3
    if cozonac % 3 == 0:
        colored_eggs -= cozonac - 2

money_left = budget - (cozonac_count * cozonac_price)
print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
