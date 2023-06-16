import re

def double_triple_points(row, col, player, bonus):
    total_points = 0

    total_points += int(dartboard[0][col]) + int(dartboard[-1][col]) + int(dartboard[row][0]) + int(dartboard[row][-1])

    if bonus == "D":
        player[1] -= total_points * 2

    else:
        player[1] -= total_points * 3


players = input().split(", ")

SIZE = 7

dartboard = [input().split() for _ in range(SIZE)]

current_player = [players[0], 501, 0]
next_player = [players[1], 501, 0]

while True:
    r, c = [int(x) for x in re.findall(r"\d+", input())]

    current_player[2] += 1

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        current_player, next_player = next_player, current_player
        continue

    position = dartboard[r][c]

    if position.isdigit():
        current_player[1] -= int(position)

    elif position == "B":
        print(f"{current_player[0]} won the game with {current_player[2]} throws!")
        break

    else:
        double_triple_points(r, c, current_player, position)

    if current_player[1] <= 0:
        print(f"{current_player[0]} won the game with {current_player[2]} throws!")
        break

    current_player, next_player = next_player, current_player

