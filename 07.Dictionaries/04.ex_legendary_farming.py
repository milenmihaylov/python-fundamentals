def collection(key_materials_dict: dict, junk_materials: dict, material: str, qty: int):
    if material in key_materials_dict:
        key_materials_dict[material] += int(qty)
    else:
        if material not in junk_materials:
            junk_materials[material] = 0
        junk_materials[material] += qty


key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}

collecting = True
while collecting:
    input_materials = input().split()
    for index in range(0, len(input_materials), 2):
        material = input_materials[index + 1].lower()
        quantity = int(input_materials[index])
        collection(key_materials, junk, material, quantity)
        if key_materials['shards'] >= 250:
            print('Shadowmourne obtained!')
            key_materials['shards'] -= 250
            collecting = False
            break

        elif key_materials['fragments'] >= 250:
            print('Valanyr obtained!')
            key_materials['fragments'] -= 250
            collecting = False
            break

        elif key_materials['motes'] >= 250:
            print('Dragonwrath obtained!')
            key_materials['motes'] -= 250
            collecting = False
            break

for material, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{material}: {quantity}")

for material, quantity in sorted(junk.items(), key=lambda x: x[0]):
    print(f"{material}: {quantity}")
