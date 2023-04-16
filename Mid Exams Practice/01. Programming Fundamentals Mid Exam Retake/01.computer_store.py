parts_prices = []
while True:
    price = input()
    if price == 'special':
        discount = 0.1
        break
    elif price == 'regular':
        discount = 0
        break
    elif float(price) < 0:
        print("Invalid price!")
    else:
        parts_prices.append(float(price))

price_without_tax = sum(parts_prices)
taxes = sum([x * 0.2 for x in parts_prices])
total_price = (price_without_tax + taxes) * (1 - discount)

if total_price > 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print('-----------')
    print(f"Total price: {total_price:.2f}$")
