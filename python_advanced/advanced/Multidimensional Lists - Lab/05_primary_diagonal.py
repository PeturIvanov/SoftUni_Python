n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

total_sum = 0
for index in range(n):
    total_sum += matrix[index][index]

print(total_sum)