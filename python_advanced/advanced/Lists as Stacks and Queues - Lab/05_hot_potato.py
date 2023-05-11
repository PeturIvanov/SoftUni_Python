from collections import deque

kids = input()
toss_count = int(input())

circle = deque(kids.split())

while len(circle) > 1:
    circle.rotate(-toss_count)
    eliminated_kid = circle.pop()
    print(f"Removed {eliminated_kid}")

print(f"Last is {circle[0]}")
