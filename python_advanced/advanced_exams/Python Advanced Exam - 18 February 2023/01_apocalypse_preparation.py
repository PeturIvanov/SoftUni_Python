from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

created_items = {}

while textiles and medicaments:
    textile_value = textiles.popleft()
    medicament_value = medicaments.pop()

    total_value = textile_value + medicament_value

    if total_value == 30:
        created_items["Patch"] = created_items.get("Patch", 0) + 1

    elif total_value == 40:
        created_items["Bandage"] = created_items.get("Bandage", 0) + 1

    elif total_value == 100:
        created_items["MedKit"] = created_items.get("MedKit", 0) + 1

    elif total_value > 100:
        created_items["MedKit"] = created_items.get("MedKit", 0) + 1
        materials_remainder = medicaments.pop() + total_value - 100
        medicaments.append(materials_remainder)

    else:
        medicaments.append(medicament_value + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

else:
    print("Medicaments are empty.")

if created_items:
    sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    print("\n".join(f"{item} - {count}" for item, count in sorted_items))

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")

elif textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
