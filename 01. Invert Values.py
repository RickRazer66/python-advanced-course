numbers = input()
received_numbers = numbers.split()
opposite_numbers = []

for i in received_numbers:
    i = int(i)
    i = i * (-1)
    opposite_numbers.append(i)
print(opposite_numbers)