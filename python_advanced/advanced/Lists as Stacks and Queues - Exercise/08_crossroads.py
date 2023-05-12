from collections import deque

green_light_duration = int(input())
green_light_duration_copy = green_light_duration

free_window_duration = int(input())
free_window_duration_copy = free_window_duration

lane_of_cars = deque()

total_cars_passed = 0

while True:
    command = input()
    green_light_duration_copy = green_light_duration
    free_window_duration_copy = free_window_duration

    if command == "END":
        break

    if command != "green":
        lane_of_cars.append(command)

    if command == "green":
        while lane_of_cars and green_light_duration_copy != 0:
            car_to_pass = lane_of_cars.popleft()
            cars_chars = deque(car_to_pass)

            while cars_chars:
                char = cars_chars.popleft()
                if green_light_duration_copy != 0:
                    green_light_duration_copy -= 1
                elif free_window_duration_copy != 0:
                    free_window_duration_copy -= 1
                else:
                    print("A crash happened!")
                    print(f"{car_to_pass} was hit at {char}.")
                    exit()

            total_cars_passed += 1


print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")
