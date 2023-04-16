def plunder(city: str, population: int, gold: int):
    target_cities[city]['population'] -= population
    target_cities[city]['gold'] -= gold
    print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
    if target_cities[city]['population'] <= 0 or target_cities[city]['gold'] <= 0:
        target_cities.pop(city)
        print(f"{city} has been wiped off the map!")


def prosper(city: str, gold_added: int):
    if gold_added < 0:
        print("Gold added cannot be a negative number!")
    else:
        target_cities[city]['gold'] += gold_added
        print(f"{gold_added} gold added to the city treasury. {city} now has {target_cities[city]['gold']} gold.")


target_cities = {}

command = input()
while not command == 'Sail':
    city, population, gold = command.split('||')
    if city not in target_cities:
        target_cities[city] = {'population': 0, 'gold': 0}
    target_cities[city]['population'] += int(population)
    target_cities[city]['gold'] += int(gold)

    command = input()

events = input()
while not events == 'End':
    events = events.split('=>')
    if events[0] == 'Plunder':
        event, city, population, gold = events
        population = int(population)
        gold = int(gold)
        plunder(city, population, gold)

    elif events[0] == 'Prosper':
        event, city, gold = events
        gold = int(gold)
        prosper(city, gold)

    events = input()

if len(target_cities) > 0:
    print(f"Ahoy, Captain! There are {len(target_cities)} wealthy settlements to go to:")
    for city, numbers in sorted(target_cities.items(), key=lambda x: (-x[1]['gold'], x[0])):
        print(f"{city} -> Population: {numbers['population']} citizens, Gold: {numbers['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
