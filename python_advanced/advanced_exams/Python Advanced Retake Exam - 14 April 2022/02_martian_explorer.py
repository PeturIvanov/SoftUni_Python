from collections import deque


def is_out(row, col):
    if not 0 <= row < SIZE:
        row = SIZE - 1 if row < 0 else 0

    elif not 0 <= col < SIZE:
        col = SIZE - 1 if col < 0 else 0

    return [row, col]


SIZE = 6

field = []

rover_pos = []

deposits_data = {
    "W": ["Water", 0],
    "M": ["Metal", 0],
    "C": ["Concrete", 0],
}

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

for row in range(SIZE):
    field.append(input().split())

    if "E" in field[row]:
        rover_pos = [row, field[row].index("E")]

commands = deque(input().split(", "))

while commands:
    current_command = commands.popleft()

    r = rover_pos[0] + directions[current_command][0]
    c = rover_pos[1] + directions[current_command][1]

    r, c = is_out(r, c)

    if field[r][c] in deposits_data:

        deposits_data[field[r][c]][1] += 1

        print(f"{deposits_data[field[r][c]][0]} deposit found at ({r}, {c})")

    elif field[r][c] == "R":
        print(f"Rover got broken at ({r}, {c})")
        break

    rover_pos = [r, c]

if deposits_data["W"][1] >= 1 and deposits_data["M"][1] >= 1 and deposits_data["C"][1] >= 1:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
