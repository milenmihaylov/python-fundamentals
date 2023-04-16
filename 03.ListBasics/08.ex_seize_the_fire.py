level_of_fire = input()
amount_of_water = int(input())

fires_list = level_of_fire.split('#')
effort = 0
total_fire = 0
print("Cells:")

for fire in fires_list:
    fire_lst = fire.split(' = ')
    type_of_fire = fire_lst[0]
    value_of_cell = int(fire_lst[1])
    if (type_of_fire == 'High' and 81 <= value_of_cell <= 125) or (
            type_of_fire == 'Medium' and 51 <= value_of_cell <= 80) or (
            type_of_fire == 'Low' and 1 <= value_of_cell <= 50):
        if amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell
            effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            print(f" - " + str(value_of_cell))
    else:
        continue

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
