rows, column = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

max_sum = float('-inf')
max_sum_el = []

for i in range(rows - 1):
    for j in range(column - 1):
        current_el = matrix[i][j]
        next_el = matrix[i][j + 1]
        bottom_el = matrix[i + 1][j]
        diagonal_el = matrix[i + 1][j + 1]
        total_sum = current_el + next_el + bottom_el + diagonal_el
        if total_sum > max_sum:
            max_sum = total_sum
            max_sum_el = [[current_el, next_el], [bottom_el, diagonal_el]]


for el in max_sum_el:
    print(*el)
print(max_sum)
