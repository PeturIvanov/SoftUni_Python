from collections import deque

queue = deque()

while True:
    name = input()
    if name == "Paid":
        while queue:
            print(queue.popleft())
        continue
    elif name == "End":
        print(f"{len(queue)} people remaining.")
        break

    queue.append(name)
