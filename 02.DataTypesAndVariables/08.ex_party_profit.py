party_size = int(input())
days = int(input())
total_coins = 0

for day in range(1, days + 1):
    daily_earnings = 50
    food_per_companion = 2
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    if day % 3 == 0:
        food_per_companion += 3
    if day % 5 == 0:
        daily_earnings += 20 * party_size
        if day % 3 == 0:
            food_per_companion += 2

    food_costs = food_per_companion * party_size
    total_coins += (daily_earnings - food_costs)

member_coins = int(total_coins / party_size)
print(f"{party_size} companions received {member_coins} coins each.")
