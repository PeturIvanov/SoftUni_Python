from collections import deque

water_quantity = int(input())

queue = deque()

name = input()
while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_needed = int(data[0])
        if water_quantity >= liters_needed:
            water_quantity -= liters_needed
            person = queue.popleft()
            print(f"{person} got water")
        else:
            person = queue.popleft()
            print(f"{person} must wait")
    else:
        liters_to_refill = int(data[1])
        water_quantity += liters_to_refill
    command = input()

print(f"{water_quantity} liters left")