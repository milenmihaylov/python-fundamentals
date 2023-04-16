allowed_quantity = int(input())
total_days = int(input())
day = 1

ornament_set_cost = 2
tree_skirt_cost = 5
tree_garlands_cost = 3
tree_lights_cost = 15

christmas_spirit = 0
total_costs = 0

while total_days > 0:
    if day % 11 == 0:
        allowed_quantity += 2

    if day % 2 == 0:
        christmas_spirit += 5
        total_costs += allowed_quantity * ornament_set_cost

    if day % 3 == 0:
        christmas_spirit += 13
        total_costs += allowed_quantity * tree_skirt_cost
        total_costs += allowed_quantity * tree_garlands_cost

    if day % 5 == 0:
        total_costs += tree_lights_cost * allowed_quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_costs += tree_skirt_cost * 1
        total_costs += tree_garlands_cost * 1
        total_costs += tree_lights_cost * 1

    if total_days == 1 and day % 10 == 0:
        christmas_spirit -= 30

    day += 1
    total_days -= 1

print(f"Total cost: {total_costs}")
print(f"Total spirit: {christmas_spirit}")
