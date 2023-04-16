import re

pattern_star = r'[sStTaArR]'
pattern_planet = r'(?P<name>(?<=\@)[A-Za-z]+)[^@\!\:\>\-]*:(?P<population>\d+)[^@\!\:\>\-]*!(?P<attack>[A|D])![' \
                 r'^@\!\:\>\-]*->(?P<soldiers>\d+)'

attacked_planets = []
destroyed_planets = []

number_of_messages = int(input())

for _ in range(number_of_messages):
    message = input()
    decryption_key_count = len(re.findall(pattern_star, message))
    decrypted_message = ''

    for ch in message:
        decrypted_message += chr(ord(ch) - decryption_key_count)

    valid_planet = re.finditer(pattern_planet, decrypted_message)
    for planet in valid_planet:
        current_planet = planet.groupdict()
        if current_planet['attack'] == 'A':
            attacked_planets.append(current_planet['name'])
        elif current_planet['attack'] == 'D':
            destroyed_planets.append(current_planet['name'])


print(f"Attacked planets: {len(attacked_planets)}")
attacked_planets.sort()
for planet in attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
destroyed_planets.sort()
for planet in destroyed_planets:
    print(f"-> {planet}")
