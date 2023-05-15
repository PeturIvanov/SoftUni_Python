number_of_lines = int(input())

odd_set = set()
even_set = set()

for row in range(1, number_of_lines + 1):
    name = input()

    sum_char = sum([ord(char) for char in name]) // row
    if sum_char % 2 == 0:
        even_set.add(sum_char)
    else:
        odd_set.add(sum_char)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(*odd_set.union(even_set), sep=", ")

elif odd_sum > even_sum:
    print(*odd_set.difference(even_set), sep=", ")

elif even_sum > odd_sum:
    print(*even_set.symmetric_difference(odd_set), sep=", ")