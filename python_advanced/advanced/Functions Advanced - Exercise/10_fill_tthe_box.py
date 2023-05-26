from collections import deque


def fill_the_box(height, length, width, *data):
    box_space = height * length * width
    data = deque(data)

    while data[0] != "Finish":
        cubes_amount = data.popleft()

        box_space -= cubes_amount

        if box_space < 0:
            cubes_left = sum([el for el in data if el != "Finish"])
            return f"No more free space! You have {cubes_left + abs(box_space)} more cubes."

    return f"There is free space in the box. You could put {box_space} more cubes."


print(fill_the_box(2, 8,
2, 2, 1, 7, 3, 1, 5,
"Finish"))
