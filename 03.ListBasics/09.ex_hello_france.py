collection_of_items = input()
budget = float(input())
list_collection_of_items = collection_of_items.split('|')

sold_prices_list = []
profit = 0

for item in list_collection_of_items:
    item_type_and_price = item.split('->')
    item_type = item_type_and_price[0]
    item_price = float(item_type_and_price[1])
    if (item_type == 'Clothes' and item_price <= 50.00) or (
            item_type == 'Shoes' and item_price <= 35.00) or (
            item_type == 'Accessories' and item_price <= 20.50):
        if budget >= item_price:
            budget -= item_price
            selling_price = item_price * 1.4
            print(f"{selling_price:.2f}", end=' ')
            sold_prices_list.append(selling_price)
            profit += item_price * 0.4
    else:
        continue

new_budget = budget + sum(sold_prices_list)
print()
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
