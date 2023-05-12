from collections import deque

all_parenthesis = deque(input())
open_parenthesis = deque()


while all_parenthesis:
    current_parenthesis = all_parenthesis.popleft()

    if current_parenthesis in "([{":
        open_parenthesis.append(current_parenthesis)

    else:
        if not open_parenthesis:
            print("NO")
            break

        parenthesis = open_parenthesis.pop()

        if f"{parenthesis}{current_parenthesis}" not in "(){}[]":
            print("NO")
            break
else:
    print("YES")

