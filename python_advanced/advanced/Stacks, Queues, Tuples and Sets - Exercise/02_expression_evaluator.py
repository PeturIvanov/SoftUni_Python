from collections import deque

string = deque(input().split())

numbers = deque()

while string:
    char = string.popleft()

    if char not in "-*/+":
        numbers.append(int(char))

    else:
        result = numbers.popleft()

        while numbers:
            digit = numbers.popleft()

            if char == "-":
                result -= digit

            elif char == "+":
                result += digit

            elif char == "*":
                result *= digit

            else:
                result //= digit
                
        string.appendleft(str(result))

        if len(string) == 1:
            print(*string)
            break
