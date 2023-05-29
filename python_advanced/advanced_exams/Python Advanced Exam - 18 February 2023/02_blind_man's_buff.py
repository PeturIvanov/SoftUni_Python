rows, columns = [int(x) for x in input().split()]

field = []
my_pos = []

touched_players = 0
moves_made = 0

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1)  # right
}

for row in range(rows):
    field.append(input().split())

    if "B" in field[row]:
        my_pos = [row, field[row].index("B")]
        field[my_pos[0]][my_pos[1]] = "-"


while True:
    command = input()
    if command == "Finish" or touched_players == 3:
        break

    r = my_pos[0] + directions[command][0]
    c = my_pos[1] + directions[command][1]

    if 0 <= r < rows and 0 <= c < columns and field[r][c] != "O":
        if field[r][c] == "-":
            moves_made += 1

        elif field[r][c] == "P":
            moves_made += 1
            touched_players += 1
            field[r][c] = "-"
    else:
        continue

    my_pos = [r, c]

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves_made}")
