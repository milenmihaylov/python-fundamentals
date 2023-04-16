def user_existence(forcebook_dict: dict, user: str):
    for k in forcebook_dict:
        if user in forcebook_dict[k]:
            return k
    return False


def initial_force_side(forcebook_dict: dict, side: str, user: str):
    if not user_existence(forcebook_dict, user):
        forcebook_dict[side].append(user)
        print(f"{force_user} joins the {force_side} side!")

    else:
        k = user_existence(forcebook_dict, user)
        forcebook_dict[k].remove(user)
        forcebook_dict[side].append(user)
        print(f"{user} joins the {side} side!")


forcebook = {}

information = input()
while not information == 'Lumpawaroo':
    if ' | ' in information:
        force_side, force_user = information.split(' | ')
        if force_side not in forcebook:
            forcebook[force_side] = []

        if not user_existence(forcebook, force_user):
            forcebook[force_side].append(force_user)

    elif ' -> ' in information:
        force_user, force_side = information.split(' -> ')
        good = False
        if force_side not in forcebook:
            forcebook[force_side] = []

        initial_force_side(forcebook, force_side, force_user)

    information = input()

for key, value_list in sorted(forcebook.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(value_list) > 0:
        print(f"Side: {key}, Members: {len(value_list)}")
        value_list.sort()
        for person in value_list:
            print(f"! {person}")
