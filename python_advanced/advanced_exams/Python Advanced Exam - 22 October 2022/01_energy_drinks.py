from collections import deque

MAX_COFFEINE = 300

stamat_init_coffeine = 0

milligrams_of_coffeine = deque([int(x) for x in input().split(", ")])

energy_drinks = deque([int(x) for x in input().split(", ")])

while milligrams_of_coffeine and energy_drinks:
    current_milligrams = milligrams_of_coffeine.pop()
    current_drink = energy_drinks.popleft()

    total_sum = current_drink * current_milligrams

    if stamat_init_coffeine + total_sum <= MAX_COFFEINE:
        stamat_init_coffeine += total_sum

    else:
        energy_drinks.append(current_drink)

        if stamat_init_coffeine - 30 >= 0:
            stamat_init_coffeine -= 30
        else:
            stamat_init_coffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(drink) for drink in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_init_coffeine} mg caffeine.")
