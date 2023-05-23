def move(direction, steps):
    r = my_pos[0] + directions[direction][0] * steps
    c = my_pos[1] + directions[direction][1] * steps

    if (0 <= r < SIZE and 0 <= c < SIZE) and field[r][c] == ".":
        field[my_pos[0]][my_pos[1]] = "."
        field[r][c] = "A"
        return [r, c]

    return [my_pos[0], my_pos[1]]


def shoot(direction):
    r, c = my_pos
    while True:
        r += directions[direction][0]
        c += directions[direction][1]

        if not (0 <= r < SIZE and 0 <= c < SIZE):
            return

        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]


SIZE = 5

field = []
my_pos = []

total_targets = 0
targets_hit_pos = []

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

for row in range(SIZE):
    field.append(input().split())
    if "A" in field[row]:
        my_pos = [row, field[row].index("A")]

    total_targets += field[row].count("x")


for _ in range(int(input())):
    command = input().split()

    if command[0] == "shoot":
        target_shoot = shoot(command[1])
        if target_shoot:
            targets_hit_pos.append(target_shoot)
            total_targets -= 1

    elif command[0] == "move":
        my_pos = move(command[1], int(command[2]))

    if total_targets == 0:
        print(f"Training completed! All {len(targets_hit_pos)} targets hit.")
        break

else:
    print(f"Training not completed! {total_targets} targets left.")

print(*targets_hit_pos, sep="\n")
