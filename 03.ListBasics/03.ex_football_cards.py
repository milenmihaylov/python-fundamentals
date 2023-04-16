a_team = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
b_team = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

cards_list = input().split()
referee_stop = False

for card in cards_list:
    card_info = card.split('-')

    team_name = card_info[0]
    player_number = card_info[1]

    if team_name == 'A' and player_number in a_team:
        a_team.remove(player_number)
    elif team_name == 'B' and player_number in b_team:
        b_team.remove(player_number)

    if len(a_team) < 7 or len(b_team) < 7:
        referee_stop = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if referee_stop:
    print("Game was terminated")
