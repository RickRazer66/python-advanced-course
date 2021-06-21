lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shield_count = 0

for games in range(1, lost_fight_count + 1):
    if lost_fight_count % 2 == 0:
        expenses += helmet_price
    if lost_fight_count % 3 ==0:
        expenses += sword_price

print(expenses)
