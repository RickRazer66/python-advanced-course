lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shield_count = 0

for lost_fights in range(1, lost_fight_count + 1):
    if lost_fights % 2 == 0:
        expenses += helmet_price
    if lost_fights % 3 ==0:
        expenses += sword_price
    if lost_fights % 2 == 0 and lost_fights % 3 == 0:
        expenses += shield_price
        broken_shield_count += 1
        if broken_shield_count % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
