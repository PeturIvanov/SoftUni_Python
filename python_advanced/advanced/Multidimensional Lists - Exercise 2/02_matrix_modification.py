def is_valid(row, col):
    if (0 > row or row > n - 1) or (0 > col or col > n - 1):
        return False
    return True


n = int(input())

matrix = [[int(n) for n in input().split()]for _ in range(n)]

while True:
    command, *data = input().split()
    if command == "END":
        break

    data = [int(x) for x in data]
    row, col, value = data

    if is_valid(row, col):
        if command == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for el in matrix:
    print(*el)

