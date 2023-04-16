tank_capacity = 255
n = int(input())
water_in_tank = 0
for i in range(n):
    liters = int(input())
    if liters + water_in_tank > tank_capacity:
        print("Insufficient capacity!")
        continue
    else:
        water_in_tank += liters

print(water_in_tank)
