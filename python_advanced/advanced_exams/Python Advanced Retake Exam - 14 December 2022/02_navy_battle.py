size = int(input())

battlefield = []

submarine_pos = []
submarine_health = 3

cruiser_destroyed = 0


for row in range(size):
    battlefield.append(list(input()))

    if "S" in battlefield[row]:
        submarine_pos = [row, battlefield[row].index("S")]
        battlefield[submarine_pos[0]][submarine_pos[1]] = "-"

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

while True:
    command = input()

    r = submarine_pos[0] + directions[command][0]
    c = submarine_pos[1] + directions[command][1]

    if battlefield[r][c] == "*":
        submarine_health -= 1

    elif battlefield[r][c] == "C":
        cruiser_destroyed += 1

    battlefield[r][c] = "-"

    submarine_pos = [r, c]

    if submarine_health == 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
        break

    if cruiser_destroyed == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

battlefield[submarine_pos[0]][submarine_pos[1]] = "S"

print(*[''.join(el) for el in battlefield], sep="\n")
