from collections import deque

substrings = deque(input().split())
all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
find_colors = []

while substrings:
    first_subst = substrings.popleft()
    second_subst = substrings.pop() if substrings else ""

    for color in (first_subst + second_subst, second_subst + first_subst):
        if color in all_colors:
            find_colors.append(color)
            break

    else:
        for el in (first_subst[:-1], second_subst[:-1]):
            if el:
                substrings.insert(len(substrings) // 2, el)


for el in set(secondary_colors.keys()).intersection(find_colors):
    if not secondary_colors[el].issubset(find_colors):
        find_colors.remove(el)

print(find_colors)
