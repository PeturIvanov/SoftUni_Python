from collections import deque

substrings = deque(input().split())
all_colors = ["red", "yellow", "blue", "orange", "purple", "green"]

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
find_colors = []

while substrings:
    first_subst = substrings.popleft()
    second_subst = substrings.pop() if substrings else ""

    first_str = f"{first_subst}{second_subst}"
    second_str = f"{second_subst}{first_subst}"

    if first_str in all_colors or second_str in all_colors:
        find_colors.append(first_str if first_str in all_colors else second_str)

    else:
        first_subst = first_subst[:len(first_subst) - 1]
        second_subst = second_subst[:len(second_subst) - 1]
        if first_subst:
            substrings.insert(len(substrings) // 2, first_subst)
        if second_subst:
            substrings.insert(len(substrings) // 2, second_subst)

for el in find_colors:
    if el in secondary_colors:
        if not secondary_colors[el].issubset(find_colors):
            find_colors.remove(el)


print(find_colors)





