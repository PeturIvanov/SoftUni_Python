from collections import deque


pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
gas_in_tank = 0
index = 0
circle = pumps_data.copy()

while circle:
    gas, kilometers = circle.popleft()

    gas_in_tank += gas

    if gas_in_tank >= kilometers:
        gas_in_tank -= kilometers

    else:
        gas_in_tank = 0
        index += 1
        circle = pumps_data.copy()
        circle.rotate(-1)

print(index)