rows = int(input())


matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonal = 0
secondary_diagonal = 0

for i in range(rows):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][rows - i - 1]

print(abs(primary_diagonal - secondary_diagonal))
