n = int(input())

field = []
bunny_pos = []
best_path = []
best_path_direction = ""
max_eggs_collected = 0

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

for row in range(n):
    inner_row = input().split()
    if "B" in inner_row:
        bunny_pos = [row, inner_row.index("B")]
    field.append(inner_row)

for direction, positions in directions.items():
    r = bunny_pos[0] + positions[0]
    c = bunny_pos[1] + positions[1]

    eggs_collected = 0
    current_path = []

    while 0 <= r < n and 0 <= c < n:
        if field[r][c] == "X":
            break

        eggs_collected += int(field[r][c])
        current_path.append([r, c])
        r += positions[0]
        c += positions[1]

    if eggs_collected >= max_eggs_collected:
        max_eggs_collected = eggs_collected
        best_path = current_path
        best_path_direction = direction

print(best_path_direction)
print(*best_path, sep="\n")
print(max_eggs_collected)
