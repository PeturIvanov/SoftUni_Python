import re
def bucket_hit(bucket_col):
    points = 0

    for r in range(SIZE):
        if board[r][bucket_col].isdigit():
            points += int(board[r][bucket_col])

    return points


SIZE = 6

THROW = 3

board = []

for _ in range(SIZE):
    board.append([el for el in input().split()])

buckets_hit = []

points_collected = 0

for _ in range(THROW):
    row, col = [int(x) for x in re.findall(r"\d+", input())]

    if not (0 <= row < SIZE and 0 <= col < SIZE):
        continue

    if board[row][col] == "B":
        if [row, col] not in buckets_hit:
            buckets_hit.append([row, col])

            points_collected += bucket_hit(col)

if points_collected < 100:
    print(f"Sorry! You need {100 - points_collected} points more to win a prize.")

else:
    if points_collected < 200:
        print(f"Good job! You scored {points_collected} points, and you've won Football.")

    elif points_collected < 300:
        print(f"Good job! You scored {points_collected} points, and you've won Teddy Bear.")

    else:
        print(f"Good job! You scored {points_collected} points, and you've won Lego Construction Set.")


