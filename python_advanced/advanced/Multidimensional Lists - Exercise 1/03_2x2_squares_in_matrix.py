rows, columns = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

counter = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        current_el = matrix[i][j]
        next_el = matrix[i][j + 1]
        bottom_el = matrix[i + 1][j]
        diagonal_el = matrix[i + 1][j + 1]

        elements = f"{current_el}{next_el}{bottom_el}{diagonal_el}"
        combination = current_el * 4
        if elements == combination:
            counter += 1

print(counter)
