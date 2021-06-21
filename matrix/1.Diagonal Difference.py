n = int(input())

matrix = []

main_diagonal = 0
secondary_diagonal = 0

for row in range(n):
    matrix.append([])
    for el in input().split():
        inner_list = matrix[-1]
        inner_list.append(int(el))

for i in range(n):
    main_diagonal += matrix[i][i]

for i in range(n):
    secondary_diagonal += matrix[len(matrix) - 1 - i][i]

print(abs(main_diagonal - secondary_diagonal))