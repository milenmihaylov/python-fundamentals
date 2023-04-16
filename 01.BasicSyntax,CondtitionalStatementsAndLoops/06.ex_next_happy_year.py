current_year = int(input())

while True:
    current_year += 1
    current_year = str(current_year)
    if len(set(current_year)) == len(current_year):
        print(current_year)
        break
    else:
        current_year = int(current_year)
        continue
