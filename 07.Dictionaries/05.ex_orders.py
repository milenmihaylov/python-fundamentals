products = {}

info = input()
while not info == 'buy':
    product_name, price, quantity = info.split()
    # product_numbers = {'price': float(price), 'quantity': int(quantity)}
    if product_name not in products:
        products[product_name] = {'price': 0.00, 'quantity': 0}
    products[product_name]['price'] = float(price)
    products[product_name]['quantity'] += int(quantity)

    info = input()

for product, numbers in products.items():
    total_price = numbers['price'] * numbers['quantity']
    print(f"{product} -> {total_price:.2f}")
