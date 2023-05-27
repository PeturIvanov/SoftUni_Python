from collections import deque

programmers_times = deque([int(x) for x in input().split()])
tasks = deque([int(x) for x in input().split()])

ducks_data = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while tasks:
    time = programmers_times.popleft()
    task = tasks.pop()

    total_time = time * task

    if 0 < total_time <= 60:
        ducks_data["Darth Vader Ducky"] += 1

    elif 60 < total_time <= 120:
        ducks_data["Thor Ducky"] += 1

    elif 120 < total_time <= 180:
        ducks_data["Big Blue Rubber Ducky"] += 1

    elif 180 < total_time <= 240:
        ducks_data["Small Yellow Rubber Ducky"] += 1

    else:
        programmers_times.append(time)
        tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
print(*[f"{duck}: {value}" for duck, value in ducks_data.items()], sep="\n")











