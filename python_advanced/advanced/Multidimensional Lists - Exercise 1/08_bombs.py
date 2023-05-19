def is_alive(row, col):
    if 0 >= matrix[row][col]:
        return False

    return True


def detonate_bomb(row_start, row_end, col_start, col_end):
    for row in range(row_start, row_end):
        for col in range(col_start, col_end):

            if is_alive(row, col):
                matrix[row][col] -= bomb_damage


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

bombs_coordinates_data = input().split()


for bom in bombs_coordinates_data:
    i, j = [int(x) for x in bom.split(",")]

    bomb_damage = matrix[i][j]
    if bomb_damage < 0:
        continue

    # Corners
    if i == 0 and j == 0:
        detonate_bomb(0, 2, 0, 2)

    elif i == 0 and j == n - 1:
        detonate_bomb(0, 2, n - 2, n)

    elif i == n - 1 and j == 0:
        detonate_bomb(n - 2, n, 0, 2)

    elif i == n - 1 and j == n - 1:
        detonate_bomb(n - 2, n, n - 2, n)

    #  Upper Wall
    elif i == 0 and (i < j < n - 1):
        detonate_bomb(0, 2, j - 1, j + 2)

    # Left Wall
    elif 0 < i < n - 1 and j == 0:
        detonate_bomb(i - 1, i + 2, 0, 2)

    # Bottom Wall
    elif i == n - 1 and 0 < j < n - 1:
        detonate_bomb(n - 2, n, j - 1, j + 2)

    # Right Wall
    elif 0 < i < n - 1 and j == n - 1:
        detonate_bomb(i - 1, i + 2, j - 1, n)

    # Middle
    else:
        detonate_bomb(i - 1, i + 2, j - 1, j + 2)


alive_cells = [num for el in matrix for num in el if num > 0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for el in matrix:
    print(*el, sep=" ")

