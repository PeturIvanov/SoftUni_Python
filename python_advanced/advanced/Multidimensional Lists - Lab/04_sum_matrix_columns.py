rows, column = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for column_index in range(column):
    total_sum = 0
    for rows_index in range(rows):
        total_sum += matrix[rows_index][column_index]
    print(total_sum)
