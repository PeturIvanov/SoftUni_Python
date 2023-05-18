rows = int(input())


matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - i - 1])


print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
