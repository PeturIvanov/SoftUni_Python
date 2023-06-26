def draw_rhombus(n, count):
    print(" " * (n - count), end="")
    print(*["*"] * count)


def upper_part(n):
    for count in range(1, n + 1):
        draw_rhombus(n, count)


def bottom_part(n):
    for count in range(n - 1, 0, -1):
        draw_rhombus(n, count)


n = int(input())
upper_part(n)
bottom_part(n)