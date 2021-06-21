rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

print(matrix)

