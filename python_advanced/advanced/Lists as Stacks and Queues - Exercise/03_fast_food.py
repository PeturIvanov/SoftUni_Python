from collections import deque

food_quantity = int(input())

orders = [int(n) for n in input().split()]
queue = deque(orders)
print(max(queue))

for order in orders:
    if food_quantity >= order:
        food_quantity -= order
        queue.popleft()
    else:
        break

if queue:
    print(f"Orders left: ", end="")
    print(*queue, sep=" ")
else:
    print("Orders complete")
