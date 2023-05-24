from collections import deque


def spread_bunnies():
    for row in range(rows):
        for col in range(columns):
            if field[row][col] == "B":
                bunny_positions.append([row, col])

    while bunny_positions:
        bunny_position = bunny_positions.popleft()
        for direction in directions.values():
            bunny_row = bunny_position[0] + direction[0]
            bunny_col = bunny_position[1] + direction[1]
            if 0 <= bunny_row < rows and 0 <= bunny_col < columns:
                if field[bunny_row][bunny_col] == ".":
                    field[bunny_row][bunny_col] = "B"


rows, columns = [int(x) for x in input().split()]

field = []
player_pos = []

bunny_positions = deque()

directions = {
    "U": (-1, 0),  # up
    "D": (1, 0),  # down
    "L": (0, -1),  # left
    "R": (0, 1),  # right
}

for row in range(rows):
    field.append(list(input()))
    if "P" in field[row]:
        player_pos = [row, field[row].index("P")]
        field[player_pos[0]][player_pos[1]] = "."

win = False

for command in input():
    r = player_pos[0] + directions[command][0]
    c = player_pos[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < columns):
        spread_bunnies()
        win = True
        break

    if field[r][c] == ".":
        player_pos = [r, c]
        spread_bunnies()

    elif field[r][c] == "B":
        player_pos = [r, c]
        spread_bunnies()
        break

    if field[player_pos[0]][player_pos[1]] == "B":
        break

print(*["".join(el) for el in field], sep="\n")

if win:
    print(f"won: {' '.join(str(x) for x in player_pos)}")
else:
    print(f"dead: {' '.join(str(x) for x in player_pos)}")
