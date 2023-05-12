from collections import deque
from datetime import datetime, timedelta

robots_data = {}

for r in input().split(";"):
    robot_name, process_time = r.split("-")
    robots_data[robot_name] = [int(process_time), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

while True:
    product = input()
    if product == "End":
        break

    products.append(product)


while products:
    factory_time += timedelta(0, 1)

    current_product = products.popleft()

    free_robots = deque()

    for robot in robots_data.keys():
        if robots_data[robot][1] != 0:
            robots_data[robot][1] -= 1

        if robots_data[robot][1] == 0:
            free_robots.append(robot)

    if free_robots:
        current_robot = free_robots.popleft()
        robots_data[current_robot][1] += robots_data[current_robot][0]
        print(f"{current_robot} - {current_product} [{factory_time.time()}]")

    else:
        products.append(current_product)
