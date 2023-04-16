resource = input()
collection = {}
while not resource == 'stop':
    quantity = int(input())
    if resource not in collection:
        collection[resource] = 0
    collection[resource] += quantity

    resource = input()

for resource, quantity in collection.items():
    print(f"{resource} -> {quantity}")
