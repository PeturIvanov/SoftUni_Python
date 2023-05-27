size = int(input())
moves = input().split(", ")

field = []
squirrel_pos = []

hazelnuts = 0

for row in range(size):
    field.append(list(input()))
    if "s" in field[row]:
        squirrel_pos = [row, field[row].index("s")]
        field[squirrel_pos[0]][squirrel_pos[1]] = "*"

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

for move in moves:
    r = squirrel_pos[0] + directions[move][0]
    c = squirrel_pos[1] + directions[move][1]

    if not (0 <= r < size and 0 <= c < size):
        print("The squirrel is out of the field.")
        break

    if field[r][c] == "h":
        hazelnuts += 1
        field[r][c] = "*"

    elif field[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

    squirrel_pos = [r, c]


else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")


















