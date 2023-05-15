number_of_lines = int(input())

names = set()

for _ in range(number_of_lines):
    name = input()
    names.add(name)

print(*names, sep="\n")
