from collections import deque

bowls = deque([int(n) for n in input().split(", ")])
customers = deque([int(n) for n in input().split(", ")])

while bowls and customers:
    current_bowl = bowls.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        current_bowl -= current_customer

        bowls.append(current_bowl)

    elif current_bowl < current_customer:
        current_customer -= current_bowl

        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join([str(r) for r in bowls])}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(r) for r in customers])}")

