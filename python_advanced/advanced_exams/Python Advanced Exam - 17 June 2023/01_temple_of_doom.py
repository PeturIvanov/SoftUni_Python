from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])

challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    total_sum = current_tool * current_substance

    if total_sum in challenges:
        challenges.remove(total_sum)

    else:
        tools.append(current_tool + 1)

        if current_substance - 1 != 0:
            substances.append(current_substance - 1)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")

