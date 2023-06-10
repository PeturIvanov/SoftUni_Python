size = int(input())

car_number = input()

field = []

tunnels_pos = []

car_pos = [0, 0]

total_km = 0

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1)  # right
}

for r in range(size):
    field.append(input().split())

    if "T" in field[r]:
        tunnels_pos.append([r, field[r].index("T")])

while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break

    row = car_pos[0] + directions[command][0]
    col = car_pos[1] + directions[command][1]

    car_pos = [row, col]
    total_km += 10

    if field[row][col] == "T":
        total_km += 20
        field[row][col] = "."

        if car_pos != tunnels_pos[0]:
            car_pos = tunnels_pos[0]

        else:
            car_pos = tunnels_pos[1]

        field[car_pos[0]][car_pos[1]] = "."

    if field[row][col] == "F":
        print(f"Racing car {car_number} finished the stage!")
        break

field[car_pos[0]][car_pos[1]] = "C"

print(f"Distance covered {total_km} km.")

print(*[''.join(row) for row in field], sep="\n")
