reservations_count = int(input())

reservations = set()

for _ in range(reservations_count):
    reservation_number = input()
    reservations.add(reservation_number)

while True:
    guest_number = input()
    if guest_number == "END":
        break

    reservations.remove(guest_number)


print(len(reservations))
print(*(sorted(reservations)), sep="\n")
