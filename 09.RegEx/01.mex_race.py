import re

participants = input().split(', ')
race = {}
pattern_names = r'[A-Za-z]+'
pattern_numbers = r'\d'

text = input()
while not text == "end of race":
    racer = ''.join(re.findall(pattern_names, text))
    distance = sum(int(num) for num in re.findall(pattern_numbers, text))
    if racer in participants:
        if racer not in race:
            race[racer] = 0
        race[racer] += distance
    text = input()

count = 0
places = ['1st', '2nd', '3rd']
for racer, distance in sorted(race.items(), key=lambda x: -x[1]):
    print(f"{places[count]} place: {racer}")
    count += 1
    if count == 3:
        break
