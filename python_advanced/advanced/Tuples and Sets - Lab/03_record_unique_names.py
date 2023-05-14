names_count = int(input())

names = set()

for _ in range(names_count):
    names.add(input())

for name in names:
    print(name)