presents_count = int(input())
size = int(input())

neighborhood = []
santa_pos = []

total_nice_kid = 0
happy_kids = 0

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1),  # right
}

for row in range(size):
    neighborhood.append(input().split())

    if "S" in neighborhood[row]:
        santa_pos = [row, neighborhood[row].index("S")]
        neighborhood[row][neighborhood[row].index("S")] = "-"

    total_nice_kid += neighborhood[row].count("V")


while presents_count > 0:
    command = input()
    if command == "Christmas morning":
        break

    row = santa_pos[0] + directions[command][0]
    col = santa_pos[1] + directions[command][1]

    if 0 <= row < size and 0 <= col < 0:
        continue

    house = neighborhood[row][col]

    if house == "V":
        happy_kids += 1
        presents_count -= 1
        total_nice_kid -= 1

    elif house == "C":
        for direction in directions.values():
            r = row + direction[0]
            c = col + direction[1]

            if neighborhood[r][c] in "VX":
                if neighborhood[r][c] == "V":
                    happy_kids += 1
                    total_nice_kid -= 1

                neighborhood[r][c] = "-"
                presents_count -= 1

    neighborhood[row][col] = "-"
    santa_pos = [row, col]

neighborhood[santa_pos[0]][santa_pos[1]] = "S"

if presents_count == 0 and total_nice_kid > 0:
    print("Santa ran out of presents!")

print(*[" ".join(el) for el in neighborhood], sep="\n")

if total_nice_kid == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")

else:
    print(f"No presents for {total_nice_kid} nice kid/s.")
