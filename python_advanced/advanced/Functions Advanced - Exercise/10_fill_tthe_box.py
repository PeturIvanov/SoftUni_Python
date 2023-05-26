from collections import deque


def fill_the_box(height, length, width, *data):
    box_space = height * length * width
    data = deque(data)

    while data and box_space > 0:
        cubes_amount = data.popleft()

        if cubes_amount == "Finish":
            break

        if box_space - cubes_amount >= 0:
            box_space -= cubes_amount

        else:
            cubes_remain = cubes_amount - box_space
            box_space -= (cubes_amount - cubes_remain)
            data.append(cubes_remain)

    if box_space > 0:
        return f"There is free space in the box. You could put {box_space} more cubes."
    else:
        cubes_left = sum([el for el in data if el != "Finish"])
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(10, 10,
10, 40, "Finish", 2, 15,
30))

