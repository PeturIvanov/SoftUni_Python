from collections import deque

def flights(*args):
    flights_data = {}

    data = deque(args)

    while data:
        destination = data.popleft()

        if destination == "Finish":
            break

        passengers = int(data.popleft())

        flights_data[destination] = flights_data.get(destination, 0) + passengers

    return flights_data


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))