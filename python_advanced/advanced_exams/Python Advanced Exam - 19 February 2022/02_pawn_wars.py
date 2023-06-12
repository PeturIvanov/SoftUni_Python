def is_attack_possible(white_pos, black_pos):
    if (white_pos[1] + 1 == black_pos[1]) or (white_pos[1] - 1 == black_pos[1]):
        return True

    return False


size = 8

field = []

white_pos = []

black_pos = []

cols_symbols = "abcdefgh"

for row in range(size):
    field.append(input().split())

    if "w" in field[row]:
        white_pos = [row, field[row].index("w")]

    elif "b" in field[row]:
        black_pos = [row, field[row].index("b")]

if not is_attack_possible(white_pos, black_pos):

    black_path = size - black_pos[0] - 1
    white_path = size - (size - white_pos[0])

    if white_path <= black_path:
        print(f"Game over! White pawn is promoted to a queen at {cols_symbols[white_pos[1]]}8.")

    else:
        print(f"Game over! Black pawn is promoted to a queen at {cols_symbols[black_pos[1]]}1.")

else:
    range_between = abs(white_pos[0] - black_pos[0] - 1)

    if range_between % 2 == 0:
        position = size - int((white_pos[0] + black_pos[0]) / 2)

        print(f"Game over! White win, capture on {cols_symbols[black_pos[1]]}{int(position)}.")
    else:
        position = size - int((white_pos[0] + black_pos[0]) / 2)
        print(f"Game over! Black win, capture on {cols_symbols[white_pos[1]]}{position}.")
