from collections import deque

materials = deque([int(m) for m in input().split()])
magic = deque([int(m) for m in input().split()])

presents_data = {}

target = [{"Gemstone", "Porcelain Sculpture"}, {"Gold", "Diamond Jewellery"}]

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    total_sum = current_material + current_magic

    if total_sum < 100:

        if total_sum % 2 == 0:
            current_material *= 2
            current_magic *= 3
            total_sum = current_material + current_magic

        else:
            total_sum *= 2

    elif total_sum >= 500:
        total_sum /= 2


    if 100 <= total_sum < 200:
        presents_data["Gemstone"] = presents_data.get("Gemstone", 0) + 1

    elif 200 <= total_sum < 300:
        presents_data["Porcelain Sculpture"] = presents_data.get("Porcelain Sculpture", 0) + 1

    elif 300 <= total_sum < 400:
        presents_data["Gold"] = presents_data.get("Gold", 0) + 1

    elif 400 <= total_sum < 500:
        presents_data["Diamond Jewellery"] = presents_data.get("Diamond Jewellery", 0) + 1

if target[0].issubset(presents_data.keys()):
    print("The wedding presents are made!")

elif target[1].issubset(presents_data.keys()):
    print("The wedding presents are made!")

else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials])}")

elif magic:
    print(f"Magic left: {', '.join([str(m) for m in magic])}")

print('\n'.join([f"{present}: {count}" for present, count in sorted(presents_data.items())]))
