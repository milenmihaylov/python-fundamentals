def delivered_ingredients(distributor_name: str, money_spend: float):
    if distributor_name not in distributors:
        distributors[distributor_name] = 0
    distributors[distributor_name] += money_spend


def returned_ingredients(distributor_name: str, money_returned: float):
    if distributor_name in distributors:
        if money_returned == distributors[distributor_name]:
            distributors.pop(distributor_name)
        elif money_returned < distributors[distributor_name]:
            distributors[distributor_name] -= money_returned


def order(client_name: str, money_received: float, total_income: float):
    if client_name not in clients:
        clients[client_name] = 0
    clients[client_name] += money_received
    total_income += money_received
    return total_income


distributors = {}
clients = {}
total_income = 0.0

commands = input()
while not commands == 'End':
    command, name, money = commands.split()
    money = float(money)
    if command == 'Deliver':
        delivered_ingredients(name, money)
    elif command == 'Return':
        returned_ingredients(name, money)
    elif command == 'Sell':
        total_income = order(name, money, total_income)

    commands = input()

for client, money in sorted(clients.items(), key=lambda x: x[0]):
    print(f"{client}: {money:.2f}")
print("-----------")
for distributor, money in sorted(distributors.items(), key=lambda x: x[0]):
    print(f"{distributor}: {money:.2f}")
print("-----------")
print(f"Total Income: {total_income:.2f}")
