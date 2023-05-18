rows, columns = [int(x) for x in input().split()]

matrix = []

first_char = 97

for i in range(rows):
    matrix.append([f"{chr(first_char + i)}{chr(first_char + j + i)}{chr(first_char + i)}" for j in range(columns)])

    # inner_row = []
    #  for j in range(columns):
    #      element = f"{chr(first_char + i)}{chr(first_char + j + i)}{chr(first_char + i)}"
    #      inner_row.append(element)
    #
    #  matrix.append(inner_row)

for el in matrix:
    print(*el)

