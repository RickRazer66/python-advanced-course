def check_elements_are_equal(row, col, matrix):
    current_element = matrix[row][col]
    next_element_same_row = matrix[row][col+1]
    element_bottom = matrix[row+1][col]
    element_bottom_right = matrix[row+1][col+1]
    if current_element == next_element_same_row == element_bottom == element_bottom_right:
        return True
    return False


rows, cols = [int(el) for el in input().split()]

matrix = []
counter = 0

for row in range(rows):
    matrix.append(input().split())


for i in range(rows-1):
    for j in range(cols-1):
        if check_elements_are_equal(i, j, matrix):
            counter +=1

print(counter)
