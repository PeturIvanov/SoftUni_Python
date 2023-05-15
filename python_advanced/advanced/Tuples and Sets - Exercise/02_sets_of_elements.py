n, m = input().split()

first_set_of_numbers = set()
second_set_of_numbers = set()

for _ in range(int(n)):
    number = int(input())
    first_set_of_numbers.add(number)

for _ in range(int(m)):
    number = int(input())
    second_set_of_numbers.add(number)

print(*(first_set_of_numbers.intersection(second_set_of_numbers)), sep="\n")
