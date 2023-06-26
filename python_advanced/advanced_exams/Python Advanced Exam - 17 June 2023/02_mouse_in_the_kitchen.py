rows, cols = [int(x) for x in input().split(",")]

cup_board = []

mouse_pos = []

total_cheese = 0

for row in range(rows):
    cup_board.append(list(input()))

    if "M" in cup_board[row]:
        mouse_pos = [row, cup_board[row].index("M")]

        cup_board[mouse_pos[0]][mouse_pos[1]] = "*"

    total_cheese += cup_board[row].count("C")

directions = {
    "up": (-1, 0),  # up
    "down": (1, 0),  # down
    "left": (0, -1),  # left
    "right": (0, 1)  # right
}

while total_cheese != 0:
    direction = input()

    if direction == "danger":
        print("Mouse will come back later!")
        break

    r = mouse_pos[0] + directions[direction][0]
    c = mouse_pos[1] + directions[direction][1]

    if not (0 <= r < rows and 0 <= c < cols):
        print("No more cheese for tonight!")
        break

    position = cup_board[r][c]

    if position == "C":
        total_cheese -= 1
        cup_board[r][c] = "*"
        mouse_pos = [r, c]

    elif position == "T":
        mouse_pos = [r, c]

        print("Mouse is trapped!")
        break

    elif position == "*":
        mouse_pos = [r, c]


else:
    print("Happy mouse! All the cheese is eaten, good night!")

cup_board[mouse_pos[0]][mouse_pos[1]] = "M"

print('\n'.join([''.join(row) for row in cup_board]))




















