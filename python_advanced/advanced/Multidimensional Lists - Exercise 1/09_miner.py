size = int(input())

field = []
miner_pos = []

total_coal = 0
coal_collected = 0

moves = input().split()

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

for row in range(size):
    field.append(input().split())

    if "s" in field[row]:
        miner_pos = [row, field[row].index("s")]
        field[miner_pos[0]][miner_pos[1]] = "*"

    total_coal += field[row].count("c")

for move in moves:

    row = miner_pos[0] + directions[move][0]
    col = miner_pos[1] + directions[move][1]

    if not (0 <= row < size and 0 <= col < size):
        continue

    miner_pos = row, col

    position_value = field[row][col]

    if position_value == "c":
        coal_collected += 1
        total_coal -= 1
        field[row][col] = "*"

    elif position_value == "e":
        print(f"Game over! ({miner_pos[0]}, {miner_pos[1]})")
        break

    if total_coal == 0:
        print(f"You collected all coal! ({miner_pos[0]}, {miner_pos[1]})")
        break

else:
    print(f"{total_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
