n = int(input())

field = []
alice_pos = []

total_tea = 0

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

for row in range(n):
    field.append(input().split())
    if "A" in field[row]:
        alice_pos = [row, field[row].index("A")]
        field[row][alice_pos[1]] = "*"


while total_tea < 10:
    command = input()

    r = alice_pos[0] + directions[command][0]
    c = alice_pos[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        break

    alice_pos = [r, c]
    territory_value = field[r][c]
    field[r][c] = "*"

    if territory_value == "R":

        break

    elif territory_value.isdigit():
        total_tea += int(territory_value)


if total_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[" ".join(el) for el in field], sep="\n")
