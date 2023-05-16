from collections import deque

chocolates = deque(int(c) for c in input().split(", "))  # start from last
cups_of_milk = deque(int(m) for m in input().split(", "))  # start from first

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup_of_milk <= 0:
        continue
    if current_cup_of_milk <= 0:
        chocolates.append(current_chocolate)
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_of_milk)
        continue

    if current_chocolate == current_cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(current_cup_of_milk)
        chocolates.append(current_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(el)for el in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(el)for el in cups_of_milk)}")
else:
    print("Milk: empty")


