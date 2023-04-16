lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet_count = lost_fights_count // 2
trashed_sword_count = lost_fights_count // 3
trashed_shield_count = lost_fights_count // 6
trashed_armor_count = trashed_shield_count // 2

expenses = trashed_helmet_count * helmet_price + trashed_sword_count * sword_price \
           + trashed_shield_count * shield_price + trashed_armor_count * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")


