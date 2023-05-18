def valid_input(indexes, command):
    if command != "swap" or len(indexes) != 4:
        return False

    if (indexes[0] >= rows or 0 > indexes[0]) or (indexes[2] >= rows or 0 > indexes[2]):
        return False
    elif (indexes[1] >= columns or 0 > indexes[1]) or (indexes[3] >= columns or 0 > indexes[3]):
        return False

    return True


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command, *data = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    if valid_input(data, command):
        row1, col1, row2, col2 = data

        matrix[row1][col1], matrix[row2][col2] = \
            matrix[row2][col2], matrix[row1][col1]

        for el in matrix:
            print(*el)
    else:
        print("Invalid input!")
