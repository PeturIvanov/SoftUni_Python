n = int(input())
matrix = [input() for _ in range(n)]

symbol = input()

for row_index in range(n):
    for column_index in range(n):
        current_element = matrix[row_index][column_index]
        if current_element == symbol:
            print((row_index, column_index))
            exit(0)
print(f"{symbol} does not occur in the matrix")
