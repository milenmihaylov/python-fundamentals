working_day_events = input().split('|')
energy = 100
coins = 100
bankrupt = False

for each_event in working_day_events:
    event_list = each_event.split('-')
    event = event_list[0]
    number = int(event_list[1])

    if event == 'rest':
        if energy + number > 100:
            energy = 100
            gained_energy = 100 - energy
        else:
            energy += number
            gained_energy = number
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if number < coins:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            bankrupt = True
            break

if not bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
