from collections import deque

orders = deque([int(n) for n in input().split(", ")])
employees = deque([int(n) for n in input().split(", ")])

total_pizzas = 0

while orders and employees:
    order = orders.popleft()

    if order > 10 or order <= 0:
        continue

    while order != 0:
        if not employees:
            orders.appendleft(order)
            break

        employee = employees.pop()

        if order <= employee:
            total_pizzas += order
            order = 0

        elif order > employee:
            total_pizzas += employee

            order -= employee

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")

elif not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")


