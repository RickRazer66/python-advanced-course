number_of_cities = int(input())
total_profit = 0

for n in range(1, number_of_cities+1):
    name_of_city = input()
    owners_income = float(input())
    owners_expenses = float(input())
    if n % 3 == 0:
        owners_expenses += owners_expenses/2
    elif n % 5 == 0:
        owners_expenses += owners_income * 0.1
    result = owners_income - owners_expenses
    total_profit += result
    print(f"In {name_of_city} Burger Bus earned {result:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")


