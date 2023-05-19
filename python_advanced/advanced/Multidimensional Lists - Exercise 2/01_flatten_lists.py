matrix = [el.split() for el in input().split("|")]

flatten = [num for el in reversed(matrix) for num in el]
print(*flatten)