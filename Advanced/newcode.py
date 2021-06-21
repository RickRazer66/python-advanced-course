quantity_of_food_for_day = int(input())

orders = input().split()
queue = []
max_v = 0

for order in orders:
    order_as_int = int(order)
    queue.append(order)
    if order_as_int > max_v:
        max_v = order_as_int
    if quantity_of_food_for_day >= order_as_int:
        quantity_of_food_for_day -= order_as_int
        queue.pop()

print(max_v)

if len(queue) <= 0:
    print("Orders complete")
else:
    sorted_queue = "".join(queue)
    print(f"Orders left: {sorted_queue}")