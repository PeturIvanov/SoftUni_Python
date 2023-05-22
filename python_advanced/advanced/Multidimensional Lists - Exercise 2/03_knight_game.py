n = int(input())

field = [list(input()) for _ in range(n)]

directions = (
    (-2, -1),
    (-1, -2),
    (-2, 1),
    (-1, 2),
    (1, -2),
    (2, -1),
    (1, 2),
    (2, 1)
)

knights_removed = 0

while True:
    max_attacks = 0
    knight_with_most_attacks = []

    for row in range(n):
        for col in range(n):
            if field[row][col] == "K":

                attacks_current_knight = 0

                for pos in directions:
                    r = row + pos[0]
                    c = col + pos[1]

                    if 0 <= r < n and 0 <= c < n:
                        if field[r][c] == "K":
                            attacks_current_knight += 1

                if attacks_current_knight > max_attacks:
                    knight_with_most_attacks = [row, col]
                    max_attacks = attacks_current_knight

    if max_attacks == 0:
        print(knights_removed)
        break

    field[knight_with_most_attacks[0]][knight_with_most_attacks[1]] = "0"
    knights_removed += 1
