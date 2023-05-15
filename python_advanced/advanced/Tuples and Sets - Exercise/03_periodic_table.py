number_of_lines = int(input())

unique_el = set()

for _ in range(number_of_lines):
    compounds = input().split()
    for el in compounds:
        unique_el.add(el)

print(*unique_el, sep="\n")
