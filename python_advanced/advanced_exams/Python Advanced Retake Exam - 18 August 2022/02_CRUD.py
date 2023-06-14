def next_position(direction):
    global our_position

    r = our_position[0] + directions[direction][0]
    c = our_position[1] + directions[direction][1]

    our_position = [r, c]

    return r, c


def create(*operation_data):
    direction, value = operation_data[0]

    r, c = next_position(direction)

    if table[r][c] == ".":
        table[r][c] = value


def update(*operation_data):
    direction, value = operation_data[0]

    r, c = next_position(direction)

    if table[r][c] != ".":
        table[r][c] = value


def delete(*operation_data):
    direction = operation_data[0][0]

    r, c = next_position(direction)

    table[r][c] = "."


def read(*operation_data):
    direction = operation_data[0][0]

    r, c = next_position(direction)

    if table[r][c] != ".":
        print(table[r][c])


SIZE = 6

table = [input().split() for row in range(SIZE)]

our_position = [int(char) for char in input() if char.isdigit()]

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

commands = {
    "Create": create,
    "Update": update,
    "Delete": delete,
    "Read": read,
}

while True:
    command, *data = input().split(", ")

    if command == "Stop":
        break


    commands[command](data)

print(*[' '.join(row) for row in table], sep="\n")
