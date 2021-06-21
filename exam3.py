commands = input().split()
dict = {}

command = commands[0]
quantity = commands[1]
food = commands[2]


while not command == "Complete":
    if command == "Receive":
        quantity = int(quantity)
        if food in dict:
            pass
        if quantity >= 0:
            dict[food] = quantity
    if command == "Sell":
        if food not in dict:
            print(f"You do not have any {food}")
        else:
            pass
        if dict[quantity] < quantity:
            result = quantity - dict[quantity]
            print(f"There aren't enough {food}. You sold the last {result} of them.")

    commands = input()

print(dict)