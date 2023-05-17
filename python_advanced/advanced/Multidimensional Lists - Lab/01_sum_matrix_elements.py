rows, columns = [int(x) for x in input().split(", ")]

matrix = []

total_sum = 0

for rows in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    total_sum += sum(inner_list)
    matrix.append(inner_list)

print(f"{total_sum}\n{matrix}")
