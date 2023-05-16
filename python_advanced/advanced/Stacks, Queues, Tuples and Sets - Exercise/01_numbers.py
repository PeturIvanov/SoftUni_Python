first_sequence = set(int(n) for n in input().split())
second_sequence = set(int(n) for n in input().split())

for _ in range(int(input())):
    input_data = input().split()

    command = input_data[0]

    if command == "Add":
        numbers_to_add = set(map(int, input_data[2:]))

        if input_data[1] == "First":
            first_sequence = first_sequence.union(numbers_to_add)

        else:
            second_sequence = second_sequence.union(numbers_to_add)

    elif command == "Remove":
        numbers_to_remove = set(map(int, input_data[2:]))

        if input_data[1] == "First":
            set(first_sequence.remove(n) for n in numbers_to_remove if n in first_sequence)

        else:
            set(second_sequence.remove(n) for n in numbers_to_remove if n in second_sequence)

    else:
        print(second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence))

print(*(sorted(first_sequence)), sep=", ")
print(*(sorted(second_sequence)), sep=", ")

