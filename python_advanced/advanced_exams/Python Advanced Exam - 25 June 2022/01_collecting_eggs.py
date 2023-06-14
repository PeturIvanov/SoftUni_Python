from collections import deque

eggs = deque([int(n) for n in input().split(", ")])

papers = deque([int(n) for n in input().split(", ")])

BOX_SIZE = 50

total_boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.pop()

    total_sum = current_egg + current_paper

    if total_sum <= BOX_SIZE:
        total_boxes += 1

if total_boxes:
    print(f"Great! You filled {total_boxes} boxes.")

else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(e) for e in eggs])}")

elif papers:
    print(f"Pieces of paper left: {', '.join([str(e) for e in papers])}")


