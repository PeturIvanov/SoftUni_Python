from collections import deque

boxes_of_materials = deque(int(m) for m in input().split())  # from Last
materials_magic_level = deque(int(x) for x in input().split())  # from First

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

toys_crafted = {}

while boxes_of_materials and materials_magic_level:
    box = boxes_of_materials.pop()
    magic_level = materials_magic_level.popleft()

    total_magic_level = box * magic_level

    if total_magic_level in toys:
        toy_crafted = toys[total_magic_level]
        toys_crafted[toy_crafted] = toys_crafted.get(toy_crafted, 0) + 1

    elif total_magic_level not in toys and total_magic_level > 0:
        boxes_of_materials.append(box + 15)

    elif total_magic_level < 0:
        sum_values = box + magic_level
        boxes_of_materials.append(sum_values)

    else:
        if box != 0:
            boxes_of_materials.append(box)
        if magic_level != 0:
            materials_magic_level.appendleft(magic_level)

if ("Doll" in toys_crafted and "Wooden train" in toys_crafted) or (
        "Teddy bear" in toys_crafted and "Bicycle" in toys_crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_of_materials:
    print(f"Materials left: {', '.join(str(m) for m in reversed(boxes_of_materials))}")
if materials_magic_level:
    print(f"Magic left: {', '.join(str(m) for m in materials_magic_level)}")

for toy, amount in sorted(toys_crafted.items()):
    print(f"{toy}: {amount}")

