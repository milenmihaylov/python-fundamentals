command = input()
bakery = {}
while not command == 'statistics':
    key, value = command.split(': ')
    if key not in bakery:
        bakery[key] = 0
    bakery[key] += int(value)
    command = input()

print("Products in stock:")
for key, value in bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")
