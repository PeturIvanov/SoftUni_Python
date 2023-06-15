rows, cols = [int(x) for x in input().split(", ")]

field = []

our_pos = []

total_items = 0

for row in range(rows):
    field.append(input().split())

    total_items += len([item for item in field[row] if item != "." and item != "Y"])

    if "Y" in field[row]:
        our_pos = [row, field[row].index("Y")]
        field[row][field[row].index("Y")] = "x"


directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

items_data = {
    "D": ["Christmas decorations", 0],
    "G": ["Gifts", 0],
    "C": ["Cookies", 0]

}

while total_items > 0:
    command = input()

    if command == "End":
        break

    direction, steps = command.split("-")
    steps = int(steps)

    for _ in range(steps):
        r = (our_pos[0] + directions[direction][0]) % rows
        c = (our_pos[1] + directions[direction][1]) % cols

        position = field[r][c]

        if position in items_data:
            items_data[position][1] += 1

            total_items -= 1

        field[r][c] = "x"

        our_pos = [r, c]

        if total_items == 0:
            print("Merry Christmas!")
            break


field[our_pos[0]][our_pos[1]] = "Y"

print("You've collected:")

for item_name, count in items_data.values():
    print(f"- {count} {item_name}")

print('\n'.join(' '.join(r) for r in field))
