rows, columns = [int(x) for x in input().split()]
matrix = [[int(n) for n in input().split()] for _ in range(rows)]

max_sum = float('-inf')

max_sub_matrix = []

for i in range(rows - 2):

    for j in range(columns - 2):
        sub_matrix = []
        sum_of_sub_matrix = 0
        for row in range(3):
            elements_of_sub_matrix = []

            for column in range(3):
                elements_of_sub_matrix.append(matrix[i + row][j + column])

            sum_of_sub_matrix += sum(elements_of_sub_matrix)
            sub_matrix.append(elements_of_sub_matrix)

        if sum_of_sub_matrix > max_sum:
            max_sum = sum_of_sub_matrix
            max_sub_matrix = sub_matrix

print(f"Sum = {max_sum}")
for el in max_sub_matrix:
    print(*el)
