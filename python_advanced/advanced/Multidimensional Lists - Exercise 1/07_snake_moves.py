from collections import deque
rows, columns = [int(x) for x in input().split()]

snake = deque(input())

snake_path = []

for i in range(rows):
    inner_path = []
    for j in range(columns):
        body_peace = snake.popleft()
        inner_path.append(body_peace)
        snake.append(body_peace)
    if i % 2 == 0:
        snake_path.append("".join(inner_path))
    else:
        snake_path.append("".join(inner_path[::-1]))

for el in snake_path:
    print(el)



