from collections import deque


def task_complete():
    for firework_name, count in fireworks_data.items():
        if count < 3:
            return False

    return True


fireworks = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

fireworks_data = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while fireworks and explosive_power:
    if fireworks[0] <= 0:
        fireworks.popleft()
        continue

    elif explosive_power[-1] <= 0:
        explosive_power.pop()
        continue


    firework = fireworks.popleft()
    explosive = explosive_power.pop()

    total_sum = firework + explosive

    if total_sum % 3 == 0 and total_sum % 5 != 0:
        fireworks_data["Palm Fireworks"] += 1

    elif total_sum % 5 == 0 and total_sum % 3 != 0:
        fireworks_data["Willow Fireworks"] += 1

    elif total_sum % 3 == 0 and total_sum % 5 == 0:
        fireworks_data["Crossette Fireworks"] += 1

    else:
        fireworks.append(firework - 1)
        explosive_power.append(explosive)

    if task_complete():
        break

if task_complete():
    print("Congrats! You made the perfect firework show!")

else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for firework_name, count in fireworks_data.items():
    print(f"{firework_name}: {count}")
