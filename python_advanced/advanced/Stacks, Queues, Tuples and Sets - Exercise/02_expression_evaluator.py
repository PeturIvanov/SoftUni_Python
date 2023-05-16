from collections import deque
from functools import reduce

string = deque(input().split())

numbers = deque()

# Solution using reduce module
while string:
    char = string.popleft()

    if char not in "-*/+":
        numbers.append(int(char))

    else:
        if char == "-":
            result = reduce(lambda a, b: a - b, numbers)

        elif char == "+":
            result = sum(numbers)

        elif char == "*":
            result = reduce(lambda a, b: a * b, numbers)

        else:
            result = reduce(lambda a, b: a // b, numbers)

        string.appendleft(str(result))
        numbers.clear()

        if len(string) == 1:
            print(*string)
            break

# Second solution
# string = deque(input().split())
#
# numbers = deque()
#
# while string:
#     char = string.popleft()
#
#     if char not in "-*/+":
#         numbers.append(int(char))
#
#     else:
#         result = numbers.popleft()
#
#         while numbers:
#             digit = numbers.popleft()
#
#             if char == "-":
#                 result -= digit
#
#             elif char == "+":
#                 result += digit
#
#             elif char == "*":
#                 result *= digit
#
#             else:
#                 result //= digit
#
#         string.appendleft(str(result))
#
#         if len(string) == 1:
#             print(*string)
#             break
