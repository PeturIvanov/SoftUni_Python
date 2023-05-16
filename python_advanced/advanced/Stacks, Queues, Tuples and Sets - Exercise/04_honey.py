from collections import deque


def hive(matched_bee, matched_nectar):
    symbol = symbols.popleft()
    honey_made = 0
    if symbol == "+":
        honey_made = abs(matched_bee + matched_nectar)
    elif symbol == "-":
        honey_made = abs(matched_bee - matched_nectar)
    elif symbol == "*":
        honey_made = abs(matched_bee * matched_nectar)
    elif symbol == "/" and matched_bee != 0 and matched_nectar != 0:
        honey_made = abs(matched_bee / matched_nectar)
    return honey_made


working_bees = deque(int(b)for b in input().split())
nectar = deque(int(n) for n in input().split())
symbols = deque(input().split())

total_honey_made = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    nectar_amount = nectar.pop()

    if nectar_amount >= current_bee:
        total_honey_made += hive(current_bee, nectar_amount)

    else:
        working_bees.appendleft(current_bee)
        continue

print(f"Total honey made: {total_honey_made}")
if working_bees:
    print(f"Bees left: {', '.join(str(b) for b in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(n) for n in nectar)}")
