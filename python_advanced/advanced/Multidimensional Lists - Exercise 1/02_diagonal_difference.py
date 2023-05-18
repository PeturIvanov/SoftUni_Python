rows = int(input())
column = rows

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    primary_diagonal.append(matrix[i][i])

for i in range(rows):
    secondary_diagonal.append(matrix[i][column - 1])
    column -= 1

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
