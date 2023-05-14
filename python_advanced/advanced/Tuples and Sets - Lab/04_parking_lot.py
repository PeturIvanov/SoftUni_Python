number_of_lines = int(input())

parking_lot = set()

for _ in range(number_of_lines):
    command, number = input().split(", ")

    if command == "IN":
        parking_lot.add(number)
    else:
        parking_lot.remove(number)

if parking_lot:
    print(*parking_lot, sep="\n")
else:
    print("Parking Lot is Empty")
