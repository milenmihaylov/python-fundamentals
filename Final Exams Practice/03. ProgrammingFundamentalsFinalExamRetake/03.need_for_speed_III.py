def drive(car: str, distance: int, fuel: int):
    if cars[car]['fuel'] >= fuel:
        cars[car]['fuel'] -= fuel
        cars[car]['mileage'] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)
    else:
        print("Not enough fuel to make that ride")


def refuel(car: str, fuel: int):
    if (cars[car]['fuel'] + fuel) <= 75:
        cars[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")
    else:
        litters_refiled = 75 - cars[car]['fuel']
        cars[car]['fuel'] = 75
        print(f"{car} refueled with {litters_refiled} liters")


def revert(car: str, kilometers:int):
    cars[car]['mileage'] -= kilometers
    if cars[car]['mileage'] < 10000:
        cars[car]['mileage'] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


cars = {}

number_of_cars = int(input())
for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

commands = input()
while not commands == "Stop":
    commands = commands.split(" : ")
    if commands[0] == 'Drive':
        command, car, distance, fuel = commands
        distance = int(distance)
        fuel = int(fuel)
        drive(car, distance, fuel)

    elif commands[0] == 'Refuel':
        command, car, fuel = commands
        fuel = int(fuel)
        refuel(car, fuel)

    elif commands[0] == 'Revert':
        command, car, kilometers = commands
        kilometers = int(kilometers)
        revert(car, kilometers)

    commands = input()

for car, numbers in sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0])):
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
