from collections import deque

seats = {s: "free" for s in input().split(", ")}
first_sequence = deque([int(n) for n in input().split(", ")])
second_sequence = deque([int(n) for n in input().split(", ")])

rotations = 0
taken_seats = []

while rotations < 10 and len(taken_seats) < 3:
    rotations += 1

    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    character = chr(first_number + second_number)
    first_combination, second_combination = f"{first_number}{character}", f"{second_number}{character}"

    if first_combination in seats:
        if seats[first_combination] == "free":
            seats[first_combination] = "taken"
            taken_seats.append(first_combination)

    elif second_combination in seats:
        if seats[second_combination] == "free":
            seats[second_combination] = "taken"
            taken_seats.append(second_combination)

    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)


print(f"Seat matches: {', '.join([s for s in taken_seats])}")

print(f"Rotations count: {rotations}")



