number_of_lines = int(input())

longest_intersection = set()

for _ in range(number_of_lines):
    first_range, second_range = input().split("-")

    first_start, first_end = [int(n) for n in first_range.split(",")]
    second_start, second_end = [int(n) for n in second_range.split(",")]

    first_intersection = set([i for i in range(first_start, first_end + 1)])
    second_intersection = set([i for i in range(second_start, second_end + 1)])

    current_intersection = first_intersection.intersection(second_intersection)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = list(current_intersection)


print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")


