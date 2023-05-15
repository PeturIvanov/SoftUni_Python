n, m = input().split()

first_set_of_numbers = {int(input()) for _ in range(int(n))}
second_set_of_numbers = {int(input()) for _ in range(int(m))}

print(*(first_set_of_numbers.intersection(second_set_of_numbers)), sep="\n")
