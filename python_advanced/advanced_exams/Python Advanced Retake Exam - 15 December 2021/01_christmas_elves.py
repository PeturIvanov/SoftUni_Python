from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy = 0

toys_created = 0

box_counter = 0

while elfs_energy and materials:
    current_elf = elfs_energy.popleft()

    if current_elf < 5:
        continue

    current_box = materials.pop()
    box_counter += 1

    if box_counter % 3 == 0:
        if current_elf >= current_box * 2:
            energy_spent = current_box * 2

            total_energy += energy_spent

            if box_counter % 5 == 0:
                elfs_energy.append(current_elf - energy_spent)

            else:
                toys_created += 2
                elfs_energy.append(current_elf - energy_spent + 1)

        else:
            materials.append(current_box)
            elfs_energy.append(current_elf * 2)

    elif current_elf >= current_box:
        energy_spent = current_box

        total_energy += energy_spent

        if box_counter % 5 == 0:
            elfs_energy.append(current_elf - energy_spent)

        else:
            elfs_energy.append(current_elf - energy_spent + 1)
            toys_created += 1

    else:
        materials.append(current_box)
        elfs_energy.append(current_elf * 2)

print(f"Toys: {toys_created}")
print(f"Energy: {total_energy}")

if elfs_energy:
    print(f"Elves left: {', '.join([str(n) for n in elfs_energy])}")

elif materials:
    print(f"Boxes left: {', '.join([str(n) for n in materials])}")
