from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = deque([int(x) for x in input().split()])

wasted_water = 0

while cups_capacity and bottles_capacity:
    current_cup_value = cups_capacity.popleft()

    while current_cup_value > 0:
        if bottles_capacity:
            current_bottle_litres = bottles_capacity.pop()
            if current_cup_value < current_bottle_litres:
                wasted_water += current_bottle_litres - current_cup_value
                current_cup_value -= current_bottle_litres
            else:
                current_cup_value -= current_bottle_litres
        else:
            cups_capacity.appendleft(current_cup_value)

if not cups_capacity:
    bottles_left = " ".join([str(x) for x in reversed(bottles_capacity)])
    print(f"Bottles: {bottles_left}")
    print(f"Wasted litters of water: {wasted_water}")

else:
    cups_left = " ".join([str(x) for x in cups_capacity])
    print(f"Cups: {cups_left}\nWasted litters of water: {wasted_water}")